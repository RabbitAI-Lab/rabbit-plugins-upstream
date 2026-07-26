┌─────────────────────────────────────────────────────────────────────────────┐
│                        content-writer Skill SOP                              │
│                        内容写作技能标准操作流程                                  │
└─────────────────────────────────────────────────────────────────────────────┘

┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│  触发    │───▶│  关键词  │───▶│  选题   │───▶│  生成   │───▶│  保存   │
│  Write   │    │ Keywords │    │ Topics  │    │ Generate │    │  Save   │
│  Article │    │          │    │         │    │          │    │         │
└──────────┘    └──────────┘    └──────────┘    └──────────┘    │/Feishu │
                                                                        └────┬─────┘
                                                                             │
                                                                             ▼
                                             ┌──────────────────────────────────────────┐
                                             │       Need images?                       │
                                             │         Y: Image Flow / N: Skip          │
                                             └────────────────┬───────────────────┘
                                                              │
                           ┌─────────────────────────────────────┘
                           ▼
                    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
                    │   风格选择   │───▶│  生成配图   │───▶│  自动裁剪   │
                    │    Style    │    │ Gen Images  │    │   Crop     │
                    └─────────────┘    └─────────────┘    └──────┬──────┘
                                                                 │
                                                                 ▼
                                                        ┌─────────────┐    ┌─────────────┐
                                                        │   排版确认   │───▶│   发布     │
                                                        │  Layout    │    │  Publish   │
                                                        └─────────────┘    └─────────────┘


═══════════════════════════════════════════════════════════════════════════════

对话流程（优化版）| Dialogue Flow (Optimized)
────────────────────────────────────────────────────────────────────────────

  步骤    助手问                                    用户答/操作
  Step    Ask                                        User Answer/Action
 ─────────────────────────────────────────────────────────────────────────────
  1       「你想写什么主题的文章？」               输入关键词
          "What topic do you want to write about?"   Enter keywords
  2       推荐选题，「你选哪个？」                 选择
          "Recommend topics, which one?"            Select
  3       「文章写好了，保存到哪里？」              本地/飞书/Obsidian
          "Where to save?"                          Local/Feishu/Obsidian
  4       「需要配图吗？」                         Y/N
          "Need images?"                            Y/N
  5       「你想用哪种风格？是否需要看一下示例图？」 选择 + 看示例
          "Which style? Want to see examples?"      Select + View
  6       「标题居中还是左对齐？配色用哪种？        选择
          可以提供RGB色号」                         
          "Title center or left? Color (RGB)?"      Select
  7       「一键复制/保存HTML/飞书发布？」          选择
          "Copy/HTML/Feishu?"                       Select


═══════════════════════════════════════════════════════════════════════════════

交互话术 | Interaction Scripts
────────────────────────────────────────────────────────────────────────────

• 确定写作方向 | Determine Writing Direction：
  「你想写什么主题的文章？输入关键词，比如：职场、副业、效率」
  "What topic? Enter keywords like: career, side hustle, efficiency"

• 热门选题 | Hot Topics：
  「根据热门内容，推荐以下选题，你选哪个？」
  "Based on trending topics, recommend these. Which one?"

• 保存文章 | Save Article：
  「文章写好了，保存到哪里？本地 / 飞书 / Obsidian？」
  "Done! Save to where? Local / Feishu / Obsidian?"

• 是否配图 | Need Images：
  「需要配图吗？」
  "Need images?"

• 选择风格 | Choose Style：
  「你想用哪种风格？是否需要看一下示例图？」
  "Which style? Want to see examples?"

• 排版确认 | Layout Confirmation：
  「标题居中还是左对齐？配色用哪种？可以提供RGB色号」
  "Title center or left? What color? Provide RGB code?"

• 发布 | Publish：
  「一键复制 / 保存HTML / 飞书发布？」
  "Copy / Save HTML / Publish to Feishu?"


═══════════════════════════════════════════════════════════════════════════════

文件结构 | File Structure
────────────────────────────────────────────────────────────────────────────

  ~/skills/content-writer/
  ├── SKILL.md              # 主技能文件 | Main skill file
  ├── SOP.md                 # 本流程图 | This flowchart
  ├── prompts.md            # 提示词模板 | Prompt templates
  ├── reference/
  │   ├── templates.md     # 文章模板 | Article templates
  │   └── styles.md        # 风格指南 | Style guide
  └── examples/            # 7张风格示例图 | 7 style example images
