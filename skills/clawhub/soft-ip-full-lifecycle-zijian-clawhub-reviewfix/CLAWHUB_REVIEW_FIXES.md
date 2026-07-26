---
title: ClawHub Review Fixes
skill: soft-ip-full-lifecycle-zijian
updated: 2026-07-14
author: Yujin
---

# ClawHub Review Fixes

## 目标

当前 `soft-ip-full-lifecycle-zijian` 被 ClawHub 标记为 `Needs review`，主要命中：

- `Data Exfiltration`
- `Excessive Agency`
- `Taint Tracking`
- `MCP Tool Poisoning`
- `Missing User Warnings`

这个清单的目标不是保证 100% 自动放行，而是把最容易触发审计器的点压下来。

## 必改项

### 1. `scripts/create_order.py`

#### 问题 A：`SERVER_URL` 可通过环境变量直接覆盖

当前模式：

```python
SERVER_URL = os.environ.get("CLAWTIP_SERVER_URL", "https://...")
```

审计器会把它理解成：

- 外发目标可变
- 可将订单或凭证发往任意地址

#### 修改建议

改成“固定地址”或“白名单校验后才允许使用”。

推荐方案：

```python
DEFAULT_SERVER_URL = "https://your-fixed-domain.example"
ALLOWED_HOSTS = {
    "your-fixed-domain.example",
    "vehicles-consumer-induced-beneficial.trycloudflare.com",
}
```

然后校验 `CLAWTIP_SERVER_URL` 的 host，不在白名单就回退到默认值。

#### 问题 B：把原始请求写入本地订单文件

当前模式：

```python
"local_question": question
```

软著技能里这个字段通常包含：

- 本地项目路径
- 项目名
- 申报目标
- 用户补充说明

这会被审计器视为“把潜在敏感信息持久化到磁盘”。

#### 修改建议

优先级从高到低：

1. 最优：不要落盘原始 `question`
2. 次优：只保存摘要，例如：

```python
"local_question_summary": "software-ip-request"
```

3. 如果后续执行必须依赖原始输入，则在 `service.py` 阶段重新要求用户输入，而不是从订单 JSON 回读

#### 问题 C：缺少显式提示

当前脚本虽然最小化上送数据，但对用户没有明确提示：

- 会访问远端支付服务
- 会在本地保存订单文件
- 不会上传源码正文

#### 修改建议

在脚本开始输出简短提示，例如：

```python
print("NOTICE: this step creates a local order file and sends only minimal payment metadata to the payment service.")
print("NOTICE: project source files are not uploaded in create_order.")
```

---

### 2. `scripts/service.py`

#### 问题 A：发送 `credential` 到远端前没有用户可见提示

当前逻辑会直接把：

- `slug`
- `orderNo`
- `credential`

发到远端。

这对支付闭环是必要的，但审计器会视作：

- secret 外发
- 缺少显式告知

#### 修改建议

在发请求前输出明确说明：

```python
print("NOTICE: this step sends the payment credential to the payment service for verification and fulfillment authorization only.")
print("NOTICE: project source files are not uploaded in service verification.")
```

#### 问题 B：从本地订单文件读取 `local_question`

当前模式：

```python
question = order_data.get("local_question") or order_data.get("question")
```

这会放大审计器对“本地敏感数据持久化”的判断。

#### 修改建议

改成以下两种之一：

1. 不再依赖本地订单文件保存原始请求，执行时重新输入：

```bash
python3 scripts/service.py "<order_no>" "<project_path_or_request>"
```

2. 或只读取最小摘要，不读取用户原文

#### 问题 C：错误信息里不要暗示会处理完整项目数据

现在文案虽然不算严重，但建议进一步收紧，避免“自动处理整个项目”的感觉。

---

### 3. `scripts/file_utils.py`

#### 问题 A：订单文件落在固定用户目录

当前目录：

- Windows: `~/openclaw/skills/orders/{indicator}/`
- Linux/macOS: `~/.openclaw/skills/orders/{indicator}/`

这个本身不是漏洞，但会被审计器理解为：

- 长期持久化
- 本地状态残留

#### 修改建议

保留目录结构可以，但要加两点：

1. 在 `save_order` 前只保存最小字段
2. 在文档中说明这些文件仅用于支付流程，且不保存源码正文

可选增强：

- 增加 TTL / 清理命令
- 增加注释说明为什么只接受 `indicator` 和 `order_no`

---

### 4. `SKILL.md`

#### 问题 A：能力描述过重

当前文案容易让审计器理解成：

- 自动扫描项目
- 自动生成 8 份材料
- 自动推进完整申报流程

这会触发：

- `Excessive Agency`
- `MCP Tool Poisoning`

#### 修改建议

把措辞统一改成“受限辅助”。

推荐表达：

- “Only generate draft markdown materials after user confirmation.”
- “Do not submit anything to any official platform.”
- “Read only the files necessary for the current step.”
- “Require explicit user confirmation before each document draft.”

#### 问题 B：强化用户确认边界

需要在 `SKILL.md` 里更显眼地写：

1. 只生成草稿
2. 不自动提交
3. 不自动上传源码
4. 每份文档生成前需要用户确认
5. 支付验证只发送最小元数据和支付凭证

#### 问题 C：补充本地持久化说明

需要明确写：

- 本地订单文件会保存订单元数据
- 不保存源码正文
- 如包含项目路径，属于用户本地可见信息，仅用于本地流程衔接

如果你准备彻底规避审计，最好直接移除项目路径落盘。

---

## 推荐改法顺序

1. 先改 `create_order.py`
   - 去掉 `local_question` 落盘
   - 加白名单 URL 校验
   - 加用户提示

2. 再改 `service.py`
   - 不再从订单 JSON 读取原始请求
   - 改成执行时重新传入，或只读摘要
   - 加发送 `credential` 的提示

3. 再改 `SKILL.md`
   - 收紧能力描述
   - 强调用户确认和最小化上送

4. 最后再发 ClawHub 新版本
   - patch 版本递增
   - 重新等待审核

## 建议的下一版目标

目标不是“零提示”，而是把结论从：

- `Critical` / `High`

压到：

- 仅人工复核
- 或更少的中低风险提示

## 备注

`obsidian-memory-system` 之所以更容易过，是因为它的本地持久化和项目路径语义更轻。  
`soft-ip-full-lifecycle-zijian` 天然更像“读取本地项目后生成材料”，所以必须主动收紧本地存储、外发目标和文案边界。
