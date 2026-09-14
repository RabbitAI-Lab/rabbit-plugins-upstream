# Amazon 标题优化建议 API 参考

固定契约：`listing/title` → `ops_listing`。不得改成任意 prompt 或其他 focus。

## 固定命令

```bash
python scripts/ari.py operations capabilities
python scripts/ari.py operations profile --asin <ASIN> --site amz_us
python scripts/ari.py operations quote --asin <ASIN> --site amz_us
python scripts/ari.py operations run --asin <ASIN> --site amz_us --request-id <requestId> --confirm
python scripts/ari.py operations status --request-id <requestId>
```

## 授权与环境

- 需要 ARI API Key（`ari_live_*`）；首次使用运行 `python scripts/ari.py setup`。
- API 与授权入口固定为 https://ari.funewa.com，生产包不支持自定义端点。

## 计费

- 采集按页扣点、分析按次扣点；`quote` 返回报价后必须由用户明确确认才可 `run`。
- `capabilities` 与 `profile` 不扣分析积点。

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

- 完整 Listing 文案代写
- 广告关键词与竞价
- 自动修改或发布 Amazon 页面
