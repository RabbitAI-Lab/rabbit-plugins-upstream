# HTTP 请求与任务轮询

根地址：`${AI_SKILLS_API_URL:-https://ai-skills.open-idea.net/api/v1}`。

## 生成设计方案

```sh
BASE="${AI_SKILLS_API_URL:-https://ai-skills.open-idea.net/api/v1}"
curl -sS -X POST "$BASE/ui-ux-design/design.plan" \
  -H "Authorization: Bearer $UI_UX_DESIGN_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: 生成一个新的UUID" \
  --data '{"platform":"flutter","product_name":"家庭记账","product_type":"productivity","primary_goal":"快速记账并查看月度预算","visual_style":"friendly","brand_color":"#1677FF"}'
```

`platform` 支持 `web`、`flutter`、`react_native`、`ios`、`android`、`mini_program`。`product_type` 支持 `business`、`commerce`、`content`、`social`、`productivity`、`other`。

结果中的 `plan` 包含平台约束、信息架构、设计系统、必备状态、交互规则和验收清单。

## 获取验收清单

```sh
curl -sS -X POST "$BASE/ui-ux-design/design.checklist" \
  -H "Authorization: Bearer $UI_UX_DESIGN_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: 生成另一个新的UUID" \
  --data '{"platform":"web","focus":"accessibility"}'
```

`focus` 支持 `complete`、`accessibility`、`responsive`、`interaction`。

同步成功时直接返回 `status: "succeeded"`。如果返回排队状态，使用原 operation 和 `task_id` 查询：

```text
GET /api/v1/ui-ux-design/design.plan/tasks/{task_id}
GET /api/v1/ui-ux-design/design.checklist/tasks/{task_id}
```

查询请求继续携带 `Authorization: Bearer`。同一业务重试复用原 `Idempotency-Key`；新任务必须生成新值。
