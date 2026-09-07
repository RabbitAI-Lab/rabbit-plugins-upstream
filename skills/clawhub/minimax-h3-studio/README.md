# MiniMax H3 Studio

中文视频创作 Skill，整合 H3 提示词编写与八种风格创作流程。

## 能力

H3 提示词、3D 动画短片、极简产品广告、品牌宣传、音乐 MV 与歌词动效、双人游戏开场、纸艺定格科普、纸拼贴讲解、手绘实拍融合。

## 使用

将完整目录复制到目标智能体的技能目录，名称保持 `minimax-h3-studio`。Codex 可安装到 `~/.codex/skills/minimax-h3-studio`，随后使用 `$minimax-h3-studio`。其他智能体读取 [SKILL.md](SKILL.md) 即可；`agents/openai.yaml` 仅为可选界面元数据。

示例：使用 `$minimax-h3-studio`，写一段小女孩和小怪兽在游乐场玩耍的三维动画提示词，角色独立描述，全部使用中文。

## 输出约定

- 提示词正文、标题与镜头描述统一中文，保留用户锁定原文。
- 每个角色独立成块，镜头通过名称引用，方便修改。
- 基础结构为「综合多模态描述」「整体声景」「画外配乐」。这些为本地译名，并非官方中文协议，尚未做中英标题生成效果对照测试。
- 默认 MiniMax-H3，不自动切换模型。实际接口需要英文字段时由提交适配层转换。

纯提示词编写不依赖网络、Codex、Hub 或外部 API。实际图片、视频、音频生成与合成需要目标环境具备相应工具；安装 Skill 不会安装模型或开通服务。

## 文档

- [统一入口](SKILL.md)
- [中文输出规范](references/中文输出规范.md)
- [移植说明](references/移植说明.md)
- [来源与版本](references/来源与版本.json)

## 来源与权利说明

本项目是本地中文整合与移植适配，非 MiniMax 官方发布。上游资料来自 [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3/tree/main/skills)，快照提交为 `d21241f0a4b3acbb34c97dae47fa417b7065e438`。保留原文、来源和校验信息，未为第三方资料另行授予许可；使用与再分发遵循上游适用条款。
