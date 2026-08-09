# 儿科健康档案建立器（云端付费版）

SkillHub 付费 skill 源码 + 微信支付商户服务器实现。对应 SkillHub 上架项：`@org-vnlatddn/pediatric-health-record`（云端付费版）。

## 结构

```
SKILL.md          # 付费 skill 定义（即发布到 SkillHub 的内容）。按次计费 2.99 元，数据经 TLS 加密提交至商户服务器生成儿童健康档案
mch-demo/         # 微信支付商户服务器（部署于 NAS，监听 8080，经 Cloudflare tunnel 暴露为 https://mch.1001058.xyz/）
  server.py           # 付费校验 + 档案生成接口（X402 / WeixinPay-Required 402 流程）
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

商户服务器运行需要以下私钥与配置，**不会进入本仓库**，请在各 `mch-demo/` 目录本地放置：

- `apiclient_key.pem`、`pub_key.pem`、`skillhub_private_key.pem`（微信支付 / SkillHub 私钥）
- `.env`（参照 `.env.example` 填入 `APP_ID` / `MCH_ID` / `SERIAL_NO` / `SKILLHUB_TOKEN` 等真实值）

## 计费与隐私

- 计费模型：`per_call`，2.99 元/次（SkillHub 商家后台需填一致价格）。
- 仅面向儿童法定监护人；资料仅用于本次档案生成，服务完成后不长期留存，不向第三方共享。
- 详见 `SKILL.md` 内的《未成年人个人信息保护声明》与《数据披露与隐私声明》。

## 端口 / 连通性

- 本地端口：`8080`
- 公网入口：`https://mch.1001058.xyz/`（Cloudflare tunnel）
- 健康档案主项目见 `个人健康档案/邬致远健康档案/`
