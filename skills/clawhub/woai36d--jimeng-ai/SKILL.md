---
name: jimeng-ai
description: 即梦AI图像生成技能。使用即梦AI官方会员账号进行文生图、图生图。支持工作流集成、sessionid自动更新机制、图片自动下载保存。当用户需要AI生成图片、绘画、文生图时触发。
---

# Jimeng AI Skill

即梦AI图像生成技能封装，基于 jimeng-free-api 服务。

## 前置要求

- 即梦AI官方会员账号
- sessionid（从网页端获取）

## 获取 sessionid

1. 打开 https://jimeng.jianying.com/ 并登录
2. F12 打开开发者工具 → Application → Cookies
3. 复制 `sessionid` 的值

## 工具列表

### 1. jimeng_generate - 文生图

生成图片并自动保存到本地。

**参数：**
- `prompt` (string, 必需): 图片描述
- `n` (number, 可选): 生成数量 1-4，默认 1
- `model` (string, 可选): 模型版本，默认 `jimeng-3.0`
- `width` (number, 可选): 图片宽度，默认 1024
- `height` (number, 可选): 图片高度，默认 1024
- `output_dir` (string, 可选): 保存目录，默认 `~/.openclaw/workspace/output/jimeng/`

**支持的模型：**
- `jimeng-3.0`（默认，推荐）
- `jimeng-2.1`
- `jimeng-2.0-pro`
- `jimeng-2.0`
- `jimeng-1.4`
- `jimeng-xl-pro`

### 2. jimeng_status - 检查服务状态

检查本地服务是否运行正常。

### 3. jimeng_start - 启动服务

启动 jimeng-free-api 本地服务。

### 4. jimeng_stop - 停止服务

停止本地服务。

### 5. jimeng_update_session - 更新 sessionid

当 sessionid 过期时更新配置。

**参数：**
- `sessionid` (string, 必需): 新的 sessionid

## 配置存储

配置文件位于：`~/.openclaw/workspace/skills/jimeng-ai/config.json`

```json
{
  "sessionid": "你的sessionid",
  "default_model": "jimeng-3.0",
  "output_dir": "~/.openclaw/workspace/output/jimeng/",
  "port": 8000
}
```

## 图片保存

生成的图片自动保存到配置目录，命名格式：
```
jimeng_{YYYYMMDD}_{HHMMSS}_{n}.png
```

## 使用示例

```python
# 生成一张图片
jimeng_generate(prompt="一只可爱的太空猫，卡通风格")

# 生成4张不同角度的图片
jimeng_generate(prompt="未来城市，赛博朋克风格", n=4)

# 指定输出目录
jimeng_generate(
  prompt="山水画，水墨风格",
  output_dir="~/Desktop/my-images/"
)
```

## 故障排查

**服务无法启动：**
- 检查端口 8000 是否被占用
- 查看日志：`tail -f ~/.openclaw/workspace/skills/jimeng-ai/server.log`

**生成失败：**
- 检查 sessionid 是否过期，使用 `jimeng_update_session` 更新
- 检查即梦AI账号积分是否充足

**图片未保存：**
- 检查输出目录是否存在且有写入权限
- 查看下载日志
