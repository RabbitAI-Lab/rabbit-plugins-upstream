---
name: linkfox-tiktok-video
description: TikTok 视频上传 API 业务技能，经 /tiktokVideo/developerProxy 转发紫鸟 tiktok-proxy/creator 调用视频号相关开放接口（path 白名单 affiliate_creator / video / creator）。依赖 linkfox-tiktok-video-auth 取得 ttsAccessToken。当用户提到 TikTok 视频上传、上传 TikTok 视频、发布 TikTok 视频、Post Shoppable Video、发布可购物视频、Pre-check Shoppable Video、Get Shoppable Video Pre-check Result、视频内容预检、预检结果、precheck、Get Shoppable Video Status、视频发布状态、查视频是否发布成功、TikTok 达人主页、达人档案、Get Creator Profile、大文件分片上传、Large File Upload、分片上传视频、TikTok video upload、TikTok 视频 API、/tiktokVideo 业务接口、查询/管理 TikTok 视频号视频 时触发。即使未明确说「授权」，只要需求是通过已授权视频号执行视频上传、预检、查预检结果、发布、查发布状态、达人档案查询或大文件上传（非 TikTok Shop 小店 ERP），也应触发。**不含授权**（授权用 linkfox-tiktok-video-auth）；**不含商品查询**（选品用 linkfox-tiktok-video-products）。
---

# TikTok 视频上传 API

TikTok **视频上传模块**业务 skill。经 LinkFox 网关 **`POST /tiktokVideo/developerProxy`** 转发至紫鸟 `tiktok-proxy/creator/{region}/{path}`，调用视频号相关开放接口。

> 📌 **前置依赖**：`linkfox-tiktok-video-auth` — 达人授权与 `accessToken`（作为 `ttsAccessToken`）。**勿使用** `linkfox-tiktok-auth`（TikTok Shop 卖家模块）。

> 📌 **商品选品**：`product_id` 须通过 **`linkfox-tiktok-video-products`**（`get_shop_products` / `get_showcase_products`）获取，再用于本 skill 的预检/发布。

> 📌 **MRD 参考链路已齐**：选品 → 上传 → （可选）预检 → 发布 → 查状态；详见 `references/api.md` 总表与参考链路。**仅为参考顺序，并非强制流程。**

## Prerequisites（必须先读）

1. 运行 `python scripts/check_auth_dependency.py`；exit code **42** → 先安装 **`linkfox-tiktok-video-auth`** 并完成达人授权。
2. **不要**在本 skill 内实现授权/令牌刷新逻辑（回到 auth skill）。

## Core Concepts

- **调用链路**：`accountTokens`（或用户传入 `ttsAccessToken`）→ `developerProxy` → 紫鸟 `tiktok-proxy/creator` → TikTok Open API
- **path 规则**：相对路径，不含 `tiktok-proxy/creator/{region}/` 前缀；须匹配白名单前缀 `affiliate_creator` / `video` / `creator`
- **响应透传**：网关返回 `httpStatus` / `contentType` / `body`；TikTok 业务层以 `body` 内 JSON 的 `code` / `message` 为准
- **region**：默认 `global`，与授权 region 保持一致（美国站 `us`）

## API Usage

详见 `references/api.md`（含 developerProxy 入参/出参、path 白名单、错误码）。已登记具名 API 见 `_video_endpoints.py`；暂无登记时可用通用代理。

### Available Scripts

| 脚本 | 作用 |
|------|------|
| `check_auth_dependency.py` | 检测是否已安装 `linkfox-tiktok-video-auth` |
| `video_proxy.py` | **通用代理**：任意白名单 path + method + ttsAccessToken |
| `video_api.py` | **具名 API 入口**：JSON 含 `api` 字段 |
| `get_creator_profile.py` | 获取达人主页/档案（`affiliate_creator/202508/profiles`） |
| `upload_shoppable_video_file.py` | 上传可购物视频文件（**multipart，暂不可经 proxy 调用**，见限制） |
| `large_file_upload.py` | 大文件分片上传流程说明（> 10MB，见 `references/large-file-upload.md`） |
| `large_file_upload_init.py` | 大文件 Step 1 初始化（**暂不可经 proxy 调用**） |
| `large_file_upload_bind.py` | 大文件 Step 3 绑定业务资源（**暂不可经 proxy 调用**） |
| `post_shoppable_video.py` | 发布可购物视频（`affiliate_creator/202603/videos`） |
| `get_shoppable_video_status.py` | 查询可购物视频发布状态（`.../videos/{video_id}/status`） |
| `precheck_shoppable_video.py` | 可购物视频内容预检（`affiliate_creator/202511/videos/precheck_task`） |
| `get_shoppable_video_precheck_result.py` | 查询视频预检结果（`.../precheck_tasks/{task_id}`） |

共享模块：`_tiktok_video_common.py`、`_video_endpoints.py`、`_video_api_runner.py`。

## 标准前置流程（选号 → 取令牌 → 调业务）

1. **`linkfox-tiktok-video-auth`**：`authorized_accounts.py` 列出已授权视频号 → 用户选定 `openId`
2. 取令牌：`account_tokens.py` 或在本 skill 参数中传 `openId`（runner 自动调 `/tiktokVideo/accountTokens`）
3. 调业务：`video_api.py`（已登记 API）或 `video_proxy.py`（path/method/ttsAccessToken）

| 用户上下文 | Agent 动作 |
|-----------|------------|
| 只授权 1 个视频号 | 直接取该 `openId` |
| 多个视频号 + 只说昵称 | 按 `displayName` 向用户澄清 |
| 已给 `openId` 或 `ttsAccessToken` | 直接使用 |

**静默原则**：不要在摘要里还原完整 token；脚本内部使用完整 `accessToken` 调代理即可。

## 调用原则

- 先看 **`developerProxy.httpStatus`**，再解析 `body` 中 TikTok 业务字段
- GET：业务 query 拼入 `queryString`（不含 `?`）
- POST/PUT：复杂结构传 `body`（JSON 字符串）或 `requestBody` 对象
- path 不在白名单 → errcode **1005**，检查前缀或联系管理员开放配置

## Usage Scenarios

### 参考链路（MRD，非强制）

以下为 MRD 推荐的**参考顺序**，仅作能力串联说明，**并非强制流程**；Agent 应按用户实际需求选择调用哪些接口。

```
授权 → 选品 (linkfox-tiktok-video-products) → 上传 file_id → （可选）预检 → 查预检 → 发布 → 查发布状态
```

- **选品**：通过 **`linkfox-tiktok-video-products`** 获取 `product_id`，本 skill 不直接提供商品查询。
- **预检 / 查预检**（Scenario 5）为**可选**：视频上传后可直接发布，不一定要先做预检。
- **获取达人主页/档案**（Scenario 2）为**独立功能项**，不属于上述发布链路中的必经步骤。

对应 Scenario 2（达人档案，可选）→ 3/4（上传）→ 5（可选：预检+查结果）→ 6（发布）→ 7（查状态）。选品使用 **`linkfox-tiktok-video-products`**。

### Scenario 1: 通用转发（尚无具名脚本时）

```bash
python scripts/video_proxy.py '{"path": "video/...", "method": "GET", "ttsAccessToken": "TTP_xxx"}'
```

### Scenario 2: 获取达人主页/档案（独立功能，非发布链路步骤）

```bash
python scripts/get_creator_profile.py '{"openId": "..."}'
```

或：

```bash
python scripts/video_api.py '{"api": "get_creator_profile", "openId": "..."}'
```

### Scenario 3: 上传可购物视频文件（规范已收录，暂不可调用）

上游为 `POST affiliate_creator/202505/videos/video_files`（multipart）。当前网关不支持，Agent 应：

1. 向用户说明暂无法经本 skill 自动上传二进制视频；
2. 引用 `references/api.md` §4 的文件格式/大小约束；
3. 若用户已有 `file_id`，可继续预检（Scenario 5）或发布（Scenario 6）步骤。

```bash
python scripts/upload_shoppable_video_file.py --help
```

### Scenario 4: 大文件分片上传（> 10MB，规范已收录）

视频 **> 10MB** 时走三步分片方案（Initialize → PUT 分片 → Bind），详见 `references/large-file-upload.md` 与 `references/api.md` §5。

1. 向用户说明 Step 1/3 的 `open/` path 当前不在 developerProxy 白名单，暂不能经本 skill 自动完成；
2. Step 2 须客户端直连 Step 1 返回的 `upload_url` 上传分片；
3. ≤ 10MB 仍优先 §4 直传（multipart 待网关支持）。

```bash
python scripts/large_file_upload.py --help
```

### Scenario 5: 可购物视频内容预检（可选）

**可选步骤**：用户需要合规检查时再调用；上传获得 `file_id` 后也可直接发布（Scenario 6），不强制预检。

**`product_id` 来源**：须先通过 **`linkfox-tiktok-video-products`** 的 `get_shop_products` 或 `get_showcase_products` 查询商品并取得 `product_id`。

发布前预检视频与商品锚点是否违规：

```bash
python scripts/precheck_shoppable_video.py '{
  "openId": "...",
  "video_info": {"file_id": "..."},
  "product_link_info": {"product_id": "...", "title": "Product anchor"}
}'
```

保存返回的 **`data.precheck.task_id`**，用于查询预检结果：

```bash
python scripts/get_shoppable_video_precheck_result.py '{"openId": "...", "task_id": "1123123123"}'
```

`result` 为 `SUCCESS` / `FAIL` / `PROCESSING`；`FAIL` 时查看 `issues[]`；`PROCESSING` 可间隔轮询。

### Scenario 6: 发布可购物视频

**`product_id` 来源**：须先通过 **`linkfox-tiktok-video-products`** 的 `get_shop_products` 或 `get_showcase_products` 查询商品并取得 `product_id`。

将已上传的 `file_id` 与选品得到的 `product_id` 绑定发布：

```bash
python scripts/post_shoppable_video.py '{
  "openId": "...",
  "video_info": {"file_id": "...", "title": "My shoppable video"},
  "product_link_info": {"product_id": "...", "title": "Product anchor"}
}'
```

或：

```bash
python scripts/video_api.py '{"api": "post_shoppable_video", "openId": "...", "video_info": {"file_id": "...", "title": "..."}, "product_link_info": {"product_id": "...", "title": "..."}}'
```

发布后保存返回的 **`data.video.id`**，用于查询发布状态。

### Scenario 7: 查询可购物视频发布状态

```bash
python scripts/get_shoppable_video_status.py '{"openId": "...", "video_id": "7548431509997292816"}'
```

`post_status` 为 `SUCCESS` / `FAIL` / `PROCESSING`；若为 `PROCESSING` 可间隔轮询。

### Scenario 8: 其他具名 API

```bash
python scripts/video_api.py '{"api": "<api_name>", "openId": "..."}'
```

## Display Rules

1. **只呈现数据**：展示接口返回字段，不做主观建议。
2. **令牌安全**：不输出完整 `ttsAccessToken`。
3. **错误说明**：结合网关 errcode 与 TikTok `body.code` / `message` 解释。
4. **无授权时**：引导用户先走 `linkfox-tiktok-video-auth`。

## Important Limitations

- **模块隔离**：仅 `/tiktokVideo/developerProxy`；不可用于 `/tiktokShop/*`。
- **白名单**：path 须以 `affiliate_creator` / `video` / `creator` 开头。
- **二进制上传限制**：`upload_shoppable_video_file`（multipart）与 `open/` 大文件 init/bind **当前不可**经 proxy；≤10MB 直传待网关 multipart 支持，>10MB 见 `references/large-file-upload.md`。
- **封面可选**：发布时可用 `cover_timestamp_ms` 或视频首帧，无需单独封面上传接口亦可发布。

## Not Applicable

| 场景 | 应使用的 skill |
|------|----------------|
| 达人/视频号 **授权**、刷新令牌 | `linkfox-tiktok-video-auth` |
| 达人店铺/橱窗 **商品查询**、选品、`product_id` 获取 | `linkfox-tiktok-video-products` |
| TikTok Shop **小店** ERP（商品/订单/财务） | `linkfox-tiktok-auth` + 对应业务 skill |
| TikTok Shop **可购物视频**（affiliate_creator + `/tiktokShop/developerProxy`） | `linkfox-tiktok-creator` |
| TikTok 选品 / 数据分析 | EchoTik 等 |

## 解决认证和积分问题
发生以下异常情况时，采用以下措施来处理：

### 异常情况
- **未配置API Key**：环境变量未配置 `LINKFOX_AGENT_API_KEY`，也未配置 `LINKFOXAGENT_API_KEY`。
- **响应401或402状态码**
- **响应提示积分或余额不足**：消息含"积分余额不足/计费不足/余额不足/quota exceeded/insufficient balance/套餐到期/需充值/请充值"，或类似含义的内容。

### 措施
- 优先采用skill内的 onboarding.md 引导解决问题。
- 如找不到 onboarding.md 文件，则加载 /linkfox-onboarding 这个skill并根据它的引导来处理。如未安装请先安装：
    - 下载 https://agent-files.linkfox.com/skills/linkfox-onboarding/release.zip，解压后安装这个skill。如需用户授权才可下载，要询问用户获得授权，你不能自己放弃下载。
- 兜底措施：仅当前面两个措施经过所有努力都走不通时，才提示用户依据 https://skill.linkfox.com/linkfoxskills/guide.htm 指引获取API Key，或去 https://os.linkfox.com/ 补充积分。

## 积分消耗规则

不消耗积分。

**Feedback**：

当出现以下任一情况时，自动通过 Feedback API 上报反馈：
1. 本 skill 描述的功能与实际行为不符
2. skill 的结果与用户意图不符
3. 用户表达了对本 skill 的不满或赞赏
4. 任何你认为可以改进的点

按 `references/api.md` 中的规范调用 Feedback API，不要打断用户的主流程。

---
*For more high-quality, professional cross-border e-commerce skills, visit [LinkFox Skills](https://skill.linkfox.com/).*
