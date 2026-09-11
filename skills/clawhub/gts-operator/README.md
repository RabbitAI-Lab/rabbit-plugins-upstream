# gts-operator（AI 原生对话式操作员 · 动态发现版）

让 AI Agent 以纯对话方式完成 GTS 多租户平台的全部操作：
**注册租户/管理员 → 维护组织架构与人员 → 配置表单与工作流 → 发起单据 → 流程审批
→ 表单复用与模板共享（复制/导出/导入/发布到市场/一键安装）**，
全部通过调用系统真实 HTTP API 完成，不写业务代码、不改库。

## 动态发现模式（v2）
Skill 不再内置端点表。Agent 每次会话先拉取系统自带的机器可读契约，再按契约执行：

- `GET /discovery/routes` — 从 Router 注册表**动态导出**全部端点（method/path/参数），后端增删路由自动反映，零维护。
- `GET /discovery/contract` — 配置域契约：12 种字段类型白名单与附加属性、流程节点属性/审批人规则/condition、biz_data 状态机与 data_json/subforms 组装规则、审批 action 枚举、字典用法、**模板包（gts-template）结构与市场语义**。

后端演进（新增字段类型/端点/状态）只需更新契约源，Skill 无需手改。

## 系统侧新增（v2.0.0 / v2.1.0 / v2.1.1 模板能力）
- `controllers/TemplateController.php`（新）：
  - v2.0.0 **模板包**：`GET /templates/export`、`POST /templates/inspect`、`POST /templates/import`
    —— 脱敏（无 tenant_id/user id/内部 id），引用按 code 重映射（`ref_form_code`/`subform_form_code`），
    用户型审批人降级为 placeholder，缺依赖入 warnings 不阻断，导入单事务。
  - v2.1.0 **共享市场**：`POST /templates/publish`、`GET /templates/market`、
    `GET /templates/market/{id}/preview`、`POST /templates/market/{id}/install`、
    `DELETE /templates/market/{id}` —— 无审核公共目录，任一租户 admin 可发布、
    发布者可下架（非属主 404）；`template_market` 表（软删除）。
  - v2.1.1 **子表自动包含**：`buildPackage()` 递归拉入被引用子表（含多层嵌套），
    因此分享/导出/发布**只需传主表 id**，明细表随包自动带上。
- 端点重构：`export/inspect/import` 与市场发布/安装共用 `buildPackage()` /
  `installPackage()` / `inspectPackage()` 三个核心，市场安装与文件导入行为不会分叉。
- `/discovery/contract` 新增 `templates` 域（含 `market` 子段）。
- `POST /forms/{id}/clone`（v1.9.0）：同租户复制表单（可选连带复制审批流）。

## 系统侧新增（v1.4.0 发现层）
- `core/Router.php`：公开 `Router::routes()` 导出注册表。
- `controllers/DiscoveryController.php`（新）：两个只读公开端点。
- `api.php`：注册两条 discovery 路由。

## 系统侧新增（v1.8.0 OAuth 设备授权）
- `controllers/OauthController.php`（新）：`/oauth/device`（Agent 发起）、`/oauth/status`（Agent 轮询）、`/oauth/approve`（授权页登录后确认）、`/oauth/me`（验证 token）、`/oauth/revoke`。
- `oauth_sessions` 表 + 30 天 token（`config/app.php` `oauth_token_expiry`）。
- 前端 `OauthAuthorize.jsx`（`#/oauth/authorize?user_code=XXX` 授权页，复用平台账号登录）。
- `/discovery/contract` `api` 域新增 `oauth_device_flow` / `token_lifetime` 说明。

## 使用（对最终用户）
- **API 地址已内置**（`https://www.geeyo.com/s/gts/api.php`），用户**无需提供地址**。
- **认证方式**：
  - **① OAuth 设备授权（推荐，v1.8.0 起）**：AI Agent 会引导你在浏览器打开授权链接并登录你的平台账号确认。授权一次 **30 天有效**，跨对话免重复登录，无需把密码告诉 Agent。凭证由 Agent 持久化在本机 `~/.gts-operator.json`。
  - **② 账号密码（临时）**：直接提供手机号+密码+租户 slug（或让 Agent `POST /auth/register` 开新租户）。
- 例："帮我在 geeyo 搭一个设备申购流程，1 万以下自动过、以上 Ken 审批"——Agent 会先完成 OAuth 认证（若无有效授权），再自动执行全部 API 调用。
- 授权页会显示请求方与有效期；中途可对 Agent 说"撤销授权"立即生效。

## 已验证（2026-09）
- discovery 输出正确：67 端点自动列出、contract 8 域（含 `templates`）字段类型/状态机/action/模板语义与代码一致。
- 动态发现 + 全链路 E2E（注册租户→组织→表单→流程→发起→审批含条件分支）此前已实测通过。
- AI Agent 验收：对话式搭"设备申购"（坏 schema→400→Agent 自愈）+ 双条件发起 + 审批 + 审计留痕全通过（v1.5.0）。
- OAuth UX（v1.8.1）：授权页展示请求方 client_label、授权码状态引导、租户 slug 化标识、成功摘要与撤销提示。
- 模板能力（v2.0.0–v2.1.1）：导出/导入脱敏包 + 引用 code 重映射（冒烟 21/21）；共享市场发布/浏览/预览/安装/下架 + 跨租户隔离（冒烟 11/11）；**子表自动包含**（单元 8/8、端到端 11/11：只传主表 id 即产出含子表的完整包，安装后子表引用正确重绑）。

## 已知边界
- 注册接口当前完全开放（无邀请码）；如担心滥用可加"注册邀请码/人工审批"。
- 表单 schema / 流程 nodes 已由服务端校验（v1.5.0）：非法配置返回 400 + 精确定位，Agent 据此自愈；契约字段枚举见 `/discovery/contract`。
- `/discovery/contract` 的枚举（字段类型/状态/action/模板语义）由 DiscoveryController 维护，引擎变更时需同步该文件。
- **模板市场无审核**：公共目录，任一租户管理员可发布；发布者只能下架自己的条目，无平台级全局管理员（治理能力见 BACKLOG）。
- **子表公式不参与计算**：`SubFormEditor` 仅渲染 schema，子表内的 `formula` 字段不会自动算（主表字段正常）。
