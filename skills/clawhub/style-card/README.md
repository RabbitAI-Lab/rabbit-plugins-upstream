# style-card · 图生风格卡

把任何喜欢的图变成可复用的风格资产：**参考图 → 结构化风格卡 → 填槽生成同风格新图**。

一个 coding-agent skill（兼容任何有读图 + ImageGen + 文件系统能力的 agent，零外部依赖）。

## 它解决什么问题

- 看到好图只能说"哇好看"，说不出怎么做 → **风格卡**把风格拆成配色(hex)/构图线框/字体/槽位
- 市面"反推提示词"工具只输出一坨文本，不可复用 → 这里的卡是**槽位式模板 + 可积累的风格库**，越用越厚
- 反推的 prompt 不可信 → 每张卡必须经过**换内容闭环验证**（生成→对比→差异回写）才算 verified

## 目录结构（渐进加载）

```
style-card/
├── SKILL.md                     # 工作流地图：反推→验证→入库→复用
├── library/
│   ├── INDEX.json               # 风格库索引（紧凑元数据）
│   └── cards/*.md               # 风格卡正文（含可复制的生成prompt）
├── references/reverse-meta-prompt.md   # 图→风格卡 的反推模板
├── gotchas.md                   # 生图实战坑清单（持续回写）
└── examples/                    # 实际产出样例（换内容验证图 + HTML 引擎成品）
```

## 快速开始

给 agent 一句话即可：

- **反推**：「用 style-card 帮这张图做一张风格卡」+ 图片
- **复用**：「用我的风格卡库，把这段内容出成图：……」

内置 3 张已验证/待验证风格卡：复古印刷信息图（3:4 小红书）、手绘白板涂鸦（4:3 概念科普）、终端风封面（16:9）。

## 致谢

工作流设计借鉴了 [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) 的 progressive disclosure 与 show-don't-tell 理念。

## License

MIT
