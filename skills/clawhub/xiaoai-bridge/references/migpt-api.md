# MiGPT-Next API 参考

本文档对应依赖 `@mi-gpt/miot@1.2.2`。

## 核心配置

`getMiNA()` / `getMIoT()` 接收的是**扁平**的 `MiServiceConfig`：

```typescript
interface MiServiceConfig {
  did: string;          // 设备名称、miotDID 或 MAC
  userId?: string;      // 小米 ID（纯数字）
  password?: string;    // 账号密码（可能触发安全验证）
  passToken?: string;   // 推荐：passToken
  debug?: boolean;      // 打印设备列表等调试信息
  timeout?: number;     // 请求超时（毫秒，默认 5000）
}
```

> 注意：`{ speaker: { ... } }` 是 MiGPT-Next 上层应用的配置结构，**不是** `@mi-gpt/miot` 的入参，直接传给 `getMiNA()` 会登录失败。

### 使用 passToken 登录（推荐）

```typescript
import { getMiNA } from "@mi-gpt/miot";

const mina = await getMiNA({
  userId: "你的小米账号ID",
  passToken: "你的passToken",
  did: "小爱音箱设备ID",
});
```

### 使用密码登录（可能触发风控）

```typescript
const mina = await getMiNA({
  userId: "你的小米账号ID",
  password: "你的密码",
  did: "小爱音箱设备ID",
});
```

## 会话缓存（重要安全提示）

`@mi-gpt/miot` 登录成功后会执行等价于下面的逻辑：

```typescript
const kConfigFile = ".mi.json";
store[service] = account;         // account 含 passToken / serviceToken / ssecurity
await writeJSON(kConfigFile, store); // 相对 process.cwd() 解析
```

也就是说：

- `.mi.json` 会写到**进程当前工作目录**，不是包目录；
- 文件里包含可直接接管小米账号的会话凭据；
- 在 Git 仓库根目录直接运行脚本，凭据就会出现在仓库里，极易被提交。

本 Skill 的处理方式：

1. 登录前 `process.chdir()` 到 `XIAOAI_STATE_DIR`（默认系统临时目录下的 `xiaoai-bridge/`）；
2. 目录权限 0700，缓存文件尽量收紧到 0600；
3. `node scripts/xiaoai-listen.js clean` 一键删除；
4. 启动时检测技能目录中的遗留 `.mi.json` 并告警。

如果你在自己的项目里直接使用 `@mi-gpt/miot`，请自行做同样的隔离，并把 `.mi.json` 加入 `.gitignore`。

## 底层 API

### 获取消息

```typescript
import { getMiNA } from "@mi-gpt/miot";

const mina = await getMiNA(config);

const conversations = await mina.getConversations({
  limit: 10,
  timestamp: Date.now(),
});
```

返回结构（记录按时间**新 → 旧**排列，且包含游标消息本身）：

```typescript
interface MiConversations {
  records: Array<{
    time: number;        // 时间戳（毫秒）
    query: string;       // 用户说的话
    answers: Array<{
      tts?: { text: string }; // 小爱的回复
    }>;
  }>;
}
```

### TTS 播放

```typescript
await mina.play({ text: "你好" });
await mina.play({ url: "https://example.com/audio.mp3" });
```

### 音量与播放控制

```typescript
const volume = await mina.getVolume();
await mina.setVolume(50);   // 0-100
await mina.pause();
await mina.playOrPause();
await mina.stop();
```

### 设备列表

```typescript
const devices = await mina.getDevices();
```

`debug: true` 时，`getMiNA()` 在匹配设备前也会把设备列表打印出来。

## 轮询模式

直接照抄「遍历时推进游标」的写法会漏消息：接口返回新 → 旧，第一次循环就把游标推到最新，后面的新消息全部被跳过。正确做法是先收集、再统一推进：

```typescript
let lastTimestamp = Date.now();

while (true) {
  const conversations = await mina.getConversations({
    limit: 10,
    timestamp: lastTimestamp,
  });

  const since = lastTimestamp;
  let newest = lastTimestamp;
  const messages: string[] = [];

  for (const record of conversations?.records ?? []) {
    if (record.time > newest) newest = record.time;
    if (record.time > since) messages.push(record.query);
  }

  lastTimestamp = newest;
  messages.reverse(); // 按时间从旧到新处理

  for (const message of messages) {
    console.log(`新消息：${message}`);
  }

  await new Promise((resolve) => setTimeout(resolve, 1000));
}
```

## 环境变量配置

```bash
MI_USER_ID=1234567890
MI_PASS_TOKEN=your_pass_token_here
MI_DEVICE_ID=小爱音箱Pro
```

## 常见问题

### 获取 passToken

访问：https://github.com/idootop/migpt-next/issues/4

### 获取设备 ID

```typescript
const mina = await getMiNA({
  userId: "...",
  passToken: "...",
  did: "任意设备名",
  debug: true, // 会打印设备列表
});
```

### 登录失败

- 触发风控：改用 passToken
- 账号错误：`userId` 是数字，不是手机号
- 设备错误：开启 debug 查看设备列表
- 缓存冲突：删除 `XIAOAI_STATE_DIR` 下的 `.mi.json` 后重试
