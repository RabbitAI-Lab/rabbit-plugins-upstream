# Amazon 竞品特性矩阵

按商品字段与评论证据整理竞品特性矩阵

## 一句话开始

安装授权后，把下面这句话发到 AI 客户端对话框，替换示例 ASIN 即可：

~~~text
根据主 ASIN 与竞品证据整理商品特性对照矩阵。商品 B0XXXXXXXX（美国站），竞品 B0YYYYYYYY（美国站）。
~~~

示例 ASIN 是占位符。AI 会识别商品、站点和目标，无需填写接口参数。
客户端未选中时，在问题前加“使用 $amazon-competitor-feature-matrix”。
缺少必要资料或目标不唯一时，AI 会说明需要补充什么；专用 Skill 只处理本页对应场景。

首次使用可说“帮我完成 ARI 授权并检查是否可用”，自己在浏览器登录并授权。

以下命令供高级用法参考；日常只需描述目标，AI 会处理参数与当前账户可用性。

本场景先检查数据与费用，用户确认后生成。资料不足会说明需要补什么。

固定工作流：`page_compare/features`，输出 `ops_page_compare`。

## 高级用法与计费

```bash
python scripts/ari.py operations capabilities
python scripts/ari.py operations profile --asin <ASIN> --site amz_us
python scripts/ari.py operations quote --asin <ASIN> --site amz_us
# 用户明确确认后，复用报价返回的 requestId：
python scripts/ari.py operations run --asin <ASIN> --site amz_us --request-id <requestId> --confirm
```

评论不足时先单独使用 `collect`；本 Skill 不会隐式采集。流中断时使用
`operations status --request-id <原requestId>`，不要直接重跑。

需要 ARI API Key（`ari_live_*`）。首次使用运行 `python scripts/ari.py setup`。

## 不适用

- 销量或市场份额预测
- 实时库存、订单或广告数据
- 没有证据的性能或合规认证
