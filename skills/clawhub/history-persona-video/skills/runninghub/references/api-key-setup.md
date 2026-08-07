# API Key Setup（安装必读）

## ⚠️ 重要原则

- 本技能**不附带任何 API Key**，也**不使用任何他人共享的 Key**。
- 每个安装者必须**自行前往 RunningHub 官网注册账号，生成自己的 API Key**。
- 请勿向他人索要 Key，也不要将 Key 写入技能文件或随技能一起分发。
- Key 仅保存在安装者自己的本地配置 `~/.openclaw/openclaw.json` 中。

## 第一步：去官网生成你自己的 API Key

1. 打开官网：https://www.runninghub.cn
2. 注册 / 登录你的账号（手机号或邮箱）
3. 进入「企业API / API 管理」页面创建 Key：https://www.runninghub.cn/enterprise-api/sharedApi
4. 充值：生成图片/视频/音频需要余额，充值地址：https://www.runninghub.cn/vip-rights/4

## 第二步：检查 Key 状态

Run `--check` first:
```bash
python3 {baseDir}/scripts/runninghub.py --check
```

React by `status`:
- `"ready"` → "账号就绪！余额 ¥{balance}，想做点什么？生图、视频、配音都可以找我～"
- `"no_key"` → 引导用户按上方「第一步」去官网注册并生成**自己的** Key
- `"no_balance"` → "余额空了～ 充个值就能继续：https://www.runninghub.cn/vip-rights/4"
- `"invalid_key"` → "Key 不太对，请重新到官网生成：https://www.runninghub.cn/enterprise-api/sharedApi"

## 第三步：保存你自己的 Key

When user sends their own key, verify with `--check --api-key <KEY>`. If valid, save it:

```bash
python3 -c "
import json, pathlib
p = pathlib.Path.home() / '.openclaw' / 'openclaw.json'
p.parent.mkdir(exist_ok=True)
cfg = json.loads(p.read_text()) if p.exists() else {}
cfg.setdefault('skills', {}).setdefault('entries', {}).setdefault('runninghub', {})['apiKey'] = 'THE_KEY'
p.write_text(json.dumps(cfg, indent=2))
"
```

Replace `THE_KEY` with **your own** key. OpenClaw auto-injects it as `RUNNINGHUB_API_KEY` env var via `primaryEnv`.

> ⚠️ 该 Key 仅保存在你自己的 `~/.openclaw/openclaw.json` 中，属于个人配置，不会随技能文件分发，也不会被其他安装者使用。
