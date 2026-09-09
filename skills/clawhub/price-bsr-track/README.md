# Amazon 价格与 BSR 变化追踪

从商品快照摘要展示价格与 BSR 字段变化

## 一句话开始

安装授权后，把下面这句话发到 AI 客户端对话框，替换示例 ASIN 即可：

~~~text
摘要一个 Amazon ASIN 已保存快照中的展示价格与 BSR 字段变化。商品 B0XXXXXXXX（美国站）。
~~~

示例 ASIN 是占位符。AI 会识别商品、站点和目标，无需填写接口参数。
客户端未选中时，在问题前加“使用 $amazon-price-bsr-tracker”。
缺少必要资料或目标不唯一时，AI 会说明需要补充什么；专用 Skill 只处理本页对应场景。

首次使用可说“帮我完成 ARI 授权并检查是否可用”，自己在浏览器登录并授权。

以下命令供高级用法参考；日常只需描述目标，AI 会处理参数与当前账户可用性。

固定工作流：`watch/price_bsr`，输出 `watch_digest`；确定性 digest 为 0 积点，自动扫描不调用 LLM。

本包在正式清单发布前不得作为线上 1.4.1 市场包上传。先运行 `python scripts/ari.py watch --help`；当前 CLI 未提供 watch 子命令时必须停止并提示升级。

## 高级用法与可用性

```bash
python scripts/ari.py watch list
python scripts/ari.py watch create --asin <ASIN> --site amz_us --schedule weekly
python scripts/ari.py watch pause --watch-id <watchId>
python scripts/ari.py watch resume --watch-id <watchId>
python scripts/ari.py watch delete --watch-id <watchId>
python scripts/ari.py watch digest --watch-id <watchId> --period 7d
python scripts/ari.py watch events --watch-id <watchId>
```

watch 只提供快照变化和确定性摘要，不承诺实时价格、销量、库存或广告数据。
AI 周报须使用 weekly 专用工作流，单独报价并在用户明确确认后执行；本 Skill 不代办。

## 不适用

- 实时价格、实时 BSR 或小时级监控
- 销量、转化率或利润预测
- 库存、广告、订单或自动调价执行
