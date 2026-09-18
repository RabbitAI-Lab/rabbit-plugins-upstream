# 接口速查

环境里没有 Python 时直接用这些。有 Python 的话优先用 `scripts/patentmax_client.py`——临时 id、字段名归一、任务轮询它都处理好了。

**Base URL** `https://api.ip930.com`
**认证** 所有接口都要 `Authorization: Bearer <API_KEY>`

---

## 一个必须先懂的机制：临时 id

`/api/search` 返回的每条结果里有个 `id`，这是**临时标识，60 分钟过期**。

详情类接口（detail / claims / fulltext / legal / citation / similar）**只认这个 id，不认公开号**。

所以想查某件专利的详情，必须先用公开号跑一次检索拿到 id：

```bash
# 1. 用公开号检索，从结果里取 id
curl -s -H "Authorization: Bearer $PATENTMAX_API_KEY" \
  "https://api.ip930.com/api/search?q=CN109761224A&ds=all&size=10"

# 2. 用拿到的 id 查详情
curl -s -H "Authorization: Bearer $PATENTMAX_API_KEY" \
  "https://api.ip930.com/api/detail?id=<上一步的 id>"
```

字段名不统一：公开号可能叫 `documentNumber`、`publicationNumber` 或 `pn`；临时 id 可能叫 `id` 或 `temporaryId`。取值时按候选名依次试。

结果列表也有好几种叫法：`patents` / `list` / `data` / `records`。

---

## 检索

### GET /api/search — 全球专利检索

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `q` | 是 | 检索式，支持 `AND` / `OR` / `NOT` 和括号，最长 4000 字符 |
| `ds` | 否 | `all` 全球（默认）、`cn` 仅中国 |
| `page` | 否 | 1–100，默认 1 |
| `size` | 否 | 1–50，默认 20 |

```bash
curl -s -H "Authorization: Bearer $PATENTMAX_API_KEY" \
  --data-urlencode 'q=(固态电池 OR 全固态电池) AND 电解质' \
  --data-urlencode 'ds=all' --data-urlencode 'size=20' \
  -G "https://api.ip930.com/api/search"
```

> 检索式里有中文和括号，一定用 `--data-urlencode -G`，别手工拼 URL。

**¥0.10 / 次**

### 详情类

以下都是 `GET`，都只接受一个 `id` 参数（临时 id，不是公开号）：

| 接口 | 返回 | 单价 |
| --- | --- | --- |
| `/api/detail` | 著录项目：标题、申请人、发明人、申请日、公开日、IPC、法律状态 | ¥0.10 |
| `/api/claims` | 权利要求书 | ¥0.20 |
| `/api/fulltext` | 说明书全文（很长） | ¥0.20 |
| `/api/legal` | 法律事件流水 | ¥0.10 |
| `/api/citation` | 引用与被引用，含非专利文献 | ¥0.10 |
| `/api/similar` | 语义相似专利 | ¥0.10 |

```bash
curl -s -H "Authorization: Bearer $PATENTMAX_API_KEY" \
  "https://api.ip930.com/api/claims?id=<temporary_id>"
```

---

## 健康检查

```bash
curl -s "https://api.ip930.com/api/v1/health"
```

**不需要密钥**，用来确认网络通不通。

---

## 状态码

| 码 | 含义 | 怎么办 |
| --- | --- | --- |
| 400 | 参数有问题 | 检查必填项和取值范围 |
| 401 | 密钥无效或已撤销 | 确认密钥完整、`Bearer ` 前缀没漏 |
| 402 | 余额不足 | 去控制台充值 |
| 403 | 该密钥无此接口权限 | 换密钥或联系支持 |
| 404 | 资源不存在 | 查详情时多半是临时 id 过期，重新检索 |
| 409 | 任务冲突 | 多半是重复提交，用同一个 Idempotency-Key 重试是安全的 |
| 429 | 限流 | 沙箱密钥每天 30 次；生产密钥稍后重试 |

调用失败不扣费。

---

## 两种密钥

| 前缀 | 行为 |
| --- | --- |
| `pm_live_` | 生产密钥，真实数据，从余额按次扣费。**正常使用都用这个** |
| `pm_test_` | 沙箱密钥，检索类每天 30 次，报告类任务返回模拟结果 |

沙箱密钥用于开发阶段验证参数与响应结构，跑不出真实检索结果。

新账户送的是**真实余额**，够跑 500 次检索，直接用生产密钥即可。
