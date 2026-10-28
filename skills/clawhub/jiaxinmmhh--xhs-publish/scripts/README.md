# scripts 使用说明

这 7 个脚本是作者本机实测跑通的版本，**不是开箱即用**——里面有绝对路径和对本机环境的假设。用之前按下表改一遍。

## 运行环境（三个都要设）

```bash
export NO_PROXY='127.0.0.1,localhost'
export NODE_PATH=/path/to/node_modules        # 需要 puppeteer-core
NODE=/path/to/node                             # node 可执行文件绝对路径
```

`batch-drafts.sh` 顶部的 `NODE=` 是硬编码的，改它。各 `.js` 顶部的 `SHOT`（截图目录）也要改成自己存在的目录。

## 脚本清单

| 脚本 | 作用 | 用法 |
|---|---|---|
| `xhs-draft-ep.js` | 上传视频 + 填标题/正文/话题 + 原创 + 合集（不点保存） | `SERIES=xip EP=03 COLLECTION="合集名" NO_CHAPTER=1 node xhs-draft-ep.js` |
| `xhs-save-draft.js` | 在已填好的发布页上点「暂存离开」 | `EP=03 node xhs-save-draft.js` |
| `batch-drafts.sh` | 批量串起上面两个，逐期入库 | `SERIES=xip COLLECTION="合集名" zsh batch-drafts.sh 03 05 06` |
| `xhs-drafts-dump.js` | 读草稿箱列表 → `drafts.json` | `node xhs-drafts-dump.js` |
| `xhs-full-scan.js` | 服务端笔记（tab 0/1/2/3）+ 草稿箱 → `nm-now.json` / `drafts.json` | `node xhs-full-scan.js` |
| `xhs-coverage2.js` | 本地文案 vs 已发布 vs 草稿的覆盖矩阵 → `coverage2.json` | `node xhs-coverage2.js` |
| `xhs-fix-draft.js` | 打开已有草稿补原创/合集后存回 | `SERIES=xip EP=22 COLLECTION="合集名" node xhs-fix-draft.js` |

## 目录约定

脚本默认按这个结构找素材，不用这个结构就改脚本顶部的 `VIDEO` / `COPY` 路径：

```
{系列前缀}-ep{NN}/
  ├── output.mp4
  └── xhs-copy.txt      # 【标题】/【正文】/【话题标签】 或 ## 标题/## 正文/## 话题标签
```

## 两个必须知道的运行前提

1. **Chrome 要先开着调试端口** `--remote-debugging-port=9222`，并且已登录小红书创作服务平台。
2. **长任务一定要后台跑**。`batch-drafts.sh` 15 期约 25 分钟，前台跑会被工具超时打断，脚本半途死掉，留下半截状态。

## 别做的事

- ❌ 别 kill 这个调试 Chrome。草稿存在浏览器本地 IndexedDB，强杀重启可能全量归零。
- ❌ 别让脚本点「发布」。批量脚本化发布会被判「利用 AI 托管运营账号」。
- ❌ 别信单期耗时突然从 90 秒涨到 15 分钟时的日志——那是浏览器退化了，不是网络问题。
