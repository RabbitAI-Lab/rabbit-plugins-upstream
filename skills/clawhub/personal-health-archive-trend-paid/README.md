# 个人健康档案与趋势分析（付费解锁版）

SkillHub 付费 skill 源码 + 微信支付商户服务器实现。对应 SkillHub 上架项：`@org-vnlatddn/personal-health-archive-trend`（付费解锁版）。

## 结构

```
SKILL.md              # 付费 skill 定义（即发布到 SkillHub 的内容）。按次计费 5.99 元，本地生成档案、仅付费校验走云端
mch-demo-adult/       # 微信支付商户服务器（部署于 NAS，监听 8081，经 Cloudflare tunnel 暴露为 https://mch.1001058.xyz/api/adult/resource）
  server.py           # 付费校验接口（X402 / WeixinPay-Required 402 流程），不接收健康资料
  Dockerfile          # 容器化构建
  Caddyfile           # 反向代理 + TLS 终止
  docker-compose.yml  # 编排
  requirements.txt    # Python 依赖
  .env.example        # 环境变量样例（真实 .env 不入库）
  .dockerignore
  部署-群晖NAS.md      # 群晖 NAS 部署说明
  部署说明.md          # 通用部署说明
```

## 部署前准备（本地补齐，不入库）

商户服务器运行需要以下私钥与配置，**不会进入本仓库**，请在各 `mch-demo-adult/` 目录本地放置：

- `apiclient_key.pem`、`skillhub_private_key.pem`、`wechat_pub_key.pem`（微信支付 / SkillHub 私钥）
- `.env`（参照 `.env.example` 填入 `APP_ID` / `MCH_ID` / `SERIAL_NO` / `SKILLHUB_TOKEN` 等真实值）

## 计费与隐私

- 计费模型：`per_call`，5.99 元/次（SkillHub 商家后台需填一致价格）。
- 健康资料**全程仅在用户本地处理**，付费校验接口仅传递 Skill 调用标识与订单信息，不上传任何健康资料。
- 详见 `SKILL.md` 内的《个人信息保护与授权声明》。

## 端口 / 连通性

- 本地端口：`8081`
- 公网入口：`https://mch.1001058.xyz/api/adult/resource`（Cloudflare tunnel）
- 健康档案主项目见 `个人健康档案/健康档案/`
