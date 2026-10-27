# 数据源与指标口径

只读取当前任务相关的部分。以下为来源入口和口径提示，不保证页面在当前工具中可访问，也不保证其中报价实时；实际引用要链接至查到的具体页面。失败时遵循 SKILL.md 的预算及备用源规则。

## A 股与港股

| 需求 | 优先核验来源 | 报价/报道备选与口径 |
|---|---|---|
| 上证综指、科创板指数及沪市公告 | [上交所](https://www.sse.com.cn/) | [东方财富行情中心](https://quote.eastmoney.com/)、[新浪财经](https://finance.sina.com.cn/)、[财联社](https://www.cls.cn/)；核对报价时点 |
| 深证成指、创业板指及深市公告 | [深交所](https://www.szse.cn/)；[国证指数](https://www.cnindex.com.cn/) | 同上；代码须带交易所/指数名称，不能只用可能重名的六位数字 |
| 沪深300、中证500/1000、指数估值 | [中证指数](https://www.csindex.com.cn/) | 标明价格/全收益指数、估值日期和口径；指数代码由官方页面核对 |
| 恒生、恒生科技、国企指数 | [恒生指数公司](https://www.hsi.com.hk/) | 东方财富/新浪报价；港股时区为Asia/Hong_Kong，勿套用A股午休/收市时间 |
| 公司财报/重大事项 | 公司IR、交易所、[巨潮资讯](https://www.cninfo.com.cn/)；港股用[披露易](https://www.hkexnews.hk/) | 报道用于发现，不替代公告正文；区分报告期和公告日 |
| 互联互通与融资数据 | [港交所互联互通](https://www.hkex.com.hk/Mutual-Market/Stock-Connect?sc_lang=zh-HK)、沪深交易所公开统计 | 先核对当前披露规则/频率；不假设北向实时净流入仍有公开可靠值，不把额度余额、成交额当净流入；南向与北向分开 |

成交额注明是否沪深合计、是否含北交所及单位（元/亿元）；涨跌家数和涨跌停家数说明股票池及统计时点。盘中与全天数据不可直接据此判断缩量/放量。

交易时段以[上交所交易安排](https://english.sse.com.cn/start/trading/schedule/)及相应交易所当年日历为准。A股竞价交易有午休和收盘集合竞价，不能把午休视为数据故障；盘后定价交易也不能混入普通收盘涨跌。

## 美股及市场风险

| 需求 | 优先核验来源 | 口径 |
|---|---|---|
| 标普500、道琼斯、等权指数 | [S&P Dow Jones Indices](https://www.spglobal.com/spdji/en/) | 官方指数资料与公开报价可能有延迟；实际时点照实标注 |
| 纳斯达克综合/100 | [Nasdaq](https://www.nasdaq.com/market-activity/indexes) | 两者成分与权重不同，不能统称“纳指”后混用数值 |
| 罗素2000 | [FTSE Russell](https://www.lseg.com/en/ftse-russell) | 小盘股参照，不能用ETF价格冒充指数点位 |
| ETF | 发行人资料，如[Invesco QQQ](https://www.invesco.com/qqq-etf/en/about.html) | QQQ跟踪Nasdaq-100；SPY跟踪S&P500；价格、NAV、总回报分别标识 |
| VIX | [Cboe波动率资料](https://www.cboe.com/tradable-products/volatility-trading) | 基于标普500期权的约30天预期波动；VIX现货指数、期货和ETF不可互换 |
| 个股财报 | 公司IR、[SEC EDGAR](https://www.sec.gov/edgar/search/) | 核对财季、GAAP/非GAAP、同比/环比、实际值/指引 |

公开行情备选：Nasdaq的标的页、东方财富、新浪、Yahoo Finance等当前能访问且带时间的页面。不存在永久“可用/禁用”清单；遇限制切换而非持续重试。

常规交易、延长时段、节假日和提前收市分别核验：[NYSE交易说明](https://www.nyse.com/trade/trading-information)。使用 `America/New_York` 自动处理夏令时；不要把美股开收盘固定写成全年同一北京时间。

## 利率、信用、外汇与商品

| 指标 | 来源 | 关键口径 |
|---|---|---|
| 美债10Y/2Y | [FRED DGS10](https://fred.stlouisfed.org/series/DGS10)、[DGS2](https://fred.stlouisfed.org/series/DGS2)；[美国财政部](https://home.treasury.gov/resource-center-data-chart-center/interest-rates) | 日频、单位百分比；观测日可能早于网页更新日，不是盘中实时报价 |
| 10Y−2Y曲线 | 同日DGS10与DGS2 | 相减得百分点，乘100得bp；不能用不同观测日拼出利差 |
| 10Y实际收益率 | [FRED DFII10](https://fred.stlouisfed.org/series/DFII10) | 日频TIPS实际收益率；与名义收益率区分 |
| 美国高收益债信用利差 | [FRED BAMLH0A0HYM2](https://fred.stlouisfed.org/series/BAMLH0A0HYM2) | 日频收盘OAS，单位百分比；3%等于300bp，不是债券总收益率；读取可用日期范围，勿假设完整长期历史 |
| 中国国债收益率 | [中债](https://www.chinabond.com.cn/) | 期限、曲线类型、估值日分别标明；人民币债券不能无条件充当美元股票的无风险基准 |
| DR007、人民币汇率 | [中国货币网](https://www.chinamoney.com.cn/)；[人民银行](https://www.pbc.gov.cn/) | DR007市场资金利率与政策利率不同；USD/CNY、USD/CNH、人民币中间价分别报告 |
| 美元指数 | [ICE美元指数说明](https://www.ice.com/products/194/US-Dollar-Index-Futures)及能核验的报价页 | DXY与美联储广义贸易加权美元指数不是同一指标；期货注明合约 |
| 黄金 | [LBMA](https://www.lbma.org.uk/prices-and-data)、[上海黄金交易所](https://www.sge.com.cn/)、可核验报价页 | LBMA基准定价、现货XAU/USD、COMEX期货、国内黄金和GLD各自有不同单位/时段 |
| 原油 | [CME WTI](https://www.cmegroup.com/markets/energy/crude-oil/light-sweet-crude.html)、[ICE](https://www.ice.com/)、[EIA](https://www.eia.gov/petroleum/) | WTI与Brent分开；注明交割月、美元/桶；换月跳变不直接解释为需求突变；EIA统计不是即时价格 |

单位示例（仅演示，非当前行情）：收益率从4.20%到4.30%是上升0.10个百分点/10bp；PE为25、国债收益率4%时，盈利收益率差为 `100/25 − 4 = 0` 个百分点。

## 宏观、政策和事件

- 美国：CPI/非农用[BLS](https://www.bls.gov/)及[CPI发布日历](https://www.bls.gov/schedule/news_release/cpi.htm)；PCE/GDP用[BEA](https://www.bea.gov/)；FOMC用[美联储日历与声明](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm)。本次可访问性优先于过去访问失败记录。
- 中国：CPI/PPI/PMI、工业及消费数据用[国家统计局](https://www.stats.gov.cn/)；社融、信贷、政策操作用人民银行；LPR使用官方发布的期限与日期。
- 区分观测月份、发布日期、同比/环比、季调与否；经济数据“前值”可能修订。不能将实际值、市场预期、修订前值混写。
- 降息概率查[CME FedWatch](https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html)；必须带目标会议、具体利率区间/事件定义和快照时间。旧报道只能作历史背景，不能冒充当前概率。
- 新闻备用可用财联社及可靠财经报道，但政策与日历尽量回查原始发布。“下次事件”须晚于当前时点，区分会议日期、决议发布时间与会议纪要发布日期。
- 数据页面无法访问且备用报道不能验证时，保留事件/指标名称并明确未核实，不猜日期或数值。
