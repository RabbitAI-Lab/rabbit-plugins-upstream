# -*- coding: utf-8 -*-
"""DATA TEMPLATE for the financial-innovation briefing.

Replace the placeholders with real, dated, sourced news. Rules:
- 6 directions (each title must be unique and match the EXTRA key exactly).
- 5 items per direction (30 total).
- Every item: title / source / link / body(>=100 chars) / innovation / learning.
- body should include: 时间 + 具体公司 + 动作/数据 + 为什么值得关注.
- EXTRA key === DIRECTIONS[].title (including the "：" wording), or the
  summary card's tags/insight/action will come out empty.
"""

DIRECTIONS = [
    {
        "title": "存款理财：长钱锁定与活动化权益",
        "subtitle": "五年期大额存单从大行到股份行梯次重启，存款营销走向任务化、场景化、游戏化",
        "items": [
            {
                "title": "示例：XX银行五年期大额存单卡位长期限",
                "source": "XX银行、财联社",
                "link": "https://example.com/news/1",
                "body": "2026年7月，XX银行上新五年期大额存单，20万元起存、年化利率1.65%，成为当前极少数发售五年期产品的股份制银行。相较此前定存约1.35%的利率收益提升明显，产品保本保息、纳入存款保险，支持质押贷款与部分提前支取。在同业集体缺位长期限产品的空窗期，该行以稀缺供给精准承接避险长钱。",
                "innovation": "利用同业窗口期卡位长期限赛道，以利差撬动客户迁徙。",
                "learning": "将该产品与私行配置方案打通，以长存单为底仓叠加理财保险形成组合。",
            },
            # ... 另外 4 条，结构相同
        ],
    },
    {
        "title": "理财货架：主题化、公益化与客群定制",
        "subtitle": "理财产品从拼收益走向拼叙事：公益联动、黄金策略、客群定制竞相涌现",
        "items": [
            {
                "title": "示例：XX理财赛事联动公益产品",
                "source": "XX理财、腾讯新闻",
                "link": "https://example.com/news/2",
                "body": "XX理财将捐赠金额与某顶流赛事赛果动态挂钩，资金来自管理费收入，投资者收益不受影响。产品业绩稳健、0回撤，年化收益约1.90%。理财、观赛、行善三合一让固收产品自带传播力。",
                "innovation": "把IP与捐赠机制化挂钩，用情感叙事为固收注入传播属性。",
                "learning": "联动集团体育/城市IP设计“业绩稳健+公益叙事”产品获取品牌声量。",
            },
            # ... 另外 4 条
        ],
    },
    {
        "title": "公募基金：主动ETF破冰与养老投顾化",
        "subtitle": "首批主动ETF集中申报，个人养老金扩容并引入投顾实现账户全委托",
        "items": [
            # 5 条
        ],
    },
    {
        "title": "私募与高净值：定投纪律与全球再配置",
        "subtitle": "头部机构把私募服务从一次性配置推向定投纪律与多资产策略",
        "items": [
            # 5 条
        ],
    },
    {
        "title": "银保协同：65号文重塑渠道生态",
        "subtitle": "银保渠道在费用新规下从规模驱动转向产品力与透明度竞争",
        "items": [
            # 5 条
        ],
    },
    {
        "title": "信托创新：养老服务信托试点提速",
        "subtitle": "信托从财富管理延伸至生命照护、家企隔离与养老支付",
        "items": [
            # 5 条
        ],
    },
]

EXTRA = {
    "存款理财：长钱锁定与活动化权益": {
        "tags": ["五年期存单", "活动化运营", "场景权益"],
        "insight": "长期限存款与场景权益成为低成本获客、长钱锁定与年轻客群经营的三重抓手。",
        "action": "将长期限存单嵌入客户养老与教育金规划，抢占利率下行期的长钱心智。",
    },
    "理财货架：主题化、公益化与客群定制": {
        "tags": ["公益理财", "主题叙事", "客群定制"],
        "insight": "理财货架从拼收益转向拼叙事，情感与IP成为新的差异化因子。",
        "action": "联动集团IP资源设计“稳健+叙事”产品，低成本获品牌声量。",
    },
    # 其余 4 个方向键必须 === 上方 title，含“：”
}
