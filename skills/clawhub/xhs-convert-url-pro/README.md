# 小红书转链工具（xhs-convert-url-pro）

小红书笔记链接**批量转链** CLI 工具，供 AI agent（OpenClaw / Claude / QwenWork 等支持 Agent Skills 的环境）调用。

## 功能

- 把小红书笔记链接（含 `xhslink.com` 短链）批量转换为携带 `xsec_token`、可直接在浏览器打开观看的新链接
- 提交任务 → 轮询 → 拿到终态结果，stdout 输出纯 JSON，方便 agent 解析
- 单批最多 50 条，幂等提交不重复扣费
- Node.js ≥ 18，零 npm 依赖，无需 `npm install`

## 使用方式

```bash
node cli.js register --link        # 注册（送 50 条免费配额，微信扫码完成）
node cli.js quota                  # 查询剩余配额
node cli.js submit --url "https://www.xiaohongshu.com/explore/xxxx" --wait
node cli.js submit --file urls.txt --wait
```

详细命令与错误码说明见 [SKILL.md](./SKILL.md)。

## 计费

- 每条**有效**转链 0.2 元（扣 1 条配额）；无效链接不扣费
- 注册即送 50 条免费配额
- 充值/批量购买优惠请联系客服：微信扫码 http://st.aidata366.com/assets/concat.png ，电话 18722121663

## 许可证

CLI 客户端代码采用 [MIT](./LICENSE) 许可证。后端转链服务为付费服务，使用受服务条款约束。
