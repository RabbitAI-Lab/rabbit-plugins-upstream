---
name: amazon-product-positioning
description: >
  基于 Amazon 商品详情与评论证据梳理用户价值、适用场景和可验证的产品定位方向。仅用于证据驱动的定位讨论；不用于市场规模、销量预测或广告执行。
  Requires an ARI API key (ari_live_*).
allowed-tools: Bash
---
# Amazon 产品定位建议

## 本 Skill 的固定运营入口

- 本入口只执行 `product/positioning`，输出模板固定为 `ops_product`。
- 先读 `skill-defaults.json` 与 `references/operation-workflow.md`，再调用 CLI。
- 接受自然语言需求，自动提取 ASIN 和站点；workflow/focus 从固定配置读取，不要求用户填写。
- 本专属入口只处理本场景：不切换到其他工作流，也不接收任意 prompt。
- 必须先报价；只有用户明确确认才可运行并扣点。评论不足只建议独立采集。
- 不虚构广告、库存、订单、利润或实时店铺数据。

## 自然语言入口与输出

- 用户只需表达目标，例如“根据 Amazon 商品详情和评论证据梳理产品定位方向。商品 B0XXXXXXXX（美国站）。”
- 从对话中提取 ASIN、站点、范围与输出长度；无站点信息时默认美国站并说明。
- 简短问题优先输出：数据范围、主要发现与评论依据、结论；证据不足时说明缺口，不把缺失数据补成结论。
- 用户未要求技术细节时，不展示内部任务标识、参数清单或命令日志。

## 固定 CLI 入口

```bash
python scripts/ari.py operations capabilities
python scripts/ari.py operations profile --asin <ASIN> --site amz_us
python scripts/ari.py operations quote --asin <ASIN> --site amz_us
# 用户明确确认后，复用报价返回的 requestId：
python scripts/ari.py operations run --asin <ASIN> --site amz_us --request-id <requestId> --confirm
python scripts/ari.py operations status --request-id <原requestId>
```

评论不足时先单独使用 `collect`；本 Skill 不会隐式采集。流中断后只运行
`operations status --request-id <原值>`，不要直接重跑。

## 计费与数据边界

- 采集按页扣点、分析按次扣点；先报价，用户明确确认后才执行。
- `capabilities` 与 `profile` 是确定性读取，不扣分析积点。
- 结论只基于已采集样本，不承诺实时价格、销量、库存或广告数据。

## 基础命令

除本场景入口外，包内 CLI 只提供授权、自检与版本，以及评论不足时的单独采集：

```bash
python scripts/ari.py setup        # 首次使用：浏览器授权并保存 Key
python scripts/ari.py configure    # 隐藏输入并手动保存 ARI API Key
python scripts/ari.py check        # 验证 Key、账户和积点余额
python scripts/ari.py version      # 显示版本与分发渠道（无需 Key）
python scripts/ari.py collect --asin <ASIN> --site amz_us   # 评论不足时单独采集，先报价
python scripts/ari.py status --task <taskId>                # 查询已提交的采集任务
```

## 不适用

- 市场规模或销量预测
- 广告投放与竞价
- 没有商品和评论证据的品牌策略

## 连接安全

API 与授权入口固定为 https://ari.funewa.com，禁止重定向。生产包不支持自定义端点，ARI_ALLOW_CUSTOM_BASE 不再生效。遇到 ARI_ENDPOINT_BLOCKED 或 ARI_REDIRECT_BLOCKED 时停止操作，清除自定义地址或联系 ARI 支持，不能绕过校验。
