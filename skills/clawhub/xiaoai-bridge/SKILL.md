---
name: xiaoai-bridge
description: 小米小爱音箱语音指令桥接。截取小爱音箱的语音消息，转换为 AI 助手指令，并通过 TTS 回复。支持触发词过滤、自动去重、后台监听。适用于通过小爱音箱语音控制 OpenClaw 助手、智能家居联动、语音任务执行等场景。
version: 1.2.4
author: warm-winter
license: MIT-0
tags: [xiaomi, xiaoai, voice, tts, iot, smart-home]
allowed-tools: read, write, exec, env
metadata:
  openclaw:
    emoji: 🔉
    homepage: https://clawhub.ai/warm-winter/skills/xiaoai-bridge
    primaryEnv: MI_PASS_TOKEN
    requires:
      env:
        - MI_USER_ID
        - MI_DEVICE_ID
      bins:
        - node
      config:
        - scripts/.env
    envVars:
      - name: MI_PASS_TOKEN
        required: false
        description: 推荐登录凭据，与 MI_PASSWORD 二选一；等同小米账号密码，勿提交。
      - name: MI_PASSWORD
        required: false
        description: 备选登录方式，可能触发验证码与风控，仅用于无法获取 passToken 时。
      - name: TRIGGER_PREFIX
        required: false
        description: 触发词前缀，默认“请”；只处理以此开头的语音消息。
      - name: XIAOAI_ALLOW_UNFILTERED
        required: false
        description: 设为 true 才允许空 TRIGGER_PREFIX（处理所有语音消息）。
      - name: POLL_INTERVAL
        required: false
        description: 轮询间隔毫秒，默认 1000，范围 500-60000。
      - name: XIAOAI_STATE_DIR
        required: false
        description: 会话缓存目录；默认使用当前用户的私有状态目录。
      - name: XIAOAI_ALLOW_INSECURE_STATE_DIR
        required: false
        description: 仅在权限无法强制/ACL 无法验证时显式放行（存在凭据泄露风险）；必须在进程环境中设置，写在 .env 中会被忽略。
      - name: XIAOAI_ENV_FILE
        required: false
        description: 指定 .env 文件路径，默认 scripts/.env 或技能根目录 .env。
      - name: DEBUG
        required: false
        description: 设为 true 输出调试信息到 stderr。
      - name: PRINT_TRANSCRIPTS
        required: false
        description: 仅 debug-fetch.js：设为 true 才打印语音转写原文。
---

# 小爱音箱语音桥接 Skill

通过小米小爱音箱实现 OpenClaw 的语音交互能力。

## 功能特性

- ✅ **语音指令监听** - 实时轮询小爱音箱的语音消息（小米云端语音识别）
- ✅ **智能触发过滤** - 支持触发词前缀（默认“请”），避免误触发
- ✅ **TTS 语音回复** - 将 AI 处理结果通过小爱音箱播报
- ✅ **消息去重机制** - 自动跟踪时间戳，避免重复处理
- ✅ **后台持续运行** - 支持长期监听，自动退避重连
- ✅ **多设备支持** - 支持所有小米 IoT 生态的小爱音箱设备
- ✅ **凭据缓存隔离** - 会话缓存写入经校验的私有目录，权限不符时拒绝启动

## 工作原理

1. **监听** - 轮询小爱音箱获取语音消息（小米云端语音转文字）
2. **处理** - 将语音消息转换为 AI 助手指令
3. **回复** - 通过小爱音箱 TTS 播报处理结果

消息以 JSON 行写入 stdout，状态和错误写入 stderr，方便被其他进程直接消费。

## 安全模型（请先阅读）

`passToken` 等价于小米账号的登录凭据，能读取设备列表、对话记录并控制音箱。请按以下方式使用：

1. **使用专用账号**：不要用主账号；在小米账号设置中限制授权范围。
2. **优先使用 passToken**：密码登录可能触发验证码，且更容易被风控。
3. **会话缓存**：依赖库 `@mi-gpt/miot` 会把包含 `passToken` / `serviceToken` / `ssecurity` 的 `.mi.json` 写到**进程当前目录**。本 Skill 会在登录前把工作目录切换到私有状态目录，并强制校验：
   - 默认目录不再使用共享临时目录，而是当前用户的状态目录（见下表）；
   - 目录必须是真实目录（拒绝符号链接）、属主必须是当前用户（POSIX）、权限收紧到 `0700` 并复验（只自动修改“空目录或仅含 `.mi.json`”的专用目录，不会擅自改 `$HOME`）；
   - Windows 上公共目录/其他用户 profile（`C:\Users\Public`、`C:\Windows\Temp`、`C:\ProgramData`、`C:\Users\<他人>`）一律拒绝；
   - 缓存文件在登录前以 `0600` 独占预创建，并清理未知顶层键与 `__proto__`；登录后复验类型、属主、权限、硬链接（含 NTFS）、非空内容与 `dev/ino`；
   - 任何一项不满足都会**中止运行并以退出码 2 退出**，不会把凭据写入可疑目录；
   - 可用 `node scripts/xiaoai-listen.js check` 做本地检查（不登录、不使用凭据；会加载 `.env` 读取 `XIAOAI_STATE_DIR`，目录不存在时按 0700 创建）。
4. **不要提交凭据**：`.env`、`.mi.json` 不要提交；源码目录带有 `.gitignore`，安装到其他项目后请把这两类文件加入你自己的忽略规则，发布或分享前用 `git status` 确认没有包含。
5. **用完即清**：运行 `node scripts/xiaoai-listen.js clean` 删除本地会话缓存（同时清理旧版本可能遗留的 `.mi.json`）。删除本地缓存**不等于撤销凭据**，如怀疑泄露请退出小米账号所有登录并更换 passToken。
6. **日志边界**：监听模式默认只把语音转写发给 stdout 的消费方；`debug-fetch.js` 默认不打印转写原文。stdout 含语音内容，**不要重定向到日志文件**。stderr 日志会经过脱敏（Cookie、passToken、serviceToken、ssecurity 等），但脱敏是尽力而为，仍不要长期落盘。
7. **权限最小化**：以专用、非特权系统账号运行，只给它需要的环境变量。
8. **高危动作需确认**：本 Skill 只负责“语音 → 文本 → TTS”，不执行具体动作。消费方应先确认再执行不可逆或有后果的操作（删除/清空数据、支付转账、解锁门锁、关闭安防、批量控制设备等），并把确认结果播报给用户。
9. **网络边界**：运行时只通过锁定版本的 `@mi-gpt/miot` 访问小米账号/设备接口，不下载也不执行远程代码，不发送遥测数据。

### 默认会话缓存目录

| 平台 | 默认目录 |
|------|----------|
| Windows | `%LOCALAPPDATA%\xiaoai-bridge` |
| macOS | `~/Library/Application Support/xiaoai-bridge` |
| Linux 等 POSIX | `$XDG_STATE_HOME/xiaoai-bridge`（绝对路径），否则 `~/.local/state/xiaoai-bridge` |

需要放到别处时显式设置 `XIAOAI_STATE_DIR`，但该目录同样必须通过上述属主/权限校验。

如果 `passToken` 曾经被提交到公开仓库，请立刻在小米账号中退出所有登录、修改密码，并重新获取 passToken。

## 快速开始

> 以下命令均在技能根目录（`skills/xiaoai-bridge/`）执行。

### 1. 安装依赖

```bash
cd skills/xiaoai-bridge/scripts
npm ci --registry=https://registry.npmjs.org/
cd ..
```

`npm ci` 会严格按 `package-lock.json` 安装并校验完整性；lock 中所有依赖都指向 HTTPS 官方地址。若本机 npm 配置了其他镜像，`--registry` 可确保不会回落到明文 HTTP 源。

发布包不包含 `node_modules/`（由 `.clawhubignore` 排除，避免安全扫描器无法完整分析依赖产物），因此**必须**先执行这一步。

### 2. 配置环境变量

```bash
cp scripts/env.example scripts/.env
chmod 600 scripts/.env   # POSIX 系统建议执行
```

编辑 `scripts/.env`：

```bash
MI_USER_ID=1234567890              # 小米账号 ID（纯数字）
MI_PASS_TOKEN=your_pass_token      # 推荐：使用 passToken
# MI_PASSWORD=your_password        # 备选：密码（可能触发安全验证）
MI_DEVICE_ID=小爱音箱Pro            # 设备名称、miotDID 或 MAC 地址
TRIGGER_PREFIX=请                   # 触发词前缀（默认“请”）
POLL_INTERVAL=1000                 # 轮询间隔（毫秒，默认 1000）
```

- **获取 passToken**：参考 https://github.com/idootop/migpt-next/issues/4
- **查找设备 ID**：运行 `DEBUG=true node scripts/xiaoai-listen.js test`，调试输出会列出设备名称、miotDID 与 MAC。
- `.env` 加载顺序是 `scripts/.env` → 技能根目录 `.env`；也可以用 `XIAOAI_ENV_FILE` 指定任意路径。POSIX 下若 `.env` 可被同组/其他用户读取，CLI 会告警并尽力收紧到 `0600`。

### 3. 检查运行环境

```bash
node scripts/xiaoai-listen.js check
```

该命令只做本地检查（不登录、不使用凭据），输出会话缓存目录、目录权限、缓存文件状态与旧版遗留缓存；发现问题时退出码为 2。若目录尚不存在，会按 0700 创建（不含凭据）；若使用了不安全开关放行，仍会返回 2 并标注“不安全”。

### 4. 测试连接

```bash
node scripts/xiaoai-listen.js test
```

预期输出（stderr）：

```text
🔌 正在连接小爱音箱...
✅ 连接成功
🔐 缓存文件校验通过：0600
✅ 连接测试通过
```

> Windows 上文件模式不受 POSIX 权限位控制，日志中的 `0666` 仅供参考；目录仍受“必须位于当前用户目录内”的策略保护。

### 5. 启动监听

```bash
node scripts/xiaoai-listen.js
```

stdout 只会输出 JSON 行，例如：

```json
{"type":"message","text":"查一下天气","originalText":"请查一下天气","timestamp":1708070400000}
```

后台运行（**不要把 stdout 写入文件**，其中包含语音转写）：

```bash
node scripts/xiaoai-listen.js 2> xiaoai.err &
```

或使用 OpenClaw 进程管理（推荐），由消费方通过管道读取 stdout。

### 6. 清理缓存

```bash
node scripts/xiaoai-listen.js clean
```

会清理当前状态目录的缓存（仅当该目录为空时才删除目录本身），以及旧版本可能遗留的 `scripts/.mi.json`、技能根目录 `.mi.json`、当前目录 `.mi.json` 和旧临时目录缓存。legacy 位置只删除“内容像小米会话缓存”的文件，不会删除目录；遇到符号链接目录或无法判定/清理失败时返回非 0。

## 使用示例

> 以下示例都把语音文本作为**参数数组**传给子进程，不经过 shell，因此引号、分号、反引号等字符不会被解释执行。

### 示例 1：后台监听 + 消息处理

```javascript
const { execFile } = require('node:child_process');
const path = require('node:path');

const scriptPath = path.join(__dirname, 'skills/xiaoai-bridge/scripts/xiaoai-listen.js');
const listener = execFile(process.execPath, [scriptPath], {
  maxBuffer: 1024 * 1024,
});

let buffer = '';
listener.stdout.on('data', (chunk) => {
  buffer += chunk;
  const lines = buffer.split('\n');
  buffer = lines.pop() ?? '';

  for (const line of lines) {
    if (!line.trim()) continue;
    try {
      const msg = JSON.parse(line);
      if (msg.type === 'message') {
        handleVoiceCommand(msg.text);
      }
    } catch (error) {
      console.error('无法解析的监听输出:', line);
    }
  }
});

listener.stderr.on('data', (chunk) => {
  console.error('XiaoAi:', chunk.toString().trim());
});

async function handleVoiceCommand(text) {
  // 高危动作先向用户确认，再执行；不要把转写写入日志文件。
  const response = await processCommand(text);
  await speak(response);
}
```

### 示例 2：直接 TTS 播报

```bash
node scripts/xiaoai-listen.js speak "任务已完成"
```

代码调用：

```javascript
const { execFile } = require('node:child_process');
const path = require('node:path');

const scriptPath = path.join(__dirname, 'skills/xiaoai-bridge/scripts/xiaoai-listen.js');

function speak(text) {
  return new Promise((resolve, reject) => {
    execFile(process.execPath, [scriptPath, 'speak', text], (error) => {
      if (error) reject(error);
      else resolve();
    });
  });
}

await speak('你好，任务已完成');
```

`speak` 的文本上限是 1000 字符，超出会以配置错误退出（退出码 2）。

### 示例 3：触发词过滤

Skill 自动过滤触发词前缀（默认“请”），只处理符合条件的消息：

```javascript
// 用户说："请帮我查天气" → 处理，text = "帮我查天气"
// 用户说："今天天气怎么样" → 忽略（无触发词）
```

自定义触发词（在 `.env` 中配置）：

```bash
TRIGGER_PREFIX=请        # 默认
# TRIGGER_PREFIX=小助手   # 自定义唤醒词
```

如果确实想处理所有语音消息，必须显式开启：

```bash
TRIGGER_PREFIX=
XIAOAI_ALLOW_UNFILTERED=true
```

### 示例 4：完整集成

```javascript
const { execFile } = require('node:child_process');
const path = require('node:path');

class XiaoAiBridge {
  constructor(scriptPath) {
    this.scriptPath = scriptPath;
    this.listener = null;
    this.buffer = '';
    this.lastTimestamp = Date.now();
  }

  start(onMessage) {
    this.listener = execFile(process.execPath, [this.scriptPath], {
      maxBuffer: 1024 * 1024,
    });

    this.listener.stdout.on('data', (chunk) => {
      this.buffer += chunk;
      const lines = this.buffer.split('\n');
      this.buffer = lines.pop() ?? '';

      for (const line of lines) {
        if (!line.trim()) continue;
        try {
          const msg = JSON.parse(line);
          if (msg.type === 'message' && msg.timestamp > this.lastTimestamp) {
            this.lastTimestamp = msg.timestamp;
            onMessage(msg.text);
          }
        } catch (error) {
          console.error('无法解析的监听输出:', line);
        }
      }
    });

    this.listener.stderr.on('data', (chunk) => {
      console.error('XiaoAi Error:', chunk.toString().trim());
    });
  }

  speak(text) {
    return new Promise((resolve, reject) => {
      execFile(process.execPath, [this.scriptPath, 'speak', text], (error) => {
        if (error) reject(error);
        else resolve();
      });
    });
  }

  stop() {
    if (this.listener) {
      this.listener.kill();
      this.listener = null;
    }
  }
}
```

> 注：`start()` 会把原始语音文本交给 `onMessage`，消费方应自行决定是否落盘（默认不要）。

## 消息格式

监听器输出的每条 stdout 行都是一个独立 JSON 对象：

```json
{
  "type": "message",
  "text": "查一下天气",
  "originalText": "请查一下天气",
  "timestamp": 1708070400000
}
```

- `text`：已去除触发词前缀、首尾空白后的指令。
- `originalText`：音箱识别到的原始文本。
- `timestamp`：消息时间（毫秒）。
- 同一轮轮询到的多条消息会按时间从旧到新依次输出，不会漏掉其中较早的消息。

## API 参考

完整 MiGPT-Next API 文档见 [references/migpt-api.md](references/migpt-api.md)。

### 脚本命令

```bash
# 启动监听（默认）
node scripts/xiaoai-listen.js

# TTS 播报文本
node scripts/xiaoai-listen.js speak "要说的话"

# 测试连接
node scripts/xiaoai-listen.js test

# 检查缓存目录/文件权限（不联网、不登录、不输出凭据）
node scripts/xiaoai-listen.js check

# 清理本地会话缓存（含旧版本遗留位置）
node scripts/xiaoai-listen.js clean

# 调试：查看最近对话（默认隐藏转写原文）
node scripts/debug-fetch.js
PRINT_TRANSCRIPTS=true node scripts/debug-fetch.js

# 帮助 / 版本
node scripts/xiaoai-listen.js --help
node scripts/xiaoai-listen.js --version
```

## 环境变量

| 变量 | 必需 | 说明 |
|------|------|------|
| `MI_USER_ID` | 是 | 小米账号 ID（纯数字，不是手机号或邮箱） |
| `MI_PASS_TOKEN` | 是* | passToken（推荐） |
| `MI_PASSWORD` | 是* | 密码（可能触发安全验证） |
| `MI_DEVICE_ID` | 是 | 设备名称、miotDID 或 MAC |
| `TRIGGER_PREFIX` | 否 | 触发词前缀（默认“请”） |
| `XIAOAI_ALLOW_UNFILTERED` | 否 | 设为 `true` 才允许空 `TRIGGER_PREFIX` |
| `POLL_INTERVAL` | 否 | 轮询间隔（毫秒，默认 1000，范围 500-60000） |
| `DEBUG` | 否 | 调试模式（true/false） |
| `XIAOAI_STATE_DIR` | 否 | 会话缓存目录（默认见“默认会话缓存目录”） |
| `XIAOAI_ALLOW_INSECURE_STATE_DIR` | 否 | **有风险**：仅当权限无法强制/ACL 无法验证时显式放行；必须在进程环境中设置（`.env` 中会被忽略）；不会绕过符号链接、属主不符、公共目录、硬链接等硬性检查，且 `check` 仍返回退出码 2 |
| `XIAOAI_ENV_FILE` | 否 | 指定 `.env` 文件路径 |
| `PRINT_TRANSCRIPTS` | 否 | 仅 `debug-fetch.js`：设为 `true` 打印转写原文 |

\* `MI_PASS_TOKEN` 或 `MI_PASSWORD` 二选一。

## 输出与退出码

| 场景 | stdout | stderr | 退出码 |
|------|--------|--------|--------|
| 监听模式 | 仅 JSON 行 | 状态、错误 | 0 正常退出；1 运行失败 |
| `speak` / `test` | 无（调试日志除外） | 状态、错误 | 0 成功；1 连接失败 |
| `check` | 检查报告 | — | 0 通过；2 需要处理 |
| 配置/权限错误 | 空（`clean`/`check` 除外） | 配置错误说明 | 2 |
| `--help` / `--version` / `clean` | 文本 | 无 | 0（`clean` 清理失败为 2） |

## 故障排查

### 登录失败

症状：`❌ 连接失败: 登录失败`

解决方案：

1. 使用 passToken 替代密码（推荐）
2. 检查 `MI_USER_ID` 是否为纯数字（不是手机号或邮箱）
3. 开启 `DEBUG=true` 查看详细错误信息

### 会话缓存目录校验失败

症状（stderr）中出现以下之一：

- `会话缓存目录属于其他用户…拒绝把凭据写入该目录`
- `无法把会话缓存目录权限收紧到 0700…`
- `会话缓存目录不能是符号链接…`
- `会话缓存目录不在当前用户目录内，无法验证访问控制…`
- `会话缓存目录位于公共目录或其他用户的配置目录内…`
- `会话缓存目录权限过宽…且包含其他文件，拒绝自动修改目录权限…`

解决方案：

1. 先运行 `node scripts/xiaoai-listen.js check` 查看具体原因；
2. 换到一个当前用户私有目录：`export XIAOAI_STATE_DIR="$HOME/.local/state/xiaoai-bridge"`（Windows 用用户目录内路径）；
3. POSIX 上修正属主/权限：`chown -R "$(id -u):$(id -g)" <目录>`、`chmod 700 <目录>`；若目录里有其他文件，`chmod` 需要手动执行，程序不会擅自改动；
4. 仅当确认是单用户环境或文件系统不支持 POSIX 权限时，才考虑在**进程环境**中设置 `XIAOAI_ALLOW_INSECURE_STATE_DIR=true`；写进 `.env` 无效，且该开关不会绕过符号链接、非目录、属主不符、公共目录、硬链接等硬性检查。

### `.env` 中的安全敏感变量被忽略

症状：启动时提示 `已忽略 ... 中的安全敏感变量 ...`。

`LOCALAPPDATA`/`APPDATA`/`USERPROFILE`/`HOME`/`XDG_STATE_HOME`/`ProgramData`/`PUBLIC`/`SystemRoot`/`windir`/`TEMP`/`TMP`/`TMPDIR`/`XIAOAI_ALLOW_INSECURE_STATE_DIR` 只接受进程环境，防止随技能分发的 `.env` 把缓存目录“洗白”到公共位置或静默打开不安全开关。请改用 `set`/`export` 或进程管理器设置。

### `.env` 权限被拒绝

症状：`环境变量文件可被同组或其他用户修改…` 或 `无法收紧环境变量文件权限…`。

请执行 `chmod 600 scripts/.env` 后重试；`.env` 是符号链接时只告警，需自行确认链接目标权限。

### 找不到设备

症状：`❌ 找不到设备`

解决方案：运行以下命令查看所有设备：

```bash
DEBUG=true node scripts/xiaoai-listen.js test
```

使用设备的 `name`、`miotDID` 或 `mac` 作为 `MI_DEVICE_ID`。

### 收不到消息

可能原因：

1. 消息同步延迟（1-2 秒正常）
2. 设备离线或无响应
3. 上次轮询后确实没有新消息
4. 语音消息没有以 `TRIGGER_PREFIX` 开头

### 需要验证码

症状：`❌ 本次登录需要验证码`

解决方案：必须使用 passToken 登录。参考 https://github.com/idootop/migpt-next/issues/4

### 发现遗留 `.mi.json`

如果启动时提示“发现遗留会话文件”，说明旧版本把账号会话写进了技能目录或旧临时目录。请运行 `node scripts/xiaoai-listen.js clean` 清理，不要提交；新版本只会写入通过校验的 `XIAOAI_STATE_DIR`。

## 最佳实践

1. **使用 passToken** - 比密码更稳定，避免安全验证
2. **专用账号 + 数据最小化** - 只授权需要的设备，不要使用主账号
3. **轮询间隔** - 1-2 秒最佳（平衡响应速度和 API 负载）
4. **消息去重** - 跟踪已处理的时间戳，避免重复处理
5. **错误处理** - 监听器已内置指数退避，消费方仍应处理进程退出
6. **长文本分段** - 将长回复分句后多次调用 `speak`，单次不超过 1000 字符
7. **日志脱敏** - 不要记录原始语音转写；确需排查时用 `PRINT_TRANSCRIPTS=true` 临时开启。stderr 已对凭据字段脱敏，但仍不要长期落盘。
8. **高危动作确认** - 语音触发删除、支付、门锁、安防等动作前，先向用户复述并确认
9. **定期轮换** - 定期运行 `check`/`clean`；怀疑泄露时立即更换 passToken

## 相关资源

- MiGPT-Next 项目：https://github.com/idootop/migpt-next
- passToken 获取教程：https://github.com/idootop/migpt-next/issues/4
- API 完整文档：[references/migpt-api.md](references/migpt-api.md)
- 安全问题说明：[SECURITY.md](SECURITY.md)
- 本次安全审计记录：https://clawhub.ai/warm-winter/skills/xiaoai-bridge/security-audit

## 许可证

MIT-0 License，见 [LICENSE](LICENSE)。ClawHub 上发布的所有 Skill 均以 MIT-0 授权。

## 贡献

欢迎提交 Issue 和 Pull Request。
