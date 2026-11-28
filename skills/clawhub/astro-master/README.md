# 星盘大师 API Skill

## 概述

本 Skill 提供星盘大师开放API的14项占星能力，支持本命排盘、个人运势、星座运势查询等。
数据与官方客户端（flutter-web/app-web/APP）完全一致。

## 配置信息

- 用户: jiuchongju
- 密钥前缀: zs_2JiYC1a6e
- 创建时间: 2026-08-02 09:43:02
- 有效期: 2027-08-02 01:43:02
- API地址: https://api.astro.jiuchongju.com
- 目标平台: 通用超集
- 密钥: 内置默认共享密钥（开箱即用，也可替换为自有 ASTRO_API_KEY）

## 快速开始

```bash
pip install requests
python astro_client.py  # 已内置共享密钥，直接测试连通性
# 可选（BYOK）：如需自定义密钥，环境变量会覆盖内置值
export ASTRO_API_KEY="你的密钥"
```

## 文件说明

| 文件 | 说明 |
|------|------|
| SKILL.md | ClawHub Skill 描述文件（14项功能指引 + 渲染模板） |
| config.json | API 调用配置（已内置默认共享密钥，开箱即用） |
| astro_client.py | 核心客户端库 |
| requirements.txt | Python 依赖（仅 requests） |
| README.md | 本说明文件 |

## 功能清单

1. 获取用户经纬度坐标（城市搜索）
2. 个人信息补全（交互式收集）
3. 本命排盘计算
4. 个人每日运势
5. 个人本周运势
6. 个人本月运势
7. 个人本年运势
8. 十二星座每日运势
9. 指定星座每日运势
10. 指定星座本周运势
11. 指定星座本月运势
12. 指定星座本年运势
13. 查询最近10条调用记录
14. 官网注册引导

## 注意事项

- 密钥有效期至 2027-08-02 01:43:02，过期后请到 https://astro.jiuchongju.com 重新申请
- 如遇"算力接口不可用"提示，请联系管理员
- 如需 MCP 模式（远程 Streamable HTTP 或本地 stdio 兜底），请单独导出 MCP 包
