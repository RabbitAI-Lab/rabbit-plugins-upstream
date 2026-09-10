# weixin-quote

**类型**：设置型（功能装载）技能——agent 执行本技能后，本机 OpenClaw 微信渠道即具备"引用即上下文"并完成验证（引用 bot 回复时把被引用全文注入模型）。

## 它如何带来能力

只装技能不会产生行为；**让 agent 运行它**（按 `SKILL.md` 执行）才会自动完成真正启用：

1. 确保微信渠道 = ClawBot fork 插件（`clawhub:@yechang1450/openclaw-weixin-clawbot`，内置服务端 id 记录 + 引用 id 邻近 ≤1000 解析；已装官方版则先替换）；
2. 重启 gateway；
3. 用日志验证：发送出现 `[send-resp]`；引用新 bot 回复时出现 `[quote-hit] method=id …`。

幂等：已配置好的机器只会校验。

## 新机用法

```bash
openclaw skills install @yechang1450/weixin-quote
# 然后对 ClawBot 说：启用引用 / 引用没生效
```

需要装商店插件包时 agent 会先征得你同意。

## 触发词

启用引用 / 引用没生效 / 引用追问 / quote。

文件：`SKILL.md`（执行体）、`README.md`/`README-zh.md`、`LICENSE`(MIT)。
