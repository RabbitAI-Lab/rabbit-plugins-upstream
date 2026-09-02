# 现有用户端 REST 合约

Python 工具只调用这些已经被用户端页面使用的公开接口。各环境只替换 `site`，路径和字段保持与页面一致；不存在统一的 `provider` 参数，也不存在本 Skill 自建的适配服务。

| lane | 配置/建单 | 上传/计数 | 订单查询 |
|---|---|---|---|
| character-count / vip | `/api/paper/check/public/pwp/config`、`POST /api/paper/check/public/pwp/order/create-draft` | `POST /api/paper/check/public/upload/presign` → OSS PUT → `POST /api/paper/check/public/upload/complete` | `GET /api/paper/check/public/order/{orderNo}` |
| wanfang | `/api/paper/wanfang/public/config` | `POST /api/paper/wanfang/public/upload/presign` → signed PUT | `POST /api/paper/wanfang/public/order/create`、`GET /api/paper/wanfang/public/order/{orderNo}` |
| cnki | `/api/paper/cnki/public/config` | `POST /api/paper/cnki/public/upload/presign` → signed PUT | `POST /api/paper/cnki/public/order/create`、`GET /api/paper/cnki/public/order/{orderNo}` |
| aigc | `/api/paper/aigc/public/config`、`POST /api/paper/aigc/public/order/pay/draft` | `prepare-submit` → source OSS PUT → `complete-source-archive` → `mark-upload-attempted` → supplier multipart → `complete-direct-submit` | `GET /api/paper/aigc/public/order/{orderNo}` |
| reduction | `/api/paper/reduction/public/config`、`POST /api/paper/reduction/public/order/create-draft` | source/report presign → PUT → `POST .../count/file` | `GET /api/paper/reduction/public/order/{orderNo}` |

## Response handling

站点通常返回 `{code: 0, data: ...}`。`data` 才是业务对象；非 0 业务码直接转为可执行错误。订单号只接受接口返回的 `orderNo`，不在本地生成或猜测。临时上传 URL、STS、token、对象键仅在进程内使用并脱敏输出。

## 支付与报告

支付接口（`.../pay`、`.../pay/qr`）只保留在页面内操作，本 Skill 不调用。订单完成后才调用 `.../report-download-url`（降重为 `result-download-url`），并把服务端返回的真实地址放入 `report_download_url`；没有返回就保持 `null`。浏览器页面地址来自 `domains/*.json` 的固定模板。
