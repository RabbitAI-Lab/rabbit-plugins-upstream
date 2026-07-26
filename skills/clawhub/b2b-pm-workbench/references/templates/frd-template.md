# B端产品功能需求文档（FRD）模板

> PRD的"技术翻译版"，开发团队可以直接据此编码

## 文档信息

| 字段 | 内容 |
|------|------|
| 文档名称 | [功能模块名称] FRD |
| 关联PRD | PRD-[xxx] V[X.X] |
| 版本 | V1.0 |
| 日期 | YYYY-MM-DD |
| 作者 | [姓名] |

---

## 1. 功能概述

[用一段话描述这个功能做什么，输入什么，输出什么]

### 前置依赖
- 需要哪些数据就绪？
- 需要哪些系统对接已完成？
- 依赖哪些基础设施就位？

---

## 2. 数据结构定义

### 2.1 涉及表清单

| 表名 | 说明 | 是否新增 | 预估数据量 |
|------|------|---------|-----------|
| `t_xxx` | [说明] | 新增/已有 | 日均X条 |

### 2.2 表结构定义

**表：[表名]**

| 字段名 | 类型 | 长度/精度 | 必填 | 默认值 | 唯一 | 索引 | 说明 |
|--------|------|----------|------|--------|------|------|------|
| id | bigint | - | 是 | auto | PK | - | 主键 |
| ... | | | | | | | |

### 2.3 索引设计

| 索引名 | 字段 | 类型 | 说明 |
|--------|------|------|------|
| idx_xxx | (col1, col2) | BTREE/UNIQUE | [查询场景] |

---

## 3. API接口定义

### 3.1 接口清单

| 序号 | 接口名 | Method | Path | 说明 |
|------|--------|--------|------|------|
| API-01 | 查询列表 | POST | /api/v1/xxx/list | 分页+搜索+筛选+排序 |
| API-02 | 查询详情 | GET | /api/v1/xxx/{id} | 含关联信息 |
| API-03 | 新增 | POST | /api/v1/xxx | |
| API-04 | 编辑 | PUT | /api/v1/xxx/{id} | |
| API-05 | 删除 | DELETE | /api/v1/xxx/{id} | 逻辑删除 |

### 3.2 接口详细定义

#### API-01: 查询列表

```
POST /api/v1/xxx/list
Content-Type: application/json
Authorization: Bearer {token}

Request Body:
{
  "pageNum": 1,           // 页码，从1开始
  "pageSize": 20,         // 每页数量，最大100
  "keyword": "搜索关键词",  // 模糊搜索（可选）
  "filters": {            // 精确筛选（可选）
    "status": "approved",
    "type": "contract"
  },
  "dateRange": {          // 日期范围（可选）
    "start": "2026-01-01",
    "end": "2026-06-07"
  },
  "sortField": "created_at",  // 排序字段（可选）
  "sortOrder": "desc"         // asc/desc
}

Response 200:
{
  "code": 0,
  "message": "success",
  "data": {
    "total": 150,
    "pageNum": 1,
    "pageSize": 20,
    "list": [
      {
        "id": 1,
        "name": "xxx",
        "status": "approved",
        "creatorName": "张三",
        "createdAt": "2026-06-07 10:00:00"
      }
    ]
  }
}

数据权限说明：
- 超级管理员：返回全部数据
- 部门管理员：返回本部门及下级部门数据（tenant_id + dept_id过滤）
- 普通用户：返回本人创建的数据（creator_id过滤）
```

#### API-03: 新增

```
POST /api/v1/xxx
Content-Type: application/json

Request Body:
{
  "name": "xxx",          // [必填] 名称，1-100字符
  "type": "contract",     // [必填] 类型，枚举值见数据字典
  "amount": 50000.00,     // [可选] 金额，0-99999999.99
  "date": "2026-06-07",   // [可选] 日期，格式yyyy-MM-dd
  "description": "xxx",   // [可选] 描述，≤500字符
  "attachmentIds": [1,2]  // [可选] 附件ID列表
}

校验规则：
- name: 必填，1-100字符，去除首尾空格，不能为纯空格
- type: 必填，必须是枚举值之一
- amount: 可选，≥0，保留2位小数
- date: 可选，不能早于1900-01-01

Response 200 (成功):
{
  "code": 0,
  "message": "success",
  "data": { "id": 123 }
}

Response 400 (校验失败):
{
  "code": 40001,
  "message": "参数校验失败",
  "errors": [
    { "field": "name", "message": "名称不能为空" }
  ]
}
```

### 3.3 通用响应码

| 错误码 | HTTP | 说明 | 前端处理 |
|--------|------|------|---------|
| 0 | 200 | 成功 | - |
| 40001 | 400 | 参数校验失败 | 表单标红 |
| 40100 | 401 | 未登录 | 跳转登录 |
| 40300 | 403 | 无权限 | 提示无权限 |
| 40400 | 404 | 资源不存在 | 返回列表 |
| 40900 | 409 | 数据冲突（并发） | 提示刷新重试 |
| 50000 | 500 | 服务异常 | 提示稍后重试 |

---

## 4. 业务逻辑

### 4.1 核心业务流程

```
[伪代码级别的流程描述，开发可据此编码]

1. 接收请求 → 参数校验
2. 权限检查：当前用户是否有[操作]权限
3. 数据范围检查：当前用户是否能操作该数据
4. 业务规则校验：
   a. 状态检查：当前状态是否允许此操作
   b. 规则检查：是否满足业务规则（如金额阈值）
5. 执行操作：
   a. 开启事务
   b. 更新主表
   c. 记录操作日志（审计）
   d. 触发审批流（如需要）
   e. 发送通知（如需要）
   f. 提交事务
6. 返回结果
```

### 4.2 业务规则详细说明

| 规则ID | 描述 | 触发条件 | 校验逻辑 | 失败提示 |
|--------|------|---------|---------|---------|
| BR-001 | 只有草稿状态可编辑 | 编辑操作 | status == 'draft' | "当前状态不允许编辑" |
| BR-002 | 审批中不能删除 | 删除操作 | status != 'pending_approval' | "审批中的记录不能删除" |
| BR-003 | 金额超50000需总经理审批 | 提交审批 | amount <= 50000 跳过节点 | - |

### 4.3 异常场景处理

| 异常 | 触发条件 | 处理方式 |
|------|---------|---------|
| 并发编辑 | 两人同时编辑同一条 | 乐观锁（version字段），后者提示刷新 |
| 重复提交 | 网络超时重试 | 防重Token，前端按钮loading+置灰 |
| 关联数据删除 | 删除被引用的数据 | 检查外键，有关联数据则禁止删除 |
| 附件上传失败 | 网络/容量/格式 | 重试机制，单文件≤10MB，总≤50MB |
| 批量操作部分失败 | 混合有效/无效数据 | 事务回滚 or 返回失败明细 |

---

## 5. 审批流定义

### 5.1 流程定义

```json
{
  "processKey": "contract_approval",
  "processName": "合同审批流程",
  "nodes": [
    {
      "nodeId": "node_start",
      "nodeName": "发起申请",
      "type": "start",
      "assignee": "${initiator}"
    },
    {
      "nodeId": "node_manager",
      "nodeName": "部门负责人审批",
      "type": "approval",
      "assignee": "${departmentManager}",
      "timeout": { "duration": 48, "unit": "hours", "action": "remind" }
    },
    {
      "nodeId": "node_finance",
      "nodeName": "财务审批",
      "type": "approval",
      "assignee": "role:finance_approver",
      "condition": "${amount > 5000}",
      "timeout": { "duration": 24, "unit": "hours", "action": "escalate" }
    },
    {
      "nodeId": "node_gm",
      "nodeName": "总经理审批",
      "type": "approval",
      "assignee": "role:general_manager",
      "condition": "${amount > 50000}",
      "timeout": { "duration": 72, "unit": "hours", "action": "remind" }
    },
    {
      "nodeId": "node_end",
      "nodeName": "完成",
      "type": "end"
    }
  ],
  "edges": [
    { "from": "node_start", "to": "node_manager" },
    { "from": "node_manager", "to": "node_finance" },
    { "from": "node_finance", "to": "node_gm" },
    { "from": "node_gm", "to": "node_end" }
  ]
}
```

### 5.2 审批操作与状态流转

| 操作 | 前置状态 | 后置状态 | 说明 |
|------|---------|---------|------|
| 提交 | draft | pending_approval | 进入审批流 |
| 通过 | pending_approval | pending_approval / approved | 最后节点通过→approved |
| 驳回 | pending_approval | rejected | 返回发起人 |
| 撤回 | pending_approval | draft | 仅发起人 |
| 催办 | pending_approval | pending_approval | 不变，发送通知 |

---

## 6. 消息通知

| 触发事件 | 通知对象 | 通知渠道 | 通知内容模板 |
|---------|---------|---------|------------|
| 提交审批 | 下一节点审批人 | 企微/钉钉/邮件/站内 | "您有新的审批待办：[标题]" |
| 审批通过 | 发起人 | 站内+企微 | "您的[标题]已通过审批" |
| 审批驳回 | 发起人 | 站内+企微+邮件 | "您的[标题]已被驳回，原因：[驳回意见]" |
| 超时提醒 | 当前审批人 | 站内+企微 | "您有[标题]待审批，已超过[X]小时" |
| 催办 | 当前审批人 | 站内+企微 | "[发起人]催办了[标题]，请尽快处理" |

---

## 7. 前端交互说明

### 7.1 页面状态

| 页面状态 | 触发条件 | 展示内容 |
|---------|---------|---------|
| 加载中 | 数据请求中 | 骨架屏/loading spinner |
| 空数据 | 无数据 | 空态插图+"还没有数据" + [新建]按钮 |
| 有数据 | 数据返回 | 正常列表/详情 |
| 网络错误 | 请求失败 | 错误提示+"点击重试"按钮 |
| 无权限 | 403 | "您没有权限访问此页面" + [返回]按钮 |

### 7.2 操作反馈

| 操作 | 反馈方式 | 持续时长 |
|------|---------|---------|
| 常规操作（新增/编辑） | Toast提示"操作成功" | 3秒 |
| 耗时操作（批量/导入） | 进度条+完成后Toast | 直至完成 |
| 危险操作（删除） | 弹窗二次确认 | 用户确认后方执行 |
| 失败操作 | Toast提示具体原因 | 5秒 |


---

## v1.1.0 新增: 定价模型功能规格

### 定价引擎功能需求
| 功能 | 描述 | 优先级 |
|------|------|--------|
| 多维度计费 | 支持按用量/按用户/按功能/按存储等多维度 | P0 |
| 套餐管理 | Free/Starter/Pro/Enterprise套餐配置 | P0 |
| 用量计量 | 实时用量统计+阈值告警 | P0 |
| 自动升降级 | 用量触发自动升级/降级 | P1 |
| 试用管理 | 免费试用期管理+到期提醒 | P1 |
| 发票管理 | 自动开票+多币种+多税率 | P1 |
| 优惠券/折扣 | 促销码+阶梯折扣+批量折扣 | P2 |
| 价格实验 | A/B测试不同价格方案 | P2 |

### 定价数据模型
| 实体 | 关键字段 | 说明 |
|------|---------|------|
| Plan(套餐) | name, price, features, limits | 套餐定义 |
| Subscription(订阅) | user_id, plan_id, start_date, end_date | 用户订阅 |
| Usage(用量) | user_id, metric, value, timestamp | 用量记录 |
| Invoice(发票) | user_id, amount, period, status | 账单 |