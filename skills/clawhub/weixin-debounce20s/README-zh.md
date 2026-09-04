# weixin-debounce20s

**类型**：设置型（功能装载）技能——agent 执行本技能后，本机 OpenClaw 微信渠道即具备 20s 连发防抖并完成验证。

## 它如何带来能力

只装技能不会产生传输行为；**让 agent 运行它**（按 `SKILL.md` 执行）才会自动完成真正启用：

1. 确保微信渠道 = ClawBot fork 插件（`clawhub:@yechang1450/openclaw-weixin-clawbot`，内含 20s 合并 + 引用注入；已装官方版则先替换）；
2. 设置 `messages.inbound` 窗口 = `20000`ms；
3. 重启 gateway；
4. 用日志（`debounce: buffered … windowMs=20000`）与一次连发实测做验证。

幂等：已配置好的机器只会校验。

## 新机用法

```bash
openclaw skills install @yechang1450/weixin-debounce20s
# 然后对 ClawBot 说：启用防抖 / 防抖没生效
```

需要装商店插件包时 agent 会先征得你同意。

## 触发词

启用防抖 / 防抖没生效 / 连发合并 / debounce。

文件：`SKILL.md`（执行体）、`README.md`/`README-zh.md`、`LICENSE`(MIT)。
