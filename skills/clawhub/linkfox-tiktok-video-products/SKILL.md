---
name: linkfox-tiktok-video-products
description: TikTok 视频号可带货商品查询技能，经 /tiktokVideo/developerProxy 调用达人店铺商品搜索与橱窗/直播袋商品列表（Get Shop Products、Get Showcase Products）。依赖 linkfox-tiktok-video-auth 取得 ttsAccessToken。当用户提到 TikTok 达人店铺商品、搜索店铺商品、Get Shop Products、达人橱窗商品、showcase 商品、Get Showcase Products、可带货商品、视频挂车选品、可购物视频选品、查询达人可推广商品、TikTok 视频号商品列表 时触发。返回的 product_id 供 linkfox-tiktok-video 预检/发布可购物视频使用。**不含授权**（授权用 linkfox-tiktok-video-auth）；**不含视频上传/发布**（用 linkfox-tiktok-video）。
---

# TikTok 视频号可带货商品查询

本 skill 负责 TikTok **视频上传模块**下的**商品选品**能力：搜索达人绑定店铺商品、查询达人橱窗/直播袋商品，取得 `product_id` 供后续可购物视频挂车使用。

> 📌 **前置依赖**：`linkfox-tiktok-video-auth` — 达人授权与 `accessToken`（作为 `ttsAccessToken`）。

> 📌 **下游用途**：返回商品中的 **`product_id`** 用于 **`linkfox-tiktok-video`** 的 `precheck_shoppable_video`（预检）与 `post_shoppable_video`（发布）接口中的 `product_link_info.product_id`。

## Prerequisites（必须先读）

1. 运行 `python scripts/check_auth_dependency.py`；exit code **42** → 先安装 **`linkfox-tiktok-video-auth`** 并完成达人授权。
2. **不要**在本 skill 内实现授权/令牌刷新逻辑（回到 auth skill）。

## Core Concepts

- **调用链路**：`accountTokens`（或用户传入 `ttsAccessToken`）→ `developerProxy` → 紫鸟 `tiktok-proxy/creator` → TikTok Open API
- **两类商品来源**：
  - **店铺商品**（`get_shop_products`）：搜索达人绑定店铺中的商品，支持关键词与排序
  - **橱窗/直播袋**（`get_showcase_products`）：列出达人橱窗或直播间带货袋中的商品
- **`product_id` 用途**：预检/发布可购物视频时作为 `product_link_info.product_id`，由 **`linkfox-tiktok-video`** skill 消费

## API Usage

详见 `references/api.md`（含 developerProxy 入参/出参、查询参数枚举、分页与错误码）。

### Available Scripts

| 脚本 | 作用 |
|------|------|
| `check_auth_dependency.py` | 检测是否已安装 `linkfox-tiktok-video-auth` |
| `products_api.py` | **具名 API 入口**：JSON 含 `api` 字段 |
| `get_shop_products.py` | 搜索达人绑定店铺商品（`affiliate_creator/202509/shop_products`） |
| `get_showcase_products.py` | 达人橱窗/直播袋商品（`affiliate_creator/202405/showcases/products`） |

共享模块：`_tiktok_video_products_common.py`、`_products_endpoints.py`、`_products_api_runner.py`。

## 标准前置流程（选号 → 取令牌 → 查商品）

1. **`linkfox-tiktok-video-auth`**：`authorized_accounts.py` 列出已授权视频号 → 用户选定 `openId`
2. 取令牌：传 `openId`（runner 自动调 `/tiktokVideo/accountTokens`）
3. 查商品：`get_shop_products.py` 或 `get_showcase_products.py`
4. 从返回结果中提取 **`product_id`**，供 `linkfox-tiktok-video` 预检/发布使用

## Usage Scenarios

### Scenario 1: 搜索达人绑定店铺商品

按标题关键词搜索达人店铺中的可带货商品：

```bash
python scripts/get_shop_products.py '{"openId": "...", "title_keyword": "apple", "page_size": 20}'
```

或：

```bash
python scripts/products_api.py '{"api": "get_shop_products", "openId": "...", "page_size": 20}'
```

从返回商品列表中取 **`product_id`**，用于 `linkfox-tiktok-video` 的预检/发布。

### Scenario 2: 查询达人橱窗/直播袋商品

```bash
# 橱窗商品（默认 origin=SHOWCASE）
python scripts/get_showcase_products.py '{"openId": "...", "page_size": 20}'

# 直播间带货袋
python scripts/get_showcase_products.py '{"openId": "...", "page_size": 20, "origin": "LIVE"}'
```

### Scenario 3: 翻页拉取更多商品

首次请求不传 `page_token`；若响应含 `data.next_page_token`，将其作为下一次请求的 `page_token` 继续拉取。详见 `references/api.md`。

## Display Rules

1. **只呈现数据**：展示接口返回字段，不做主观选品建议。
2. **令牌安全**：不输出完整 `ttsAccessToken`。
3. **明确 product_id**：用户需要挂车发布时，从商品列表中提取并展示 `product_id`。
4. **无授权时**：引导用户先走 `linkfox-tiktok-video-auth`。

## Important Limitations

- **模块隔离**：仅 `/tiktokVideo/developerProxy`；不可用于 `/tiktokShop/*`。
- **不含视频能力**：上传、预检、发布视频请使用 **`linkfox-tiktok-video`**。
- **列表较大时**：使用 `response_io.py` 落盘提取字段，避免上下文溢出。

## Not Applicable

| 场景 | 应使用的 skill |
|------|----------------|
| 达人/视频号 **授权**、刷新令牌 | `linkfox-tiktok-video-auth` |
| 视频 **上传 / 预检 / 发布 / 查状态** | `linkfox-tiktok-video` |
| TikTok Shop **小店** ERP 商品 | `linkfox-tiktok-auth` + 对应业务 skill |
| TikTok 选品 / 数据分析（非达人自有商品） | EchoTik 等 |

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
