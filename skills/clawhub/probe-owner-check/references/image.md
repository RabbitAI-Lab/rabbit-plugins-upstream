# AI 图片创作 / Image

脚本：`scripts/image.py`

## create — 文生图 / 图片编辑

```bash
# 文生图
python3 scripts/image.py create --prompt "极简风格的护肤品摆拍，柔和自然光"

# 图片编辑（传了 image_urls 就是编辑）
python3 scripts/image.py create --prompt "把背景换成大理石台面" \
  --image-urls https://.../product.jpg
```

`--image-urls` 空 = 文生图，非空 = 编辑这些图。默认同步返回图片 URL；加 `--async-mode` 则返回 `workspace_id` 自行轮询。

### 模型能力与参数（关键）

`ratio` / `resolution` 的取值集**因模型而异**，构造请求前先核对：

| 模型 | 文生图 | 编辑 | ratio | resolution |
|---|---|---|---|---|
| `nanobanana-pro`（默认） | ✅ | ✅ | 16:9 / 1:1 / 9:16 / 21:9 / 2:3 / 3:2 | 1k / 2k / 4k / 8k |
| `nano-banana-2` | ✅ | ✅ | 同上 | 0.5k / 1k / 2k / 4k |
| `nano-banana-2-fast` | ✅ | ✅ | 同上 | 2k / 4k |
| `seedream-4.5` | ✅ | ✅ | 16:9 / 1:1 / 9:16 / 2:3 / 3:2 | — |
| `seedream-5.0-lite` | ✅ | ✅ | 同上 | — |
| `seedream-4.5-seq` | — | ✅ | 同上 | — |
| `seedream-5.0-lite-seq` | — | ✅ | 同上 | — |
| `gpt-image-2` | ✅ | ✅ | 1:1 / 3:2 / 2:3 / 3:4 / 4:3 / 4:5 / 5:4 / 9:16 / 16:9 / 21:9 | 1k / 2k |
| `grok-2-image` | ✅ | — | 不校验 | — |
| `grok-imagine-image` | — | ✅ | 不校验 | — |

`-seq` 后缀的两个模型只能编辑不能文生。选模型前先确认用户要的是文生还是编辑。

## 电商与营销图

```bash
# 商品图套图
python3 scripts/image.py ecommerce \
  --reference-image-urls https://.../product.jpg \
  --methods hero_banner lifestyle_scene close_detail \
  --user-input "主打便携和快干"

# 活动海报
python3 scripts/image.py poster --event-info "双11 全场五折，11月1日开抢" \
  --reference-image-urls https://.../logo.png
```

`ecommerce --methods` 可选值，不传则出默认主图：

| method | 产出 |
|---|---|
| `hero_banner` | 主图（默认） |
| `lifestyle_scene` | 使用场景图 |
| `how_to_use` | 使用图 |
| `close_detail` | 细节特写图 |
| `material` | 材质图 |
| `brand_closing` | 品牌收尾图 |

一次传多个 method 就出一套图。`--product-info` 给商品参数、`--language` 定文案语言、`--aspect-ratio` 定画幅。

## 图片精修

```bash
# 抠图（去背景）
python3 scripts/image.py cutout --image-url https://.../product.jpg --output-format png

# 去水印 / 消除杂物
python3 scripts/image.py erase --image-url https://.../photo.jpg \
  --instruction "去掉右下角的水印"

# 高清放大
python3 scripts/image.py upscale --image-url https://.../small.jpg --scale 4
```

`erase` 两种指定方式：`--mask-url` 精确框定（白色为要消除的区域），或 `--instruction` 用自然语言描述消除什么。`--quantity` 可以一次出多个候选。

## 素材必须是公网 URL

```bash
python3 scripts/upload.py image ./product.jpg
```

## 耗时参考

| 操作 | 预计 |
|---|---|
| `create` | 30 秒 – 1 分钟（默认同步） |
| `cutout` / `erase` / `upscale` | 30 秒 – 2 分钟 |
| `ecommerce` / `poster` | 1–3 分钟，出多张更久 |

除 `create` 外都是异步，默认自动轮询；超时用 `query --workspace-id <id>` 续等。
