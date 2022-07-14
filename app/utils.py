import torch
from transformers import BertTokenizer, BertModel
from sklearn.metrics.pairwise import cosine_similarity


def pure_format(word):
    return word.strip().replace('\n', '').replace('\r', '').replace(' ', '')


# 这是查重的函数的实现
def check_text(texts):
    tz = BertTokenizer.from_pretrained('bert_cn')
    bert_model = BertModel.from_pretrained('bert_cn')
    tokens = {'input_ids': [], 'attention_mask': []}

    for t in texts:
        new_tokens = tz.encode_plus(t, max_length=512, truncation=True, padding='max_length', return_tensors='pt')
        tokens['input_ids'].append(new_tokens['input_ids'][0])
        tokens['attention_mask'].append(new_tokens['attention_mask'][0])

    tokens['input_ids'] = torch.stack(tokens['input_ids'])
    tokens['attention_mask'] = torch.stack(tokens['attention_mask'])

    output = bert_model(**tokens)
    embeddings = output.last_hidden_state

    attention_mask = tokens['attention_mask']
    mask = attention_mask.unsqueeze(-1).expand(embeddings.size()).float()

    masked_embeddings = embeddings * mask

    summed = torch.sum(masked_embeddings, 1)
    summed_mask = torch.clamp(mask.sum(1), min=1e-9)
    mean_pooled = summed / summed_mask
    mean_pooled = mean_pooled.detach().numpy()

    res = cosine_similarity(
        [mean_pooled[0]],
        mean_pooled[1:]
    )

    return res