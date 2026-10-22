---
name: xiaoai-bridge
description: 小米小爱音箱语音指令桥接。截取小爱音箱的语音消息，转换为 AI 助手指令，并通过 TTS 回复。支持触发词过滤、自动去重、后台监听。适用于通过小爱音箱语音控制 OpenClaw 助手、智能家居联动、语音任务执行等场景。
version: 1.1.1
author: warm-winter
license: MIT-0
tags: [xiaomi, xiaoai, voice, tts, iot, smart-home]
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

## 工作原理

1. **监听** - 轮询小爱音箱获取语音消息（小米云端语音转文字）
2. **处理** - 将语音消息转换为 AI 助手指令
3. **回复** - 通过小爱音箱 TTS 播报处理结果

消息以 JSON 行写入 stdout，状态和错误写入 stderr，方便被其他进程直接消费。

## 安全模型（请先阅读）

`passToken` 等价于小米账号的登录凭据，能读取设备列表、对话记录并控制音箱。请按以下方式使用：

1. **使用专用账号**：不要用主账号；在小米账号设置中限制授权范围。
2. **优先使用 passToken**：密码登录可能触发验证码，且更容易被风控。
3. **会话缓存**：依赖库 `@mi-gpt/miot` 会把包含 `passToken` / `serviceToken` 的 `.mi.json` 写到**进程当前目录**。本 Skill 会在登录前把工作目录切换到私有缓存目录（默认系统临时目录下的 `xiaoai-bridge/`，权限 0700，缓存文件 0600），不会写进技能目录。
4. **不要提交凭据**：`.env`、`.mi.json` 不要提交；源码目录带有 `.gitignore`，安装到其他项目后请把这两类文件加入你自己的忽略规则，发布或分享前用 `git status` 确认没有包含。
5. **用完即清**：运行 `node scripts/xiaoai-listen.js clean` 删除本地会话缓存。
6. **日志边界**：监听模式默认只把语音转写发给 stdout 的消费方；`debug-fetch.js` 默认不打印转写原文。
7. **权限最小化**：以专用、非特权系统账号运行，只给它需要的环境变量。

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

`.env` 的加载顺序是 `scripts/.env` → 技能根目录 `.env`；也可以用 `XIAOAI_ENV_FILE` 指定任意路径。

### 3. 测试连接

```bash
node scripts/xiaoai-listen.js test
```

预期输出（stderr）：

```text
🔌 正在连接小爱音箱...
✅ 连接成功
✅ 连接测试通过
```

### 4. 启动监听

```bash
node scripts/xiaoai-listen.js
```

stdout 只会输出 JSON 行，例如：

```json
{"type":"message","text":"查一下天气","originalText":"请查一下天气","timestamp":1708070400000}
```

后台运行：

```bash
node scripts/xiaoai-listen.js > xiaoai.log 2> xiaoai.err &
```

或使用 OpenClaw 进程管理（推荐）。

### 5. 清理缓存

```bash
node scripts/xiaoai-listen.js clean
```

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

# 清理本地会话缓存
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
| `XIAOAI_STATE_DIR` | 否 | 会话缓存目录（默认系统临时目录下 `xiaoai-bridge/`） |
| `XIAOAI_ENV_FILE` | 否 | 指定 `.env` 文件路径 |
| `PRINT_TRANSCRIPTS` | 否 | 仅 `debug-fetch.js`：设为 `true` 打印转写原文 |

\* `MI_PASS_TOKEN` 或 `MI_PASSWORD` 二选一。

## 输出与退出码

| 场景 | stdout | stderr | 退出码 |
|------|--------|--------|--------|
| 监听模式 | 仅 JSON 行 | 状态、错误 | 0 正常退出；1 运行失败 |
| `speak` / `test` | 无（调试日志除外） | 状态、错误 | 0 成功；1 连接失败 |
| 配置错误 | 空 | 配置错误说明 | 2 |
| `--help` / `--version` / `clean` | 文本 | 无 | 0 |

## 故障排查

### 登录失败

症状：`❌ 连接失败: 登录失败`

解决方案：

1. 使用 passToken 替代密码（推荐）
2. 检查 `MI_USER_ID` 是否为纯数字（不是手机号或邮箱）
3. 开启 `DEBUG=true` 查看详细错误信息

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

### 发现 `.mi.json`

如果启动时提示“发现遗留会话文件”，说明旧版本把账号会话写进了技能目录。请删除该文件，不要提交；新版本只会写入 `XIAOAI_STATE_DIR`。

## 最佳实践

1. **使用 passToken** - 比密码更稳定，避免安全验证
2. **轮询间隔** - 1-2 秒最佳（平衡响应速度和 API 负载）
3. **消息去重** - 跟踪已处理的时间戳，避免重复处理
4. **错误处理** - 监听器已内置指数退避，消费方仍应处理进程退出
5. **长文本分段** - 将长回复分句后多次调用 `speak`，单次不超过 1000 字符
6. **日志脱敏** - 不要记录原始语音转写；确需排查时用 `PRINT_TRANSCRIPTS=true` 临时开启

## 相关资源

- MiGPT-Next 项目：https://github.com/idootop/migpt-next
- passToken 获取教程：https://github.com/idootop/migpt-next/issues/4
- API 完整文档：[references/migpt-api.md](references/migpt-api.md)
- 安全问题说明：[SECURITY.md](SECURITY.md)

## 许可证

MIT-0 License，见 [LICENSE](LICENSE)。ClawHub 上发布的所有 Skill 均以 MIT-0 授权。

## 贡献

欢迎提交 Issue 和 Pull Request。
