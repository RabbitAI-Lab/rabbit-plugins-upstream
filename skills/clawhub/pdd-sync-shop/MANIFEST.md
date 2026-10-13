# MANIFEST — pdd-sync-shop

本声明供接收方 agent 快速安全评估。由 Claw School security_scan L0 自动生成并校验。

## 权限边界
- 网络目标（全部）：claw-school.com、host、localhost、mms.pinduoduo.com、www.python.org
- 本地写入：仅 `~/.pdd-data/`（店铺快照数据库/巡检参数/健康状态）与系统临时目录
- 子进程：scripts/run.py、scripts/chrome_manager.py（启动本地浏览器实例/内部脚本，不执行远程内容）
- 对店铺后台：只读（唯一例外 pdd-update-price，默认 dry-run，改价必须显式 --execute）

## 外发数据说明
- 仅在检测到接口改版时向 claw-school.com/api/bug-report 发送匿名故障指纹
  （技能名/版本/端点/分型，绝不含 cookie、商品、订单等商户数据；PDD_BUG_REPORT=0 可关）

## 文件清单（8 个）
- SKILL.md
- scripts/_miniws.py
- scripts/cdp_collect.py
- scripts/chrome_manager.py
- scripts/resilience.py
- scripts/run.py
- scripts/store.py
- skill.yaml

## L0 扫描结论：PASS
