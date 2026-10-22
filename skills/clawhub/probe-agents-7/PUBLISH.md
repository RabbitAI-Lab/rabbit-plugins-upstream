# 技能发布材料 · PowerShell 7 工具链

> 面向 WorkBuddy 开放平台（open.workbuddy.cn）的技能提交表单预填稿。
> 表单里每一项都可直接照抄。

---

## 一、基础信息

| 表单项 | 填写内容 |
|---|---|
| 技能名称 | `PowerShell 7 工具链` |
| 英文名称 | `PowerShell 7 Toolkit` |
| 技能标识（slug） | `powershell7-toolkit` |
| 版本号 | `1.1.0` |
| 作者 / 发布者 | 欣欣（YUJIANYU） |
| 许可证 | MIT |
| 分类 | `development`（开发工具）；备选 `utility`（效率工具） |
| 部署地域 | Global |
| 计费方式 | **Free**（免费技能，不涉及结算与实名签约） |
| 是否需要第三方 API Key | **否** |

### 技能图标

`assets/icon.png` — 512×512 PNG，深色终端风格，蓝色 `>` 提示符 + 白色 `7` + `utf-8` 标签。

---

## 二、技能描述（市场卡片上显示，约 133 字）

**中文：**

> 在 Windows 上部署 PowerShell 7 与 Rust 高性能命令行工具链（ripgrep / fd / fzf / bat / delta / jq），根治中文输出乱码，并把 pwsh 设为系统默认 shell。跨机器自包含、幂等、免管理员、断网可装。

**English:**

> Deploys PowerShell 7 and the Rust high-performance CLI toolchain (ripgrep / fd / fzf / bat / delta / jq) on Windows, fixes Chinese mojibake in shell output, and makes pwsh the default shell. Self-contained, idempotent, no admin rights required, works offline.

---

## 三、触发场景（写进 description 的 Use when，供 AI 判断何时调用）

1. 用户要求安装 / 升级 PowerShell 7 或 pwsh
2. 用户抱怨命令行中文乱码、编码报错、TLS 连不上 GitHub、PowerShell 跑得慢
3. 用户想在 Windows 上做高速文本检索（提到 rg / ripgrep / 检索太慢 / Select-String 太慢）
4. 用户要求把 PowerShell 设为系统默认

**与现有技能的区分：**

- `win-powershell` —— 只讲 5.1 的命令书写规范，不负责安装与部署。
- 本技能 —— 负责完整的探测、下载、安装、默认化、体检闭环。

---

## 四、权限声明（务必如实填写，审核重点）

### 需要的权限

| 权限 | 用途 | 是否可关闭 |
|---|---|---|
| 用户级文件写入 | `%LOCALAPPDATA%\ps7-toolkit`（安装目录） | 是（`-ToolsRoot` 可改路径） |
| 用户级注册表写入 | `HKCU` 下的 PATH / App Paths / `.ps1` 关联 / 默认控制台 | 是（`-SkipDefaults` 跳过） |
| 用户 profile 文件追加 | PowerShell 7 与 5.1 的 `Microsoft.PowerShell_profile.ps1` | 是（同上） |
| 网络访问（安装阶段） | `api.github.com`、`github.com`、`gh-proxy.com`、`ghfast.top`、`ghproxy.net`、`aka.ms` | 否（断网时走本地 zip 或内置版本表） |
| 文件关联 | `.ps1` 双击行为 | 是 |

### 明确不做的事（可在表单中声明，有助于过审）

- **不需要管理员权限**，全程用户级安装。
- **不写 `HKEY_LOCAL_MACHINE`**。
- **不修改系统区域设置**（不改 `HKLM\...\Nls\CodePage\ACP`），因此不会破坏老的 GBK 程序。
- **不劫持 `powershell.exe`** 指向 pwsh，系统组件兼容性不受影响。
- **不收集用户数据、不上报统计、不请求任何 API Key**。
- 脚本内**无硬编码凭证**。

### 数据流向

仅在需要下载安装包时向 GitHub / 微软官方短链 / 国内镜像发起 GET 请求下载公开二进制。无任何出站遥测。

---

## 五、使用说明（提交表单的「使用方法」栏）

### 给终端用户

1. 打开 PowerShell，执行：
   ```powershell
   powershell -ExecutionPolicy Bypass -File ".\scripts\install.ps1"
   ```
2. 重启终端 / 常用应用（PATH 才会刷新）。
3. 验证：`pwsh -v` 显示 7.x；`rg --version` 显示 ripgrep。

### 给 AI 助手

直接调用 `scripts/install.ps1` 完成部署，然后用 `scripts/verify.ps1` 体检；装完之后按 SKILL.md「三、日常使用规范」执行：

- 命令用 `pwsh` 跑，复杂脚本写成 `.ps1` 文件再 `-File` 执行（避免 `-Command` 内联引号被拆散）
- 文本检索用 `rg`，不用 `Select-String`（实测快 11 倍）
- 给 5.1 跑的 `.ps1` 存成 UTF-8 with BOM

### 常用参数

| 参数 | 说明 |
|---|---|
| `-ZipPath` | 指定本地安装包，跳过自动搜索 |
| `-ToolsRoot` | 自定义安装根目录（默认 `%LOCALAPPDATA%\ps7-toolkit`） |
| `-Mirror` | 自定义下载镜像，插到内置列表最前 |
| `-SkipDefaults` | 只装不配，不动系统默认 |
| `-SkipRustTools` | 只装 PowerShell 7 |
| `-CheckOnly` | 只体检，无任何改动 |
| `-Force` | 强制重装 |

---

## 六、已知风险与缓解措施

| 风险 | 缓解 |
|---|---|
| 安装脚本会修改用户 PATH 与注册表默认项 | 全部限定在 `HKCU` 与用户目录；`-SkipDefaults` 可完全跳过；SKILL.md 第八节逐项列出改动点与撤销方式 |
| 通过第三方镜像下载二进制 | 优先走官方 `api.github.com` 取真实下载地址与官方 `aka.ms` 短链；镜像仅作国内加速回退；用户可用 `-Mirror` 指定自有源 |
| 关联 `.ps1` 双击直接执行 | 仅改 `HKCU\Software\Microsoft\Classes\.ps1`，删键即可还原；默认行为仍受系统执行策略约束 |
| 卸载需手动操作 | README 与 SKILL.md 均给出：删目录 + 删 3 个注册表项 |

---

## 七、发布前自检清单

- [x] SKILL.md frontmatter 含 `name` / `description`，`name` 为 kebab-case
- [x] 含 `agent_created: true`
- [x] 含 `display_name` / `display_name_en` / `description_zh` / `description_en`
- [x] 描述长度 133 字，落在 100–300 区间
- [x] 512×512 PNG 图标就位
- [x] CHANGELOG.md 存在
- [x] 目录不含 `.git` / `LICENSE` / `.DS_Store`
- [x] 无硬编码凭证、无混淆代码
- [x] 官方 `quick_validate.py` 校验通过
- [x] 行为与风险如实声明
- [x] `clawhub skill publish --dry-run` 通过

---

## 八、两条发布路径

| 路径 | 入口 | 审核 | 备注 |
|---|---|---|---|
| **SkillHub** | `clawhub skill publish ./ps7-toolkit --slug powershell7-toolkit` | 平台自动安全扫描 | 需 `clawhub login`；发布后可在 SkillHub 分区搜到 |
| **开放平台** | https://open.workbuddy.cn | 人工审核 1–3 工作日 | 需开发者注册 + 资质认证；可设置免费/付费；上架后进入「推荐」分区 |

两条路径都需要发布者本人账号，因此最后一步必须由小主本人操作。
