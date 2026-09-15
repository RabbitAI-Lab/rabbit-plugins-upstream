# Amazon 特性利益点表达

把商品特性连接到评论验证的用户利益

## 一句话开始

安装授权后，把下面这句话发到 AI 客户端对话框，替换示例 ASIN 即可：

~~~text
把 Amazon 商品特性转成有评论证据支持的用户利益点。商品 B0XXXXXXXX（美国站）。
~~~

示例 ASIN 是占位符。AI 会识别商品、站点和目标，无需填写接口参数。
客户端未选中时，在问题前加“使用 $amazon-feature-benefit-writer”。
缺少必要资料或目标不唯一时，AI 会说明需要补充什么；专用 Skill 只处理本页对应场景。

首次使用可说“帮我完成 ARI 授权并检查是否可用”，自己在浏览器登录并授权。

以下命令供高级用法参考；日常只需描述目标，AI 会处理参数与当前账户可用性。

本场景先检查数据与费用，用户确认后生成。资料不足会说明需要补什么。

固定工作流：`listing/benefits`，输出 `ops_listing`。

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

- 广告关键词与竞价
- 无证据夸大商品承诺
- 自动修改或发布 Amazon 页面

## 连接安全

API 与授权入口固定为 https://ari.funewa.com，禁止重定向。生产包不支持自定义端点，ARI_ALLOW_CUSTOM_BASE 不再生效。遇到 ARI_ENDPOINT_BLOCKED 或 ARI_REDIRECT_BLOCKED 时停止操作，清除自定义地址或联系 ARI 支持，不能绕过校验。
