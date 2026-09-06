# Hairstyle Recommender

一个 AI 驱动的发型推荐 Skill，通过分析人像照片，根据脸型、五官、发质等因素推荐最适合的发型，并支持基于真人照片生成换发型后的效果图。

## 功能

- 📸 **人像分析**：分析脸型、五官比例、发质发量等特征
- 💇 **智能推荐**：为男性和女性用户提供个性化发型建议
- 📝 **剪法指南**：提供详细的理发师沟通话术
- 🎨 **效果图生成**：基于真人照片，使用 AI 局部编辑生成换发型后的效果图

## 适用场景

- 想换发型但不知道适合什么风格
- 需要给理发师提供明确的剪发要求
- 根据脸型和发质获取专业建议
- 想预览某款发型在自己头上的效果

## 文件结构

```
hairstyle-recommender/
├── SKILL.md                  # Skill 主文件（工作流程 + 使用说明）
├── README.md                 # 项目说明
├── references/
│   └── hairstyles.md         # 发型知识参考库
└── scripts/
    └── generate_hairstyle.py # 效果图生成脚本（需配置 RunComfy API Token）
```

## 安装

```bash
# 1. 将 skill 文件夹复制到 OpenClaw skills 目录
cp -r hairstyle-recommender ~/.kimi_openclaw/workspace/skills/

# 2. （可选）配置效果图生成功能
# 在 https://www.runcomfy.com 注册并获取 API Token
export RUNCOMFY_TOKEN="你的token"
```

## 使用方法

### 作为 OpenClaw Skill

当用户上传人像照片并询问发型建议时，Skill 会自动触发，按以下流程执行：

1. 分析人像特征（脸型、五官、发质等）
2. 查阅发型知识库
3. 输出推荐报告（含剪法说明）
4. 可选：生成效果图

### 单独使用效果图生成脚本

```bash
# 基础用法（使用默认 Mid Fade + 碎盖头提示词）
python3 scripts/generate_hairstyle.py ~/photo.png ~/Desktop/效果图.png

# 自定义发型描述
python3 scripts/generate_hairstyle.py ~/photo.png ~/Desktop/效果图.png \
  "Change only the hairstyle to a short textured fringe..."
```

## 前置条件（效果图功能）

| 项目 | 说明 |
|------|------|
| RunComfy 账号 | 在 [runcomfy.com](https://www.runcomfy.com) 免费注册 |
| API Token | 从个人中心获取，通过环境变量 `RUNCOMFY_TOKEN` 注入 |
| Python 3 | 系统自带或自行安装 |

> ⚠️ **安全提示**：`RUNCOMFY_TOKEN` 仅通过环境变量读取，不会写入任何文件。请勿将 token 硬编码到代码中或提交到版本控制。

## License

MIT
