---
name: chameleon-ultra-cli
description: "控制变色龙(Chameleon)Ultra 读写卡器，通过其 chameleon_cli_main 命令行程序操作设备。当用户想用命令行操作 Chameleon Ultra 设备时使用本技能：连接设备、扫描/读取高频(HF/NFC)或低频(LF)卡片、运行 MIFARE Classic 攻击(nested/darkside/hardnested)、管理模拟卡槽、载入/保存 dump、修改设备设置，或自动化任意 chameleon_cli_main 命令。本技能以非交互方式驱动交互式 REPL，并在首次配置后持久保存可执行文件路径。"
agent_created: true
---

# 变色龙 Ultra CLI 控制器

通过命令直接驱动 Chameleon Ultra 设备的 `chameleon_cli_main` 程序，无需在交互式
REPL 中手动敲命令。本技能把可执行文件包裹在伪终端(pseudo-terminal)中，从而可以脚本化
下发命令并可靠捕获输出（官方 CLI 是交互式的 `prompt_toolkit` REPL，在 Windows 上无法
通过管道输入来驱动）。

## 何时使用

只要用户想通过 CLI 对 Chameleon Ultra 做任何操作，就应使用本技能，包括但不限于：

- 连接 / 断开设备，读取固件版本、芯片 ID、设备模式
- 扫描或读取高频卡(ISO14443-A / NFC)或低频卡(EM410x / HID)
- MIFARE Classic 攻击：`nested`、`darkside`、`hardnested`、密钥恢复
- 管理模拟卡槽（类型、初始化、启用、切换、载入/保存 dump）
- 修改设备设置（LED 动画、BLE 配对密钥）
- 用户提到的任何其他 `chameleon_cli_main` 命令

## 首次配置（必需，仅一次）

可执行文件路径**无法预先获知**。在运行任何命令前，先确认是否已配置：

1. 运行辅助脚本的 `--show-config`。如果 `exe_path` 已设置且有效，则跳到下面的"运行命令"。
2. 如果尚未配置，向用户询问 `chameleon_cli_main` 的完整路径
   （例如 `C:\tools\chameleon\chameleon_cli_main.exe`）。
   使用 AskUserQuestion 工具询问；仅当用户之前提到过某个路径时，才提供合理的默认值。
3. 调用辅助脚本持久化保存：

   ```
   python SKILL_DIR/scripts/chameleon_control.py --set-exe "C:\path\to\chameleon_cli_main.exe"
   ```

   这会把 `exe_path` 保存到脚本同级的 `config.json` 中，之后所有运行都会复用该路径。

始终先检查 `--show-config`；如果路径已保存，不要重复询问用户。

## 运行命令

把用户的需求翻译成一条或多条 `chameleon_cli_main` 命令（命令树参见
`references/cli_reference.md`；设备上可用 command-group -h 查看精确的、与固件版本
对应的语法）。然后用辅助脚本运行，每条命令作为独立引号参数传入：

```
python SKILL_DIR/scripts/chameleon_control.py "hw connect" "hf 14a scan"
```

辅助脚本的关键行为：

- 会自动在命令前补 `hw connect`（除非加 `--no-connect`），并在末尾补 `exit`，
  因此每次调用都是一个全新的、可自行结束的会话。
- 多条命令在同一会话中顺序执行——把相关步骤（如卡槽设置 + 载入 + 启用）放在一次调用中。
- 需要等待卡片或计算的命令（如 `hf 14a scan`、`hf mf nested`）可能耗时较久，
  可用 `--timeout SECONDS` 调大上限（默认 120 秒）。
- `--file commands.txt` 会逐行运行文件中的命令（`#` 开头为注释）。
- `--raw` 保留 ANSI 转义码和回显输入；否则会对输出做清理以提升可读性。

示例——把一张 MIFARE dump 读入卡槽 8 并启用：

```
python SKILL_DIR/scripts/chameleon_control.py "hw slot type -s 8 -t MIFARE_1024" "hw slot init -s 8 -t MIFARE_1024" "hw slot enable -s 8 --hf" "hw slot change -s 8"
```

运行后，把捕获到的设备输出呈现给用户并据此处理（例如汇总扫描到的 UID、报告恢复出的密钥）。

## 依赖

在首次真正运行（非仅配置）时，辅助脚本会确保存在 PTY 后端：

- **Windows**：会在 `SKILL_DIR/.venv` 本地创建一个 venv 并安装 `pywinpty`
  （一次性，需要网络）。随后进程会用该解释器重新执行自身，无需手动安装。
- **POSIX**：使用标准库 `pty` 模块——无需安装。

若一次性的 `pywinpty` 安装失败（无网络），辅助脚本会清晰报错；恢复网络后重试即可。

## MIFARE 攻击方式速查

`chameleon_cli_main` 内置 5 种 MIFARE Classic 密钥攻击方式，各有适用场景。

| 攻击方式 | 核心原理 | 适用场景 |
|----------|----------|----------|
| Darkside（黑暗侧信道攻击） | 利用卡片在认证失败时返回的特殊错误信息（NACK）来逆向出密钥 | 完全不依赖任何已知密钥，可从零开始 |
| Nested（嵌套攻击） | 利用一个已知的扇区密钥去「偷听」并破解其他扇区的密钥 | 至少需要知道一个扇区的密钥 |
| StaticNested（静态嵌套攻击） | 嵌套攻击的一个变种，针对伪随机数生成器（PRNG）有缺陷的卡片 | 卡片生成随机数的规律较弱时 |
| Hardnested（硬嵌套攻击） | 嵌套攻击的「终极版」，不依赖卡片的随机数质量，仅凭一个已知密钥即可破解，但计算量巨大 | 卡片随机数质量很好，其他攻击无效时 |
| MFKEY32 v2 | 通常用于分析你之前「嗅探」到的刷卡数据，以计算出密钥 | 当你用 Chameleon 在「监听模式」下抓取过卡片与读卡器的通信数据时 |

对应 CLI 命令与典型用法：
- Darkside：`hf mf darkside`（0 扇区起手）
- Nested：`hf mf nested --blk BLOCK -k KEY --tblk TBLOCK [-a|-b] [--ta|-tb]`
- StaticNested：`hf mf nested` + 使用内置 `staticnested` 工具（`hf mf nested --static` 之类，因固件版本而异，先 `hf mf nested -h`）
- Hardnested：`hf mf hardnested --blk BLOCK -k KEY [--tblk TBLOCK] [--slow] [--keep-nonce-file]`
- MFKEY32 v2：先用 `hf mf econfig --enable-log` 开启认证日志，再用 Chameleon 模拟卡刷一次读卡器，下来后 `hf mf elog` / `hf mf elog --decrypt`

> 选择策略：先用 Darkside（无须已知密钥）；拿到一个密钥后再用 Nested 扩大战果；
> 遇到弱随机数卡直接 StaticNested；其他都失效时上 Hardnested（耗时可能数十分钟到数小时）。
> 监听到真实刷卡数据时优先 MFKEY32 v2。

## 注意事项

- 设备必须通过 USB 连接（或已通过 BLE 配对），`hw connect` 才能成功；
  在此之前离线命令都会失败。
- 每次辅助脚本调用都是独立的——调用之间没有持久会话。多步流程请放在同一次调用内。
- 固件版本不同命令略有差异；不确定某命令的参数时，可通过辅助脚本运行对应的
  command-group 帮助（如 `hw -h`）来查看设备实时的帮助信息。

### 排查指南

如果运行命令后**没有任何输出**（不报错也不显示设备提示符），按以下顺序排查：

1. **设备是否连上？** 先去 Windows 设备管理器确认看到 `USB Serial Device (COM3)`
   （VID_6868&PID_8686），再用 `--raw "hw version"` 看原始输出。
2. **换行符不执行？** `chameleon_cli_main` 基于 prompt_toolkit，其 REPL 只认
   `LF(\n)` 为「执行」键。`CR(\r)` 会被当成补全触发，表现为列出子命令菜单而非执行。
   辅助脚本已统一使用 `\n`，无需手动处理；但如果直接调试 winpty，注意这个区别。
3. **REPL 卡在终端查询？** prompt_toolkit 启动时会向终端发送能力查询
   （如 `\x1b[c` 设备属性查询、`\x1b[6n` 光标位置请求），必须收到应答才会渲染
   提示符。`chameleon_control.py` 已在读取线程中自动回写标准应答，无需手动干预。
   如果换了不同固件版本的 exe 且 prompt_toolkit 版本差异导致查询序列变化，可
   先用 `--raw` 抓取原始终端序列，对照 `respond_to_queries()` 补新的应答。
4. **标准 python 调用丢输出？** 若通过 `python chameleon_control.py` 调用返回空输出，
   检查是否走了 `os.execv` 重执行路径（老版本有此问题，已修复为 `subprocess.run`）。
   仍不行时直接用技能目录 `.venv/Scripts/python.exe` 运行脚本，绕过 bootstrap。
