# 省柴柴·出行规划与订票助手

一只懂旅行的柴犬。帮你规划行程、查机票高铁、找酒店和当地玩法，每个推荐都带购买入口。

## 功能

- **行程规划** — 根据目的地、天数、兴趣和预算给路线和节奏
- **机票/高铁查询** — 实时班次 + 价格 + 购买入口
- **酒店推荐** — 按位置/档次/预算给候选，附预订入口
- **景点 + 美食** — 本地口碑推荐，A 档美食带团购入口
- **出行文档** — 一键生成行程 HTML，直接带走用

## 安装

1. 安装 [Node.js](https://nodejs.org/)
2. 将本目录作为 skill 加载到你的 agent 平台
3. 首次使用自动工作，无需配置密钥

## 用法示例

```bash
# 机票查询
node scripts/travel.js --action flight-search --from 广州 --to 昆明 --date "10月3号"

# 高铁查询
node scripts/travel.js --action train-search --from 上海 --to 嘉兴 --date "明天"

# 酒店查询
node scripts/travel.js --action hotel-search --city 昆明

# 景点门票
node scripts/travel.js --action sights --city 昆明

# 美食团购
node scripts/travel.js --action food-search --keyword 米线 --city 昆明

# 生成出行文档
node scripts/gen-itinerary-html.js <行程.json> -o 行程.html
```

## 隐私

本技能不采集用户数据；查询会发送到云端接口以获取实时结果。密钥只存在于云端环境变量，仓库与发布包零明文。