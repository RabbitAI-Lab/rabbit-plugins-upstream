---
slug: "qq-zone-photo-free"
name: "qq-zone-photo-free"
version: 1.0.1
displayName: "社交空间相册基础版"
summary: "基础社交空间相册管理，扫码登录、列出和浏览相册。社交空间相册自动化管理工具的免费版。支持扫码登录、列出相册和浏览照片等基础功能. 适用于相册查看和照片URL获取场景。升级至完整版可解锁照片上"
summary_zh: "基础社交空间相册管理，扫码登录、列出和浏览相册。社交空间相册自动化管理工具的免费版。支持扫码登录、列出相册和浏览照片等基础功能. 适用于相册查看和照片URL获取场景。升级至完整版可解锁照片上"
license: "MIT"
description: "|-. 适用于需要qq zone photo相关能力的开发场景,包含结构化的工作流程和可复用的模板,帮助用户快速完成任务并保持代码质量.该技能适用于相关开发场景,包含结构化的工作流程和配置指引.经过深度差异化处置,针对用户反馈和使用痛点进行了改进,提升了实用性和可操作性.该技能适用于相关开发场景,包含结构化的工作流程和配置指引.经过深度差异化处置,针对用户反馈和使用痛点进行了改进,提升了实用性和可操作性."
  社交空间相册自动化管理工具的免费版。支持扫码登录、列出相册和浏览照片等基础功能.
  适用于相册查看和照片URL获取场景。升级至完整版可解锁照片上传、单张下载、
  整册下载和相册创建功能.
tools:
  - read
  - exec
  - write
homepage: ""
tags:
  - 通用办公
  - zone
  - photo
  - automation
  - productivity
  - 工具
  - 效率
  - 通信
  - 邮件
  - action
category: "Automation"
pricing_tier: free
---
# 社交空间相册（免费版）

社交空间相册自动化管理工具的免费版。支持扫码登录、列出相册和浏览照片等基础功能。通过 `qzone_photos.py` 脚本调用社交空间非官方API实现自动化操作.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 社交空间相册基础版处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 安全与隐私

- Cookie文件包含社交空间完整访问权限，请勿泄露或分享
- 凭证仅存储在本地，不会上传到任何服务器
- 会话Cookie有时效性，过期后需重新登录
- 本工具使用社交空间非官方API，平台更新接口后可能需要适配

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
export API_KEY=${API_KEY:?请设置环境变量}
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 核心能力

### 1. 扫码登录

通过 `python3 （请参考skill目录中的脚本文件） --action login --cookies cookies.json` 执行扫码登录。生成二维码供用户扫描，登录成功后自动将Cookie保存到指定的cookies文件中。Cookie包含 `qq_number`、`p_skey`、`skey` 和 `uin` 字段。适用于首次使用或Cookie过期后的重新认证.
### 2. 列出相册

通过 `python3 （请参考skill目录中的脚本文件） --action list --cookies cookies.json` 列出当前账号的所有相册。返回相册列表，包含相册ID（`album-id`）、相册标题、照片数量等信息。可选参数 `--qq` 指定目标账号。适用于浏览相册结构和获取相册ID。- 验证返回数据的完整性和格式正确性
### 3. 浏览相册照片

通过 `python3 （请参考skill目录中的脚本文件） --action photos --album-id "ALBUM_ID" --cookies cookies.json` 浏览指定相册中的照片。必填参数 `--album-id` 指定目标相册，可选参数 `--qq` 指定账号。返回照片列表，包含照片URL、缩略图、上传时间等信息。适用于查看相册内容。- 验证返回数据的完整性和格式正确性
- 参考`浏览相册照片`的配置文档进行参数调优
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 升级提示

以下为完整版（qq-zone-photo）独有功能，免费版不可用：

- **上传照片**：`--action upload` 将本地照片上传到指定相册，支持JPG/PNG/GIF等格式
- **下载单张照片**：`--action download` 通过照片URL下载单张照片到本地
- **下载整个相册**：`--action download-album` 批量下载整个相册的所有照片
- **创建相册**：`--action create` 创建新相册，支持设置标题和描述

升级至完整版以获取全部能力.
## 使用流程

1. 首次使用执行扫码登录：`python3 （请参考skill目录中的脚本文件） --action login --cookies cookies.json`
2. 列出所有相册获取目标 `album-id`：`python3 （请参考skill目录中的脚本文件） --action list --cookies cookies.json`
3. 浏览指定相册照片：`python3 （请参考skill目录中的脚本文件） --action photos --album-id "ALBUM_ID" --cookies cookies.json`
4. 如需上传、下载或创建相册功能，升级至完整版
5. 如遇Cookie过期，重新执行 `login` action获取新Cookie

**结果验证**: 任务完成后,查看输出确认状态。成功时返回摘要和数据;失败时根据错误信息排查,参考恢复章节获取修复步骤.
## 示例

### 示例1：扫码登录并浏览相册

```bash
# 扫码登录，Cookie自动保存到cookies.json
python3 （请参考skill目录中的脚本文件） --action login --cookies cookies.json
# 输出: 二维码已生成，请使用社交平台App扫描登录...
# 登录成功后: Cookie已保存到 cookies.json
# ...
# 列出所有相册
python3 （请参考skill目录中的脚本文件） --action list --cookies cookies.json
# 输出示例:
# 相册ID: V0003 | 标题: 旅行 | 照片数: 45
# 相册ID: V0005 | 标题: 2024毕业季 | 照片数: 28
```

### 示例2：浏览指定相册照片

```bash
# 浏览旅行相册中的照片
python3 （请参考skill目录中的脚本文件） --action photos --album-id "V0003" --cookies cookies.json
# 输出示例:
# 照片1: URL=https://photo.example.com/001.jpg | 上传时间: 2024-06-15
# 照片2: URL=https://photo.example.com/002.jpg | 上传时间: 2024-06-15
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| Cookie过期 | `p_skey` 或 `skey` 失效 | 重新执行 `--action login` 扫码登录获取新Cookie |
| 相册ID无效 | `--album-id` 指向不存在的相册 | 先执行 `--action list` 获取有效的 `album-id` |
| Cookie文件格式错误 | `cookies.json` JSON格式不正确 | 确认文件包含 `qq_number`、`p_skey`、`skey`、`uin` 四个字段且JSON格式有效 |
| 虚拟环境未激活 | 未执行 `source .venv/（请参考skill目录中的脚本文件）` | 先激活虚拟环境再执行脚本命令 |
| 请求上传功能 | 免费版不支持 `--action upload` | 升级至完整版以使用照片上传功能 |
| 请求下载功能 | 免费版不支持 `--action download`/`download-album` | 升级至完整版以使用照片下载功能 |
| 请求创建相册 | 免费版不支持 `--action create` | 升级至完整版以使用相册创建功能 |

## 常见问题

### Q1: 如何扫码登录？

执行 `python3 （请参考skill目录中的脚本文件） --action login --cookies cookies.json` 命令。脚本会生成二维码，使用社交平台App扫描二维码完成登录。登录成功后Cookie自动保存到指定的cookies文件中，包含 `qq_number`、`p_skey`、`skey` 和 `uin` 字段.
### Q2: Cookie过期怎么办？

Cookie包含的 `p_skey` 和 `skey` 有时效性，过期后所有操作会返回认证失败。重新执行 `--action login` 扫码登录即可获取新的Cookie.
### Q3: 如何获取相册ID？

执行 `python3 （请参考skill目录中的脚本文件） --action list --cookies cookies.json` 列出所有相册。返回结果包含每个相册的ID（`album-id`）、标题和照片数量。使用返回的 `album-id` 进行后续的照片浏览操作.
### Q4: 免费版可以上传照片吗？

不可以。`--action upload` 上传照片是完整版独有功能。免费版仅支持扫码登录、列出相册和浏览照片。如需上传照片，请升级至完整版.
### Q5: 免费版可以下载照片吗？

不可以。`--action download`（单张下载）和 `--action download-album`（整册下载）是完整版独有功能。免费版可以浏览照片并获取照片URL，但不能下载。如需下载照片，请升级至完整版.
### Q6: Cookie文件包含哪些字段？

Cookie文件（`cookies.json`）为JSON格式，包含4个字段：`qq_number`（社交平台账号）、`p_skey`（认证密钥）、`skey`（会话密钥）和 `uin`（用户标识，格式如 `o0123456789`）。推荐使用扫码登录自动获取.
## 已知限制

- 不支持照片上传（`--action upload`），完整版可用
- 不支持照片下载（`--action download`/`download-album`），完整版可用
- 不支持相册创建（`--action create`），完整版可用
- 依赖社交空间非官方API，平台接口变更后可能需要适配
- Cookie有时效性，过期后需重新扫码登录
- 需要Python虚拟环境（`.venv`）已激活
