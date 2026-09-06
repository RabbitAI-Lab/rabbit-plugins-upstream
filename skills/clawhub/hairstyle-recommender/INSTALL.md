# 安装说明

## 快速安装

将本文件夹复制到 OpenClaw 的 skills 目录：

```bash
# macOS
mkdir -p ~/.kimi_openclaw/workspace/skills
cp -r hairstyle-recommender ~/.kimi_openclaw/workspace/skills/

# 重启 OpenClaw 或刷新 skills 列表即可生效
```

## 配置效果图生成功能（可选）

如果希望使用"基于真人照片生成换发型效果图"功能，需要配置 RunComfy API：

### 1. 注册 RunComfy 账号

访问 [runcomfy.com](https://www.runcomfy.com) 注册免费账号。

### 2. 获取 API Token

登录后进入个人中心 → API Keys → 复制 Token。

### 3. 设置环境变量

在启动 OpenClaw 的终端或配置文件中添加：

```bash
export RUNCOMFY_TOKEN="你的API Token"
```

如果无法修改环境变量，也可以在 skill 触发后，agent 会提示你输入 token，临时设置即可：

```bash
# 在当前会话中设置
export RUNCOMFY_TOKEN="ghp_xxxxxxxx"
```

### 4. 验证配置

上传一张人像照片并询问"推荐发型"，如果 agent 能生成效果图，说明配置成功。

## 文件说明

| 文件 | 说明 |
|------|------|
| `SKILL.md` | Skill 主定义文件，包含工作流程和触发词 |
| `references/hairstyles.md` | 发型知识库（脸型-发型匹配、剪法术语等） |
| `scripts/generate_hairstyle.py` | 效果图生成脚本（需配置 API Token） |
| `examples/` | 效果图示例 |
| `README.md` | 项目介绍 |

## 注意事项

- **API Token 安全**：请勿将 token 硬编码到代码中或提交到版本控制，始终通过环境变量注入
- **效果图精度**：AI 生成的效果图仅供参考，实际理发效果可能因发质、理发师技术等因素有所不同
- **网络要求**：使用效果图功能需要能访问 model-api.runcomfy.net

## 故障排除

### 提示"未设置 RUNCOMFY_TOKEN"

检查环境变量是否正确设置：
```bash
echo $RUNCOMFY_TOKEN
```

如果为空，请重新设置后重启 OpenClaw。

### 生成效果图时报 403/401 错误

API Token 可能过期或权限不足，请去 RunComfy 重新生成 Token。

### 发型没变 / 效果不理想

这是正常的 — Nano Banana 2 Edit 模型对精细的发型替换有局限，重点看整体方向（刘海、两侧长度、顶部纹理），具体细节需要和理发师沟通。
