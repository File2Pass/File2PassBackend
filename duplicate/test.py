from transformers import BertTokenizer, BertModel
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


# 需要安装pytorch，transformers
tz = BertTokenizer.from_pretrained('bert_cn')
bert_model = BertModel.from_pretrained('bert_cn')


def sent_tensor(sent):
    tokens = tz(sent, padding=True, max_length=100, truncation=True, return_tensors='pt')
    output = bert_model(**tokens)
    last_hidden_state = output[1]
    return last_hidden_state


t = "中国改革开放以来，字母词在汉语中大量涌现。这种现象是社会发" \
    "展需求和字母词自身优势使然。字" \
    "母词具有使用数量大，分布广泛，流通度高的传播特点；由字母语素构词，很难观形知义的词形" \
    "特点；以及存在大量同形、异形和书写错误进而影响交际的使用弊端。因此，汉语要不要欣然接纳字母词的争论一直持" \
    "续至今。从央视屏蔽令到《现代汉语词典》第 6 版被指违法，字母词使用问题每隔几年便翻出来讨论一番。应对字母词数量连年增多，分布甚广，使用中争议和误解尚需解释引导的使用现状，仍需全面反映字母词使用面貌的字母"

res = sent_tensor(t)
res2 = sent_tensor("本项目的研究对象、总体框架、重点难点、主要目标等")
res3 = sent_tensor("在学术思想、学术观点、研究方法等方面的特色和创新，和同类研究相比所具有的优势和特点")
res4 = sent_tensor("由此可见，是否汉化，是否与汉语和汉字产生联系是影响其是否属于汉语词汇系统的")
res = res.detach().numpy()
res2 = res2.detach().numpy()
res3 = res3.detach().numpy()
res4 = res4.detach().numpy()

r1 = cosine_similarity(res, res2)
r2 = cosine_similarity(res, res3)
r3 = cosine_similarity(res, res4)
print(r1**5)
print(r2**5)
print(r3**5)

