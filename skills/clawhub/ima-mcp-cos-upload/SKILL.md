---
name: ima-mcp-cos-upload
description: "WorkBuddy ima-mcp 知识库入库的 COS 直传方案：create_media → HMAC-SHA1 签名 → curl PUT → add_knowledge。含两处致命签名坑（尾随\\n、header 值 safe=''）与'委托子代理避免 token 损坏'稳路。触发：ima 推库/上传 md/pdf/ppt 到知识库报 COS 403。"
version: 1.0.0
homepage: "https://ima.qq.com"
display_name: "ima 知识库 COS 直传"
description_zh: "ima-mcp 入库的 COS 签名上传方案与避坑清单"
description_en: "COS direct-upload recipe for ima-mcp knowledge-base ingestion"
agent_created: true
visibility: "user"
author: dzz-777
triggers: [ima 上传报错, COS 403, 知识库入库, ima 推库, ima-mcp 上传, 上传到 ima 知识库]
tags: [ima, 知识库, COS, 上传, 签名, 避坑, mcp]
---

# ima-mcp 知识库 COS 直传方案

本 skill 解决 **WorkBuddy 的 `mcp__ima-mcp__create_media` → 手动 COS PUT → `add_knowledge`** 入库链路中反复出现的 **COS 403** 问题。与 `ima-skills`（OpenAPI `ima_api.cjs`）是不同路径——本链路用 MCP 服务器下发的临时 COS 凭证，需自己算 HMAC-SHA1 签名并 PUT。

## 何时用
- 用 ima-mcp 把本地 `.md` / `.pdf` / `.pptx` 等推入「你的 ima 知识库（共享库或个人库均可）」。
- 现象：`curl` 返 `403 Forbidden`（XML 报错 `AccessDenied` / `SignatureDoesNotMatch`）。

## 链路全景
1. `create_media(file_name, file_size, content_type, file_ext, knowledge_base_id)` → 返回 `cos_credential`（含 `SecretId`/`SecretKey`/`Token`/`Key`、桶 host）。
2. 用凭证把文件 `PUT` 到 COS（自己算签名）。
3. `add_knowledge(media_id, folder_id?)` 入库（media_id 来自 create_media）。

> 重名策略用 SAVE，新版本带 `v1.x` 不撞名。**ima-mcp 无法删除/移动/改标签/建夹**——旧版清理须用户在 ima 界面手动。

## ⛔ 两处致命签名坑（缺一则 403）
来自 2026-08-13 实战，已验证：

**坑 A — HttpString 必须尾随 `\n`**
```
HttpString = "{method}\n{http_uri}\n\n{http_headers}\n"   # 末项后还要一个 \n
```
缺最后的 `\n` → COS 403。这是最容易漏的一点。

**坑 B — Header 值必须用 `safe=''` 编码（`/`→`%2F`）**
- `http_uri`（对象 Key 路径）：`urllib.parse.quote(key, safe='/')` —— **保留** `/`。
- `http_headers` 的每个 value：`urllib.parse.quote(v, safe='')` —— **编码** `/`。
二者编码规则不同，别混。

**坑 C — `cos_key` 不含前导 `/`，签名 `http_uri` 必须手动补 `/`**
- `create_media` 返回的 `cos_key` **不带前导 `/`**（如 `5/fGpy...md`）。
- 但 COS 服务端验签的 `FormatString` 里 `http_uri` **带前导 `/`**（如 `/5/fGpy...md`）。
- 若签名用 `5/fGpy...md`（无 `/`）→ COS 返 `403 SignatureDoesNotMatch`，响应体 XML 可定位根因。
- ✅ 修复：`http_uri = "/" + urllib.parse.quote(cos_key, safe='/')`，即先补 `/` 再编码。
- 来自 2026-08-27 实战：4 本投资书首传全 403，抓响应体定位根因修复后重传全 200。

## 签名算法（Python 参考实现）
```python
import hmac, hashlib, time, urllib.parse

def build_cos_auth(secret_id, secret_key, token, method, cos_key, content_type,
                   host="ima-share-kb-1258344701.cos.ap-shanghai.myqcloud.com"):
    method = method.lower()
    http_uri = "/" + urllib.parse.quote(cos_key, safe='/')   # 坑C: cos_key 无前导/，签名必须补；坑B: 保留 '/'
    headers = {
        "content-type": content_type,
        "host": host,
        "x-cos-security-token": token,
    }
    http_headers = "&".join(                                  # 坑B: value safe=''
        f"{k}={urllib.parse.quote(v, safe='')}" for k, v in sorted(headers.items())
    )
    now = int(time.time()); expire = 600
    key_time = f"{now};{now+expire}"
    sign_key = hmac.new(secret_key.encode(), key_time.encode(), hashlib.sha1).hexdigest()
    http_string = f"{method}\n{http_uri}\n\n{http_headers}\n"  # 坑A: 尾随 \n
    string_to_sign = f"sha1\n{key_time}\n{hashlib.sha1(http_string.encode()).hexdigest()}\n"
    signature = hmac.new(sign_key.encode(), string_to_sign.encode(), hashlib.sha1).hexdigest()
    header_list = ";".join(sorted(headers.keys()))
    auth = (f"q-sign-algorithm=sha1&q-ak={secret_id}&q-sign-time={key_time}"
            f"&q-key-time={key_time}&q-header-list={header_list}"
            f"&q-url-param-list=&q-signature={signature}")
    return auth, headers

# 用法：
# auth, headers = build_cos_auth(cred["SecretId"], cred["SecretKey"], cred["Token"],
#                                "put", cred["Key"], "text/markdown")
# curl --noproxy '*' -X PUT -T file \
#   -H "Authorization: $auth" \
#   -H "x-cos-security-token: $token" \
#   -H "Content-Type: text/markdown" \
#   "https://{host}/{cos_key}"
```

## ⛔ 网络约束（沙箱，2026-08-13 厘清）
- 后台 Bash **无 DNS**（rc=6）→ 上传必须**前台**执行。
- 前台 `--resolve` 钉死 IP 反不可达（rc=60）→ **不能用 --resolve**。
- 用 `curl --noproxy '*' -X PUT -T file`（带鉴权头，无代理、无 --resolve），curl 自走系统 DNS。
- HTTP 正向转发对长签名头硬性 502 → 只用 HTTPS。
- 域名用直达 `ima-share-kb-1258344701.cos.ap-shanghai.myqcloud.com`，**非** custom_domain CDN（会被 Lego Server 拒 403）。

## ✅ 稳路：整链委托 Agent 子代理（强烈推荐）
**主会话手动把 create_media 返回的 token 抄进凭证 JSON 极易损坏（长字符串复制错位）→ 必 403。** 已验证解法：把 `create_media → 签名 → COS PUT → add_knowledge` **整套交给一个 `general-purpose` Agent 子代理**在它自己的上下文里跑，主会话不手动传 token。子代理首试即 HTTP 200。

> 调用 Agent 时把文件路径、folder_id、knowledge_base_id、content_type 写清楚，让它独立读 create_media 响应、算签名、上传、注册，最后回报 media_id 与 HTTP 状态。

> ⚠️ 实测：子代理偶发不可用（报 `Tool Agent not found`）。此时退回主会话自跑脚本同样可行——把整段 Python（含 `build_cos_auth`）写进一个 `.py` 文件，主会话直接 `python script.py` 跑 `create_media→签名→curl PUT→add_knowledge`，token 不手动跨消息复制即不损坏。已验证 2026-08-27 用此路 4 本投资书全 200。

## ⛔ 坑 D — 重试上传必须先查重，否则产生大量重复条目（2026-08-27 实战教训）
- **现象**：同一批书因 COS 403 修正后重试，每轮都执行了完整 `create_media→PUT→add_knowledge`，导致 4 本书各入 3 份（12 条），其中 8 条为带时间戳后缀的垃圾副本。
- **根因**：脚本缺少「幂等/去重」检查——重试前未查 KB 是否已有同名标题。
- **ima 的重名行为**：`add_knowledge` 提交同名标题时，ima 自动追加 `_YYMMDDHHmmss` 后缀（防覆盖机制）。这本身合理，但我们的场景不应触发。
- ✅ **强制规则**：批量上传前**必须先调 `get_knowledge_list`**，逐本核对目标标题是否已存在：
  - 已存在且 `parse_progress=100` → **跳过**，不入
  - 已存在但 `parse=0` 或 `media_state=1` → **等**或通知用户，不重复提交
  - 不存在 → 正常走 `create_media→PUT→add_knowledge`
- 批量脚本的伪代码逻辑：
  ```
  existing = get_knowledge_list(kb_id, limit=50)
  existing_titles = {item["title"] for item in existing["knowledge_list"]}
  for book in books:
      if book.title in existing_titles:
          print(f"⚠️ 跳过（已存在）: {book.title}")
          continue
      # 正常上传流程...
  ```

## 偶发坏 media_id（invalid media_type 220001）
`create_media` 偶发下发坏 media_id，`add_knowledge` 必报且重试无效 → **重 `create_media` 换 fresh media_id + COS 重传一次**即解。

## 验证清单（每次上传后）
- `get_knowledge_list` 实时核对库 `knowledge_total_size` 与目标夹 `total_size`（库项/每夹精确计数以 ima 实时为准，文档写死数字勿信）。
- 确认 `parse_progress=100`、目标文件在列。
- 临时凭证文件（含 token）上传后立即删，避免密钥残留。

## ⛔ 坑 E — REPLACE 必须精确匹配库内旧项【完整标题】（含下划线/`.md` 后缀）
- **现象（2026-09-02 实战）**：库内旧项标题为「区别方法论方法卡手册_v1.3.md」（带下划线+`.md`），而 `create_media` 用了「区别方法论方法卡手册 v1.3」（无下划线、无后缀）→ `DUPLICATE_NAME_STRATEGY_REPLACE` 按标题精确匹配未命中 → 变成新增副本，KB 总数 +1（从 77 变 78）。
- **根因**：ima 的重名匹配是【精确字符串相等】，不忽略空格/下划线/`.md`/大小写差异。推测旧标题必然踩坑。
- ✅ **强制规则**：REPLACE 覆盖前，**先 `get_knowledge_list` 取目标项真实 `title` 全文**，`create_media` 的 `file_name` 必须与之【逐字符一致】（含 `_`、`.md`、空格）。不要凭记忆/推测旧标题。
- **若已误建副本**：ima OpenAPI/MCP 无 delete 接口 → 只能用户在 ima 界面手动删多余项；正确的那一份用精确标题二次 `create_media`+`add_knowledge(REPLACE)` 即可覆盖，库计数回正。

## ⛔ 坑 F — 偶发坏凭证（InvalidAccessKeyId）需重取 create_media（2026-09-04 / 08-31 实战）
- **现象**：某次 `create_media` 返回的 `secret_id` 含连字符 `-`（形如 `AKID-051xna3...` 或中段 `-` 如 `AKID...x_M__-qizG...` / `AKIDG-uqBd3`），用其算签名 PUT → COS 返 `403 InvalidAccessKeyId`（"The Access Key Id you provided does not exist in our records"）。
- **根因**：`create_media` 偶发下发损坏的临时密钥——与「偶发坏 media_id」同源，皆 MCP 服务端偶发异常，非签名算法错。
- ✅ **强制规则（实测强化版）**：每次 `create_media` 后，**先肉眼核对 `secret_id`**：
  - 正常凭据：`AKID` 紧跟随机字符、**全串只含字母数字、可含 `_`、绝不含 `-`**（形如 `AKIDt7Oelr...` / `AKIDluyrGpLLVE6...`）。
  - 坏凭据：**含任意 `-` 即坏**——不止 `AKID` 后紧跟 `-`，**中段 `-` 也实测 100% 触发 403**（连续 11 次带 `-` 的凭据 PUT 全 403）。`_` 合法，仅 `-` 是坏信号。
  - 若含 `-` → **直接重调 `create_media` 换 fresh 凭证**，不要硬凑签名。
- ⚠️ **重试次数可能很多**：单个文件曾连续 8~12 次返回带 `-` 的坏凭据才出现干净凭据（非「重取一次即恢复」）。**循环重调直到拿到无 `-` 的全字母数字凭据为止**，拿到即用，绝不硬编码坏签名。
- 与坑 E 区分：坑 E 是「标题匹配错」→ 副本；坑 F 是「凭证本身坏」→ 403。二者独立，可同时发生。

## ⛔ 坑 G — sign_key 必须用 `.hexdigest()`（十六进制字符串），误用 `.digest()` 原始字节必 403（2026-09-10 实战）
- **现象**：上传脚本自写签名逻辑，`sign_key = hmac.new(secret_key, key_time, sha1).digest()`（原始字节）再 `.encode()` 当下一轮 HMAC 的 key → COS 返 `403 SignatureDoesNotMatch`。`secret_id` 无 `-`（坑 F 已排除），http_string 与服务器 `StringToSign` 完全一致，唯签名值错。
- **根因**：COS 的 `sign_key` 约定是 HMAC-SHA1 的**十六进制摘要字符串**（`hexdigest()`），不是原始字节（`digest()`）。用 `digest()` 字节当 key 重算的 signature 与服务器期望不符。
- ✅ **强制规则**：
  - `sign_key = hmac.new(secret_key.encode(), key_time.encode(), hashlib.sha1).hexdigest()`（**`.hexdigest()`，非 `.digest()`**）。
  - 签名头列表（`q-header-list`）必须含**实际参与签名的全部 header**，本库稳定集 = `content-type;host;x-cos-security-token`（按字母序排序）。少签/多签任一即 403。
  - **今后补卡上传，直接逐字复制本 skill 的 `build_cos_auth` 模板（line 56-75），不要凭记忆自写签名函数**——模板已含 `.hexdigest()` + 三签名头，跑通多次。已验证参考：`/tmp/up_card_p1.py`、`/tmp/up_card_p2.py`（同构，仅换凭据/cos_key/file）。
