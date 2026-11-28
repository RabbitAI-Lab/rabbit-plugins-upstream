# flora-flow（花间搭配）

在花市拍几张摊位照片发给 AI 助手，它从 973 件真人插花作品里找一件「用到你看中那束花、其余花材这几个摊上也买得到」的作品，回一张并排图：左边是你的照片，框出要买的花；右边是作品。另附一行说明和一个结果页链接（完整购买清单）。

> **English.** An agent skill for flower markets. Send photos of the stalls; it picks a reference arrangement from a curated gallery of 973 works and frames, on your own photo, the flowers to buy for it. One side-by-side picture, one line of text and a link to the full shopping list. Works in WorkBuddy, Claude Code, Codex, OpenClaw and anything that runs `python3`; also speaks MCP.

## 安装

把整个文件夹放进助手的 skills 目录，或者让助手下载这三个文件：

```
https://flora.groundrl.com/skill/install/SKILL.md
https://flora.groundrl.com/skill/install/flora.py
https://flora.groundrl.com/skill/install/REFERENCE.md
```

需要 `python3`（3.8 起），不装任何依赖。验证：

```bash
python3 scripts/flora.py --version   # flora-flow 0.9.0
```

## 怎么用

新开对话，发 1–8 张花市照片。可以什么都不说，也可以说风格（「高贵一点」）或指一束（「第二张左边那桶粉色的」）。不满意就说「换一个」。

图上框的颜色按推荐强弱：

| 框 | 意思 |
|---|---|
| 红色粗实线 | 你看中的那束，已和作品对上 |
| 红色实线 | 去买 |
| 橙色虚线 | 同一种花，颜色相近，到摊上确认 |
| 灰色虚线 | 品种待核，到摊上确认 |

## 照片和数据

- 照片上传到 `flora.groundrl.com`，用于识别和匹配，**7 天后自动删除**；识别和查询记录（不含图片）保留 90 天。
- 脚本在本机 `~/.flora-flow` 生成一个随机 ID，作用相当于密码，只用来区分你的照片和结果。
- 每个 ID 每天最多 60 张照片、300 次查询。

## 版本

当前 0.9.0：作品里的点缀花也会给出位置；「去买」的花如果认花把握不足，改标灰色虚线「品种待核」。

## 许可

MIT No Attribution（MIT-0），见 `LICENSE`。
