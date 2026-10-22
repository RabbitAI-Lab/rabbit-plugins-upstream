# PowerShell 7 工具链 · 快速上手

给朋友的说明：把这个压缩包解压到任意目录，然后按下面做。

## 安装（1 条命令）

打开 **PowerShell**（开始菜单搜 PowerShell），粘贴：

```powershell
powershell -ExecutionPolicy Bypass -File ".\scripts\install.ps1"
```

它会自动完成：

- 安装 PowerShell 7（便携版，不需要管理员权限）
- 安装 Rust 高性能命令行工具：ripgrep(rg) / fd / fzf / bat / delta / jq
- 把中文输出乱码问题一次性根治（所有调用 PowerShell 的软件都受益）
- 把 pwsh 设成默认 shell（开始菜单快捷方式、右键 .ps1、Windows Terminal、VSCode）

**已经下载好安装包的话**（推荐，更快更稳）：

```powershell
powershell -ExecutionPolicy Bypass -File ".\scripts\install.ps1" -ZipPath "D:\下载\PowerShell-7.6.7-win-x64.zip"
```

不填 `-ZipPath` 时，它会在「下载 / 桌面 / 迅雷下载 / 文档」里自动找 `PowerShell-*-win-x64.zip`；找不到就自动从网上下（内置国内镜像加速）。

## 验证

```powershell
powershell -ExecutionPolicy Bypass -File ".\scripts\verify.ps1"
```

## 用起来

```powershell
pwsh -v                          # 应显示 7.x
rg -n "关键词" C:\某目录        # 极速检索（比 Select-String 快 10 倍以上）
```

## 卸载

删掉安装目录 `%LOCALAPPDATA%\ps7-toolkit`，再删掉注册表里这三项：

- `HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\pwsh.exe`
- `HKCU\Software\Microsoft\Classes\.ps1`
- `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced` 的 `DelegationConsole` 值

## 说明

- 所有安装都在**用户级**，不需要管理员，不写注册表 HKEY_LOCAL_MACHINE
- 重复执行安装器是安全的（幂等，只补缺失项）
- 想装到别的盘：加 `-ToolsRoot "D:\Tools\ps7"`
- 详细排错见 `references/troubleshooting.md`
