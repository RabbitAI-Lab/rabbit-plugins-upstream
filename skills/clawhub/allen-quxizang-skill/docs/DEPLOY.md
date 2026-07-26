# 部署指南

## 一、OpenCode（原生支持）

```bash
# 将整个项目放到 ~/.claude/skills/ 下
cp -r quxizang-skill ~/.claude/skills/
# 在对话中触发: /去西藏
```

SKILL.md 已定义好触发词和行为规范，开箱即用。

## 二、Coze

1. **人设与回复逻辑**
   - Bot 设置 → 人设 → 将 `prompts/system_prompt_v2.md` 全文粘贴

2. **知识库**
   - 知识库 → 创建知识库 → 上传 `data/` 目录下所有 `.md` 和 `.json` 文件

3. **技能/触发器**
   - 设置触发词：`/去西藏` `/tibet-trip` `/xizang` `/西藏` `/进藏攻略`

## 三、Dify

1. **系统提示词**
   - 工作室 → 创建应用 → 提示词编排 → 将 `prompts/system_prompt_v2.md` 粘贴到 SYSTEM 框

2. **知识库**
   - 知识库 → 创建知识库 → 上传 `data/` 下所有文件

## 四、Claude Desktop / Claude Code

本技能原生支持 Claude — 将整个项目放入 `~/.claude/skills/allen-Quxizang-Skill/` 即可。SKILL.md 自动注册，对话中触发 `/去西藏` 即可。

如需单独配置：
1. 将 `prompts/system_prompt_v2.md` 内容粘贴到 Claude Project 的 System Prompt 框
2. `data/` 下所有文件上传为 Project Knowledge
3. 如需实时天气/路况，参照 `references/api-integration-guide.md` 配置免费 API

## 五、验证清单

部署完成后，用以下测试用例验证：

- [ ] 用户说"我想去西藏" → 触发病史筛查 → 给出阶梯进藏方案
- [ ] 用户说"我有高血压" → 调低海拔目标，给出高血压专项须知
- [ ] 用户说"纳木错" → 触发海拔熔断器评估，提前预警没吃的
- [ ] 用户说"甜茶去哪里喝" → 推荐光明港琼甜茶馆（藏民自营）
