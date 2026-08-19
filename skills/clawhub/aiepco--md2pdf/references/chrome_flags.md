# Chrome headless 打印 PDF 踩坑记录

## 环境

- macOS（Apple Silicon）
- Google Chrome 151.0.7922.138
- 路径：`/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`

## 关键 flag

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new \
  --disable-gpu \
  --no-sandbox \
  --run-all-compositor-stages-before-draw \
  --virtual-time-budget=2000 \
  --print-to-pdf=/path/out.pdf \
  --no-pdf-header-footer \
  file:///tmp/input.html
```

### flag 说明

| flag | 作用 | 是否必须 |
|:---|:---|:---|
| `--headless=new` | 新版 headless 模式（旧 `--headless` 已弃用） | 是 |
| `--disable-gpu` | macOS 下避免 GPU 初始化噪音/崩溃 | 推荐 |
| `--no-sandbox` | 部分环境必需，否则报 sandbox 错误 | 推荐 |
| `--run-all-compositor-stages-before-draw` | 确保图片/字体渲染完整再打印 | 推荐 |
| `--virtual-time-budget=2000` | 等待异步内容（字体/图）加载 | 推荐 |
| `--print-to-pdf=<path>` | 输出 PDF 路径 | 是 |
| `--no-pdf-header-footer` | 关闭默认页眉页脚（日期/页码/URL） | 可选 |

## 噪音日志 ≠ 失败

Chrome headless 在 macOS 会输出这些，**都是无害噪音，不是失败**：

```
ERROR:base/process/process_mac.cc:...
ERROR:task_policy_set.cc:...
```

**判断成功的唯一标准**：输出 PDF 文件存在且 `size > 0`。

## 退出码陷阱

Chrome 即使在**成功生成 PDF** 时也可能以**非零退出码**退出（macOS 噪音相关）。因此脚本里 `execFileSync` 抛错时不直接判失败，而是检查 PDF 文件是否存在且非空。

## 中文字体

- 优先 `PingFang SC`（macOS 系统自带，无需安装）
- 字体栈：`-apple-system, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei"`
- 代码块用 `SF Mono / Menlo / Consolas`

## 纸张

`--print-to-pdf` 默认 Letter。A4 需在 CSS 里设 `@page { size: A4; }`，脚本通过 `--paper` 参数控制（A4 时注入 `@page { size: A4; margin: 2cm; }`）。
