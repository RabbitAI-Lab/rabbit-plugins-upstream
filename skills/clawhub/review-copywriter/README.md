# Amazon 评论证据文案规划

将评论语言整理为完整 Listing 优化方向

## 一句话开始

安装授权后，把下面这句话发到 AI 客户端对话框，替换示例 ASIN 即可：

~~~text
根据 Amazon 评论证据规划完整 Listing 文案优化方向。商品 B0XXXXXXXX（美国站）。
~~~

示例 ASIN 是占位符。AI 会识别商品、站点和目标，无需填写接口参数。
客户端未选中时，在问题前加“使用 $amazon-review-based-copywriter”。
缺少必要资料或目标不唯一时，AI 会说明需要补充什么；专用 Skill 只处理本页对应场景。

首次使用可说“帮我完成 ARI 授权并检查是否可用”，自己在浏览器登录并授权。

以下命令供高级用法参考；日常只需描述目标，AI 会处理参数与当前账户可用性。

本场景先检查数据与费用，用户确认后生成。资料不足会说明需要补什么。

固定工作流：`listing/full`，输出 `ops_listing`。

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

- 没有商品和评论数据的自由创作
- 广告投放与关键词竞价
- 自动修改或发布 Amazon 页面
