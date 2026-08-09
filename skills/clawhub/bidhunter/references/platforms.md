# 支持平台清单与配置

## 内置平台适配器

以下平台已在 `bid_monitor.sh` 中实现采集适配器：

| 平台编码 | 平台名称 | 网址 | 采集方式 | 认证要求 | 状态 |
|---|---|---|---|---|---|
| `cnooc` | 中海油采办业务管理与交易系统 | bid.cnooc.com.cn | API (JSON) | 免登录（公开列表） | 已适配 |
| `cebpubservice` | 中国招标投标公共服务平台 | ctbpsp.com | API (JSON POST) | 免登录 | 已适配 |
| `ccgp` | 中国政府采购网 | ccgp.gov.cn | HTML 解析 | 免登录 | 已适配 |

## 计划适配平台

以下平台已识别但尚未实现适配器，可按"自定义数据源"流程接入：

| 平台类别 | 平台名称 | 网址 | 技术难点 | 优先级 |
|---|---|---|---|---|
| 央企招采 | 中石油电子招标投标平台 | bid.cnpcbidding.com | 需注册账号 | P0 |
| 央企招采 | 中石化物资采购电子商务平台 | sourcing.sinopec.com | 需企业认证 | P0 |
| 央企招采 | 国家电网电子商务平台 | ecp.sgcc.com.cn | 需电子钥匙 | P1 |
| 央企招采 | 中国南方电网阳光电子商务平台 | bidding.csg.cn | 需注册 | P1 |
| 能源电力 | 中国华能集团电子商务平台 | ec.chng.com.cn | 需注册 | P1 |
| 能源电力 | 中国大唐集团电子采购平台 | cdt-ec.com | 需注册 | P1 |
| 能源电力 | 国家电投电子商务平台 | eptp.com.cn | 需注册 | P1 |
| 能源建设 | 中国能建电子采购平台 | ec.ceec.net.cn | 需注册 | P1 |
| 能源建设 | 中国电建招标与采购网 | powerchina.cn | 需注册 | P1 |
| 公共资源 | 全国公共资源交易平台 | ggzyjyw.com | 数据聚合，需解析 | P0 |
| 公共资源 | 各省市公共资源交易中心 | 分省平台 | 模板差异极大 | P1 |
| 行业垂直 | 军队采购网 | plap.mil.cn | 需军队供应商库资质 | P2 |
| 行业垂直 | 铁路建设工程网 | railway.cn | 需注册 | P2 |
| 行业垂直 | 民航专业工程招标投标管理系统 | caac.gov.cn | 访问受限 | P2 |

## 平台适配器开发规范

每个适配器需实现一个 `fetch_<platform>()` bash 函数：

1. **输入**：`$1` = 目标日期 (YYYY-MM-DD)
2. **输出**：JSON lines 到 stdout，每行一条公告
3. **格式**：
   ```json
   {
     "id": "公告唯一标识",
     "title": "项目名称",
     "source": "平台编码",
     "url": "详情页链接",
     "publish_time": "发布时间"
   }
   ```
4. **注意事项**：
   - 翻页时 sleep 2s 防限流
   - 401/403 时冷却 10s 重试一次
   - 过滤结果公示类（中标/成交公告）
   - 只采集当天发布（近似排除已开标标）

## 自定义数据源

添加新平台适配器步骤：

1. 在 `bid_monitor.sh` 中添加 `fetch_<platform>()` 函数
2. 将平台编码加入 `PLATFORMS` 数组
3. 在 `references/platforms.md` 中记录平台信息
4. 测试：`bash bid_monitor.sh --platform <name> --fresh --date $(date +%Y-%m-%d)`

## detail_url_template

各平台详情页链接格式：

| 平台 | 模板 |
|---|---|
| cnooc | `https://bid.cnooc.com.cn/home/#/newsAlertDetails?index=0&childrenActive=1&id={ID}&type=null` |
| cebpubservice | `https://ctbpsp.com/#/noticeDetail?id={ID}` |
| ccgp | 从列表页 HTML 中直接提取 |

## 数据源配置项

每个平台适配器支持的配置：

- **启用/停用**：在 `PLATFORMS` 数组中增删
- **监控范围**：在 `fetch_<platform>()` 函数中调整 API 参数
- **采集深度**：标题+摘要（默认）/ 全文+附件列表（需 detail 接口）
- **更新频率**：通过定时任务配置（默认每日）
- **认证配置**：免登录（默认）/ 账号 / CA证书（需自行实现）
