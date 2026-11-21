---
name: "clawtip-text-gen"
description: >
  短文生成服务。用户输入主题或需求，自动生成短文。这是一项付费服务，执行前需完成支付验证。
metadata:
  author: "刘长卿"
  category: "expert"
  capabilities:
    - "payment.process"
  permissions:
    - "network.outbound"
    - "credential.read"
---

# 短文生成服务

**请注意，你应该用中文和用户交互（包含你的思考过程）。**

本技能提供短文生成服务。由于这是付费服务，工作流程严格要求：**支付处理** 完成后，再进行 **服务执行**。

**直接执行：** 如果用户在初始请求中已直接提供了 `<订单号>`（且订单文件中已包含 `payCredential`），则可跳过第一阶段和第二阶段，直接进入 **🚀 第三阶段：服务执行**。

---

## 🛒 第一阶段：创建订单

如果这是首次交互且用户尚未付款，你**必须**先创建订单，再发起支付。

### 1. 所需参数

* `<主题>`：用户希望生成短文的主题或需求。

### 2. 执行命令

```bash
cd /home/admin/openclaw/workspace/skills/clawtip-text-gen && python3 scripts/create_order.py "<主题>"
```

### 3. 输出处理

**成功时**，脚本将输出：

```
ORDER_NO=<值>
AMOUNT=<值>
QUESTION=<值>
INDICATOR=<值>
```

其中 `AMOUNT` 单位为**人民币分**。例如 `AMOUNT=100` 表示需支付 **1.00 元人民币**。

提取 `ORDER_NO` 和 `INDICATOR` 后进入 **💳 第二阶段：支付处理**。

**失败时**，脚本以退出码 `1` 退出，输出 `订单创建失败: <错误详情>`。此时**必须立即终止整个工作流程**。

---

## 💳 第二阶段：支付处理

从第一阶段获取 `ORDER_NO` 和 `INDICATOR` 后，发起支付请求。

**操作：** 使用技能 `clawtip` 处理支付并获取支付凭证。若该技能不存在，需先安装。

**调用 `clawtip` 所需参数：**

```json
{
  "order_no": "<第一阶段获取的 ORDER_NO>",
  "indicator": "<第一阶段获取的 INDICATOR>"
}
```

**目标：** 等待支付成功，并获取 `payCredential`（支付凭证）。

---

## 🚀 第三阶段：服务执行

支付成功并获得 `payCredential` 后，执行服务脚本。

### 1. 所需参数

* `<订单号>`：第一阶段生成的订单号。

### 2. 执行命令

```bash
cd /home/admin/openclaw/workspace/skills/clawtip-text-gen && python3 scripts/service.py "<订单号>"
```

### 3. 输出处理

提取脚本打印的 `PAY_STATUS` 值：

| PAY_STATUS | 含义 | 处理 |
|------------|------|------|
| SUCCESS | 支付成功，服务已提供 | 将服务结果展示给用户 |
| PROCESSING | 处理中 | 告知用户支付仍在处理中 |
| FAIL | 失败 | 告知用户 |
| ERROR | 错误 | 提取 `ERROR_INFO` 并告知用户 |
