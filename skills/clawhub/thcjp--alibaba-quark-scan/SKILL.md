---
slug: "alibaba-quark-scan"
name: "alibaba-quark-scan"
version: 1.0.19
displayName: "文档扫描增强"
summary: "文档高清扫描增强工具，支持画质优化、去手写、去水印、去阴影等13种场景"
license: "Proprietary"
description: |-
  文档高清扫描增强工具，通过扫描服务API对图片进行画质优化、瑕疵去除和视觉增强.
  支持13种场景：考试增强、画质增强、证件票据增强、去手写、去水印、去阴影、去屏纹、
  去底色、裁剪矫正、素描速写、提取线稿、扫描合同、扫描文件。适用于独立开发者、
  企业团队和自动化工作流场景。不适用于视频处理和实时摄像头流.
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
tags:
  - 通用办公
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"

---
# 文档扫描增强工具

通过扫描服务API对图片进行高清扫描、画质优化和瑕疵去除。支持13种场景识别，每次请求只执行一个意图类型.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 文档扫描增强处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 文档扫描增强文档高清扫描 | 不支持 | 支持 |
| 深度漏洞扫描与CVE关联 | 不支持 | 支持 |
| 安全基线合规审计 | 不支持 | 支持 |
| 批量资产风险评分 | 不支持 | 支持 |
| 威胁情报实时订阅与告警 | 不支持 | 支持 |

## 隐私与数据流向

- 图片发送至扫描服务官方服务器进行识别处理
- 服务端不会永久保存图片内容
- 识别返回的图片保存至系统临时目录（如 `/tmp/imgs`）
- `SCAN_WEBSERVICE_KEY` 应妥善保管，泄露后需及时轮换

## 配置

通过环境变量配置API密钥：

```bash
skill-platform config set skills.entries.alibaba-quark-scan.env.SCAN_WEBSERVICE_KEY "your_scan_webservice_key_here"
```

配置后需重启或开启新会话才能生效.
## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
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

### 1. 考试增强（exam-enhance）
将手写笔记、试卷、教材等学习资料照片转化为高清、去噪、背景纯净的电子文档.
- scene标识：`exam-enhance`
- 示例指令："把这张拍糊了的试卷变清晰后发给我"

**输入**: 用户提供考试增强（exam-enhance）所需的指令和必要参数.
**处理**: 解析考试增强（exam-enhance）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回考试增强（exam-enhance）的处理结果,包含执行状态码、结果数据和执行日志.
### 2. 画质增强（image-hd-enhance）
将模糊、昏暗、老旧或低质量照片进行画质增强，改善视觉效果和可读性.
- scene标识：`image-hd-enhance`
- 示例指令："这张老照片太模糊了，帮我把画质变清晰一点"

**输入**: 用户提供画质增强（image-hd-enhance）所需的指令和必要参数.
**处理**: 解析画质增强（image-hd-enhance）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回画质增强（image-hd-enhance）的处理结果,包含执行状态码、结果数据和执行日志.
### 3. 证件票据增强（certificate-enhance）
对模糊、光线不佳的证件及票据照片进行画质优化，使文字与关键信息清晰可辨.
- scene标识：`certificate-enhance`
- 示例指令："帮我把这张购物小票上的金额和日期部分增强清楚"

**处理**: 解析证件票据增强（certificate-enhance）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回证件票据增强（certificate-enhance）的处理结果,包含执行状态码、结果数据和执行日志.
### 4. 图像去手写（remove-handwriting）
将手写笔迹、划痕从印刷文档图像中自动清除，保留原始印刷文字与格式.
- scene标识：`remove-handwriting`
- 示例指令："把这张做过的试卷上的手写答案去掉，还原成空白卷子"

**输入**: 用户提供图像去手写（remove-handwriting）所需的指令和必要参数.
**处理**: 解析图像去手写（remove-handwriting）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回图像去手写（remove-handwriting）的处理结果,包含执行状态码、结果数据和执行日志.
### 5. 图像去水印（remove-watermark）
精准去除图片水印（文字、Logo、标记等），不损伤背景和整体构图.
- scene标识：`remove-watermark`
- 示例指令："帮我把图片右下角的网站水印去掉"

**输入**: 用户提供图像去水印（remove-watermark）所需的指令和必要参数.
**处理**: 解析图像去水印（remove-watermark）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回图像去水印（remove-watermark）的处理结果,包含执行状态码、结果数据和执行日志.
### 6. 图像去阴影（remove-shadow）
去除文档或图像中因拍摄角度、光线产生的阴影，获得均匀亮度的高清扫描效果.
- scene标识：`remove-shadow`
- 示例指令："这张纸拍出来有大片阴影，请帮我去除阴影变平整"

**输入**: 用户提供图像去阴影（remove-shadow）所需的指令和必要参数.
**处理**: 解析图像去阴影（remove-shadow）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回图像去阴影（remove-shadow）的处理结果,包含执行状态码、结果数据和执行日志.
### 7. 图像去屏纹（remove-screen-pattern）
修复拍摄屏幕时产生的摩尔纹、反光、低对比度等问题，获得清晰文档图像.
- scene标识：`remove-screen-pattern`
- 示例指令："这张对着电脑屏幕拍的照片有很多波纹，请帮我消除屏纹"

**输入**: 用户提供图像去屏纹（remove-screen-pattern）所需的指令和必要参数.
**处理**: 解析图像去屏纹（remove-screen-pattern）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回图像去屏纹（remove-screen-pattern）的处理结果,包含执行状态码、结果数据和执行日志.
### 8. 文档去底色（remove-background-color）
将带有彩色背景、水印、阴影的文档截图一键转换为纯白背景加黑色文字.
- scene标识：`remove-background-color`
- 示例指令："把这张红头文件的红色背景去掉，变成白底黑字"

**输入**: 用户提供文档去底色（remove-background-color）所需的指令和必要参数.
**输出**: 返回文档去底色（remove-background-color）的处理结果,包含执行状态码、结果数据和执行日志.
### 9. 图像裁剪矫正（image-crop-rectify）
对图像进行自动矫正（透视校正、水平对齐）并智能裁剪多余边缘.
- scene标识：`image-crop-rectify`
- 示例指令："这张照片拍歪了，帮我把文档扶正并裁掉多余的桌子背景"

**处理**: 解析图像裁剪矫正（image-crop-rectify）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回图像裁剪矫正（image-crop-rectify）的处理结果,包含执行状态码、结果数据和执行日志.
### 10. 素描速写（sketch-drawing）
将普通照片转换为素描或速写风格图像，突出线条与明暗关系.
- scene标识：`sketch-drawing`
- 示例指令："把这张人物照片转换成铅笔素描风格"

**输入**: 用户提供素描速写（sketch-drawing）所需的指令和必要参数.
**输出**: 返回素描速写（sketch-drawing）的处理结果,包含执行状态码、结果数据和执行日志.
### 11. 提取线稿（extract-lineart）
从图片中提取线稿，将图像转换为简洁的线条形式图，用于艺术创作.
- scene标识：`extract-lineart`
- 示例指令："从这张动漫图片中提取纯线稿，去掉颜色"

**输入**: 用户提供提取线稿（extract-lineart）所需的指令和必要参数.
**输出**: 返回提取线稿（extract-lineart）的处理结果,包含执行状态码、结果数据和执行日志.
### 12. 扫描合同（scan-contract）
对合同或协议图片进行画质优化，让文字更清晰，画面更整洁，便于归档.
- scene标识：`scan-contract`
- 示例指令："帮我把这份合同高清优化一下"

**输入**: 用户提供扫描合同（scan-contract）所需的指令和必要参数.
**处理**: 解析扫描合同（scan-contract）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回扫描合同（scan-contract）的处理结果,包含执行状态码、结果数据和执行日志.
### 13. 扫描文件兜底（scan-document）
当用户指令不包含上述具体场景，仅表达优化意图时，调用扫描文件场景.
- scene标识：`scan-document`
- 示例指令："优化一下这张文档图片，让它看起来更专业"

#
## 使用流程

### 第一步：输入处理

识别用户传入的图片类型，只能是以下三种之一：
- 图片URL：`--url`
- 本地文件路径：`--path`
- 图片BASE64：`--base64`

未提供任何有效图片时，返回错误码 `A0201`.
### 第二步：意图匹配

按照场景列表从上到下顺序匹配，命中第一个即停止，只确定当前意图对应的scene标识.
### 第三步：构建执行命令

根据图片类型，严格使用对应格式：

```bash
python3 （请参考skill目录中的脚本文件） --scene "exam-enhance" --url "https://example.com/exam.jpg" --platform "skill-platform"
# ...
python3 （请参考skill目录中的脚本文件） --scene "remove-watermark" --path "/tmp/image.png" --platform "skill-platform"
# ...
python3 （请参考skill目录中的脚本文件） --scene "scan-contract" --base64 "iVBORw0KGgoAAAANSUhEUgAA..." --platform "skill-platform"
```

- `--platform` 替换为当前运行的Agent平台名称，无法确定时填 `community`
- `--scene` 必须使用本文档指定的场景名，严禁自行构造
- 直接执行命令，不增删任何参数

### 第四步：结果透出

执行完成后原样返回执行结果，不修改、不翻译、不美化。当 `scan.py` 调用成功（`code == "00000"`）且响应包含 `ImageBase64` 时，`file_saver.py` 会自动解码保存为本地图片文件，返回 `data` 替换为 `{"path": "/tmp/xxx.png"}`.
## 真实示例

### 示例1：考试试卷增强

```bash
python3 （请参考skill目录中的脚本文件） --scene "exam-enhance" --path "/tmp/exam_photo.jpg" --platform "skill-platform"
```

输出：
```json
{
  "code": "00000",
  "message": "success",
  "data": {"path": "/tmp/imgs/exam_enhanced_20260721.png"}
}
```

### 示例2：去水印

```bash
python3 （请参考skill目录中的脚本文件） --scene "remove-watermark" --url "https://example.com/watermarked.png" --platform "community"
```

输出：
```json
{
  "code": "00000",
  "message": "success",
  "data": {"path": "/tmp/imgs/nowm_20260721_143022.png"}
}
```

### 示例3：缺少图片输入

```json
{
  "code": "A0201",
  "message": "缺少图片输入，请提供图片链接、文件路径或 BASE64 数据。",
  "data": null
}
```

## 不支持的场景

| 不支持的场景 | 原因 | 建议替代方案 |
|:-----:|:-----:|:-----:|
| 视频处理 | 仅支持单张静态图片 | 先提取视频帧，再逐帧处理 |
| 批量处理 | 每次调用仅限单张图片 | 循环调用或联系管理员 |
| 实时摄像头流 | 非实时流处理架构 | 使用专用视频处理服务 |
| 超大图片（>5MB） | API限制 | 先压缩或裁剪后再处理 |
| 非图片格式 | 仅支持8种格式 | 先转换为支持的图片格式 |

## 错误处理

| 错误场景 | 错误码/原因 | 处理方式 |
|:------|------:|:------|
| 缺少图片输入 | `A0201` | 提供图片URL、文件路径或BASE64数据 |
| 图片超过5MB限制 | API拒绝处理 | 先压缩或裁剪图片至5MB以下 |
| 不支持的图片格式 | 格式校验失败 | 转换为jpg/jpeg/png/gif/bmp/webp/tiff/wbmp之一 |
| `SCAN_WEBSERVICE_KEY`未配置 | 认证失败 | 通过config命令配置API密钥后重启会话 |
| API服务端返回非00000错误码 | 服务端处理异常 | 原样透出错误信息， |
| 网络连接扫描服务超时 | 网络不可达 |  |
| 自行构造`--scene`参数值 | 场景标识无效 | 必须使用本文档指定的13种场景名 |

## 常见问题

### Q1: 支持哪些图片格式？
A: 支持8种格式：jpg、jpeg、png、gif、bmp、webp、tiff、wbmp。其他格式需先转换.
### Q2: 图片大小限制是多少？
A: 本地文件不超过5MB。超过限制时需先压缩或裁剪.
### Q3: 如何配置API密钥？
A: 使用 `skill-platform config set skills.entries.alibaba-quark-scan.env.SCAN_WEBSERVICE_KEY "your_key"` 配置，配置后需重启会话生效.
### Q4: 支持批量处理多张图片吗？
A: 不支持。每次调用仅限单张图片。如需批量处理，请循环调用或联系管理员.
### Q5: 处理结果保存在哪里？
A: 成功处理后的图片由 `file_saver.py` 自动保存至系统临时目录（如 `/tmp/imgs`），返回JSON中包含 `path` 字段。文件持续存在直到手动清理.
### Q6: 支持视频处理吗？
A: 不支持。仅支持单张静态图片处理。视频需先提取帧再逐帧处理.
### Q7: 如何获取API密钥？
A: 访问扫描服务官方开发者后台，登录/注册账号后查看API Key。密钥应妥善保管，泄露后需及时轮换.
## 已知限制

- 禁止修改固定命令格式，只能替换场景标识和图片占位符
- 严禁自行构造 `--scene` 参数值，必须使用本文档指定的13种场景名
- 图片大小限制：本地文件不超过5MB
- 支持格式：jpg/jpeg/png/gif/bmp/webp/tiff/wbmp
- 每次调用仅限单张图片，不支持批量处理
