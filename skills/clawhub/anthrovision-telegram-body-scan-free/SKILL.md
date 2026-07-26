---
slug: "anthrovision-telegram-body-scan-free"
name: "anthrovision-telegram-body-scan-free"
version: "1.0.0"
displayName: "Body Scan Basic"
summary: "在Telegram中运行基础身体扫描流程,提交视频并轮询测量结果"
license: "MIT"
description: |-
  在Telegram中运行基础身体扫描测量流程。提交视频至AnthroVision桥接工具,
  轮询状态并输出基础测量结果。基础版覆盖输入校验、扫描提交与状态轮询.
  适用场景:基础体型测量、健身追踪.
  不适用于腰臀比汇总、超时处理、确定性格式化等高级场景.
tags:
  - Communication
tools:
  - read
  - exec
homepage: "https://skillhub.cn"

---
# Anthrovision Telegram Body Scan Free

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | Body Scan Basic处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 概述

在Telegram中运行基础身体扫描测量流程。提交视频至AnthroVision桥接工具,轮询状态并输出基础测量结果。基础版覆盖输入校验、扫描提交与状态轮询.
## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-----|:-----|:-----|:-----|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 核心能力

### 1. 输入校验(基础)
- 必需输入: `gender`(male/female)、`height_cm`(100-250)、`video`附件或可下载URL、`phone_model`
- 拒绝本地文件路径与私有/本地URL

**处理**: 解析输入校验(基础)的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回输入校验(基础)的处理结果,包含执行状态码、结果数据和执行日志.
### 2. 扫描提交与轮询(基础)
- 调用 `anthrovision_bridge_submit_scan` 提交
- 调用 `anthrovision_bridge_check_scan` 轮询状态
- 状态complete时输出基础测量结果

**输入**: 用户提供扫描提交与轮询(基础)所需的指令和必要参数.
#
## 适用场景

| 场景 | 输入 | 输出 |
|---:|---:|---:|
| 基础男性身体扫描 | gender=male, height_cm=180, 视频附件 | scan_id确认,轮询后输出基础测量数据 |
| 基础女性体型测量 | gender=female, height_cm=165, 视频URL | scan_id确认,轮询后输出基础测量数据 |

**不适用于**: 腰臀比汇总、确定性响应格式化、超时处理、手机型号校准提示.
## 使用流程

1. **校验必需输入**: 确认 `gender`、`height_cm`、`video`、`phone_model` 均已提供,拒绝本地路径与私有URL
2. **提交扫描**: 调用 `anthrovision_bridge_submit_scan`,发送scan_id确认
3. **轮询状态**: 调用 `anthrovision_bridge_check_scan` 检查状态,processing时继续轮询
4. **输出结果**: 状态complete时输出基础测量数据

## 案例展示

### 案例1: 基础男性身体扫描

输入:
- gender: male
- height_cm: 180
- video: 附件
- phone_model: iPhone 13

流程:
```
1. 校验输入通过
2. 调用 anthrovision_bridge_submit_scan
3. 发送确认: scan_id=scan_a1b2c3, status=processing
4. 轮询,第48秒状态变为complete
```

输出:
```
- scan_id: scan_a1b2c3
- status: complete
- 测量数据: 胸围 102.3 cm, 腰围 84.7 cm, 臀围 98.1 cm
```

### 案例2: 基础女性体型测量

输入:
- gender: female
- height_cm: 165
- video: https://example.com/scan/female_165.mp4
- phone_model: Samsung S23

流程:
```
1. 校验输入通过,URL为https可下载
2. 调用 anthrovision_bridge_submit_scan
3. 发送确认: scan_id=scan_d4e5f6, status=processing
4. 轮询,第75秒状态变为complete
```

输出:
```
- scan_id: scan_d4e5f6
- status: complete
- 测量数据: 胸围 88.5 cm, 腰围 71.2 cm, 臀围 91.4 cm
```

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| height_cm超出范围 | 输入值<100或>250 | 提示身高范围需为100-250cm,要求重新提供 |
| gender值无效 | 输入非male/female | 提示仅支持male或female,要求重新提供 |
| 本地文件路径提交 | 用户提供 `/Users/...`、`file://...` 路径 | 拒绝本地路径,要求上传附件或提供 `https://` URL |
| 私有URL提交 | URL为localhost、127.0.0.1、RFC1918网段 | 拒绝私有URL,要求提供公网 `https://` URL |
| scan_id未找到 | check_scan的scan_id不存在 | 确认scan_id与提交时一致,若已过期需重新提交 |

## 常见问题

### Q1: 需要哪些输入?
A: 需要 `gender`(male/female)、`height_cm`(100-250)、`video`附件或可下载 `https://` URL、`phone_model`(如iPhone 13)。不接受本地文件路径与私有网段URL.
### Q2: 处理需要多长时间?
A: 一般48-90秒完成。处理期间轮询状态,complete后输出测量数据。超过3分钟的超时处理(延迟消息与询问)需升级付费版.
### Q3: 输出包含腰臀比吗?
A: 免费版仅输出基础测量数据(胸围、腰围、臀围),不提供腰臀比汇总与确定性分组格式化。如需腰臀比与确定性格式化输出,请升级付费版.
### Q4: 手机型号未校准怎么办?
A: 免费版不提供手机型号校准提示,未校准机型测量精度可能下降且无提示。如需校准提示与机型建议,请升级付费版.
## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|:---------|---------:|:---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 检查网络连接和配置后重试；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 仅支持单人身体视频扫描
- 身高范围限制100-250cm
- 不提供腰臀比汇总与确定性响应格式化
- 不提供超时处理(3分钟延迟消息与询问)
- 不提供手机型号校准提示
- 不提供显式同意流程(需用户自行确保合规)
- 输出仅含基础测量数值,不提供医疗或健康解读

## 升级提示

如需完整功能,请升级付费版,解锁以下能力:
- 显式同意流程:处理真实人物视频前获取明确同意
- 腰臀比汇总:输出腰臀比(waist-to-hip ratio)与典型范围参考
- 确定性响应格式化:结构化字段固定格式输出,不透传上游不可信文本
- 超时处理:3分钟阈值延迟消息与继续等待询问
- 手机型号校准提示:未校准机型提示与已校准机型建议
- 周期性轮询优化:10-15秒静默轮询,processing状态不发送额外消息
