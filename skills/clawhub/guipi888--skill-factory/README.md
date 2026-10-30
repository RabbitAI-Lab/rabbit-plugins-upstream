# 技能创建器·Skill Factory · WorkBuddy Skill

想把自己的方法论做成技能？想新建/安装/发布/更新一个 WorkBuddy 技能（skill）？技能创建器·Skill Factory（skill factory / skill builder / create skill）是全功能技能创建与发布工具：当用户说"新建技能""创建技能""帮我做个技能""写一个技能""发布技能"时触发。执行流程：①重叠评估（与现有技能扫描重叠度，给出整合/升级/新建三分支结论）→②安全检查（自动审计 SKILL.md 安全风险）→③创建/升级 SKILL.md→④自动发布到虾评+GitHub+ClawHub+SkillHub。v2.0 新增技能整合评估与一键发布集成。触发词：新建技能、创建技能、做个技能、发布技能、skill factory、create skill、build a skill。

## 解决什么问题

- 请参考 SKILL.md 中的详细说明

## 安装

### WorkBuddy 技能市场（推荐）

在 WorkBuddy 中搜索「技能创建器·Skill Factory」一键安装。

### 手动安装

```bash
git clone https://github.com/guipi888/skill-factory.git \
  ~/.workbuddy/skills/skill-factory
```

### 环境依赖

请参考 SKILL.md 中的环境要求章节

## 使用

```bash
python3 scripts/pipeline.py <参数>
```

详细参数请参考 SKILL.md

## 输出

请参考 SKILL.md

## 项目结构

```
.gitignore
_meta.json
LICENSE
LICENSE.txt
references
references\output-patterns.md
references\workflows.md
scripts
scripts\init_skill.py
scripts\package_skill.py
scripts\quick_validate.py
SKILL.md
```

## 关于作者

**桂皮 Guipi** — AI Agent 开发者 · 超级个体践行者
专注 AI 效率工具与一人公司方法论，帮普通人用 AI 成为超级个体

| 平台 | 账号 |
|------|------|
| 📱 小红书 | [桂皮AI实战](https://www.xiaohongshu.com/user/profile/5a409dda44363b313b9d7e15) |
| 🎬 抖音 | [桂皮AI实战](https://v.douyin.com/QJRjHGAtrvA/) |
| 📺 视频号 | 微信内搜「桂皮AI实战」 |
| 💬 公众号 | 微信搜「桂皮AI实战」 |
| 🌟 知识星球 | [AI超级个体](https://t.zsxq.com/guSUk) — AI工具 · 创作 · 产品 · 流量 · 变现 |
| 🐙 GitHub | [guipi888](https://github.com/guipi888) |
| 💬 微信 | guipi996（注明来意） |

## License

MIT License — 详见 [LICENSE](./LICENSE)
