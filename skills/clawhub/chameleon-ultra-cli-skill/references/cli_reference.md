# Chameleon Ultra CLI 命令参考 (chameleon_cli_main)

本参考整理自 RfidResearchGroup/ChameleonUltra 官方命令树（docs/cli.md、chameleon_cli_unit.py）。
chameleon_cli_main 是一个**交互式 REPL**，按功能分区组织命令：

- hw  —— 设备本身（连接、模式、版本、设置、卡槽）
- hf  —— 高频 / NFC（13.56MHz），如 ISO14443-A、MIFARE Classic
- lf  —— 低频 / 125kHz，如 EM410x、HID

通用提示
- 任何层级都可以加 -h / --help 查看该组命令与参数，例如 hw -h、hf mf -h、hw slot -h。
- 不同固件版本命令略有差异；以设备实际 *-h 输出为准。
- 本 skill 的 chameleon_control.py 会自动在每条命令前补 hw connect（除非 --no-connect），并在末尾补 exit。
- 需要等待卡片的命令（如 hf 14a scan、hf mf nested）可能耗时数秒到数十秒，可用 --timeout 调整上限。

---

## 根命令（REPL 控制）

| 命令 | 说明 |
|------|------|
| clear | 清屏 |
| rem (text) | 在输出中插入带时间戳的注释 |
| exit / quit / q | 退出 CLI 并断开设备 |
| dump_help | 列出所有命令（-d 显示描述，-g 按分组） |

---

## hw —— 设备控制

| 命令 | 参数 | 说明 |
|------|------|------|
| hw connect | -p PORT | 连接设备；自动检测失败时用 -p COM11（Windows）或 -p /dev/ttyACM0（Linux） |
| hw disconnect | — | 断开连接 |
| hw mode | -r(reader) / -e(emulator) | 获取 / 切换设备模式（读卡器 / 模拟器） |
| hw chipid | — | 读取芯片 ID |
| hw address | — | 读取蓝牙地址 |
| hw version | — | 读取固件版本与型号 |
| hw settings animation | -m (NONE\|MINIMAL\|...) | 设置 LED 动画（NONE 最隐蔽） |
| hw settings blekey | -k (key) | 修改 BLE 配对密钥（默认 12345，强烈建议修改） |
| hw settings | -h | 查看全部设备设置子命令 |

---

## hw slot —— 卡槽管理（最多 8 个，每个含 HF + LF）

| 命令 | 参数 | 说明 |
|------|------|------|
| hw slot list | — | 列出所有卡槽及状态 |
| hw slot type | -s (slot) -t (type) | 设置卡槽类型，如 MIFARE_1024 |
| hw slot init | -s (slot) -t (type) | 用指定类型的默认内容初始化卡槽 |
| hw slot enable | -s (slot) --hf / --lf | 启用某卡槽的 HF 或 LF 模拟 |
| hw slot disable | -s (slot) --hf / --lf | 禁用某卡槽的 HF 或 LF 模拟 |
| hw slot change | -s (slot) | 切换到指定卡槽（设为当前激活槽） |
| hw slot | -h | 查看其余子命令（nickname、delete 等） |

典型模拟流程（MFKEY32v2 示例）
```
hw connect
hw slot list
hw slot type   -s 8 -t MIFARE_1024
hw slot init   -s 8 -t MIFARE_1024
hw slot enable -s 8 --hf
hw slot change -s 8
hf mf econfig --enable-log
# 断开，去读卡器上刷几次卡，再连回：
hw connect
hf mf elog
hf mf elog --decrypt
hf mf econfig --disable-log
```

---

## hf —— 高频 / NFC（13.56MHz）

### hf 14a —— ISO14443-A

| 命令 | 说明 |
|------|------|
| hf 14a scan | 扫描 14a 标签，显示 UID / ATQA / SAK |
| hf 14a info | 扫描并做详细分析（猜测卡片类型、PRNG 强度等） |
| hf 14a | -h 查看读卡、raw 等子命令 |

### hf mf —— MIFARE Classic 攻击 / 操作

| 命令 | 参数 | 说明 |
|------|------|------|
| hf mf nested | --blk BLOCK -k KEY [--tblk TBLOCK] [-a\|-b] [--ta\|-tb] | Nested 攻击恢复密钥 |
| hf mf darkside | — | Darkside 攻击（0 扇区） |
| hf mf hardnested | --blk BLOCK -k KEY [--tblk TBLOCK] [--slow] [--keep-nonce-file] | HardNested 攻击（硬 PRNG） |
| hf mf elog | [--decrypt] | 查看 / 解密模拟器采集到的认证 nonce 日志 |
| hf mf econfig | --enable-log / --disable-log | 开启 / 关闭模拟器认证日志 |
| hf mf eload | (file) | 将 dump 文件载入当前模拟卡槽 |
| hf mf esave | (file) | 将当前模拟卡槽保存为 dump 文件 |
| hf mf chk | -k (keys) | 用给定密钥批量检测扇区 |
| hf mf rdbl / hf mf wrbl | 块读写（需先认证） | 读取 / 写入指定块 |
| hf mf | -h 查看全部子命令（cget/cset 等） |

---

## lf —— 低频 / 125kHz

### lf em 410x —— EM4100/EM410x（ID 卡）

| 命令 | 参数 | 说明 |
|------|------|------|
| lf em 410x scan | — | 扫描 EM410x 标签，显示 ID |
| lf em 410x write | --id (HEXID) | 将 EM410x 数据写入 T55xx 模拟槽 |
| lf em 410x | -h 查看其余子命令 |

### 其他 lf

- lf hid 等协议族：lf -h 查看完整列表（HID、T55xx、EM4x 等）。
- 模拟 EM410x：hw slot enable -s (slot) --lf 后配合 lf em 410x write --id ...。

---

## 使用建议

1. 先连接：几乎所有操作前都需要 hw connect（本 skill 默认自动补）。
2. 查帮助：不确定参数时，用 command-group -h 即时查看，例如 hw slot -h、hf mf nested -h。
3. 模拟 vs 读取：hw mode -e 进入模拟器模式、hw mode -r 进入读卡器模式；本 skill 多步命令建议在一个 chameleon_control.py 调用里连续下发，保证同一会话。
4. 等待类命令：hf 14a scan / hf mf nested 等会阻塞等待卡片或计算，按需调大 --timeout。
