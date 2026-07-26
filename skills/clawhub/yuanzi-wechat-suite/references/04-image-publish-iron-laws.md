# 04. 配图发布铁律（草稿箱无图排查）

> 来源：MEMORY.md「公众号配图发布铁律（2026-06-29）」
> 来源：MEMORY.md「公众号图文准备（2026-07-02 实战）」

## 🚨 重大踩坑：草稿箱配图不显示的根因

`publish_wechat.py` 的 `rewrite_local_images()` 函数逻辑：

| src 类型 | 处理 |
|---|---|
| `http://` / `https://` 开头 | **跳过**（已上传） |
| 相对路径 | 拼接 `base_dir` + 上传微信 CDN + 替换 |
| **base64 内联**（`data:image/png;base64,...`） | **不处理**，草稿箱无图 ❌ |

## ✅ 正确做法：用相对路径引用本地图片

```html
<!-- ❌ 错误：base64 内联（脚本不处理） -->
<img src="data:image/png;base64,iVBORw0KGgo..." />

<!-- ✅ 正确：相对路径引用（脚本自动上传 CDN） -->
<img src="imgs/v5_fig1_1260x540.png" />
```

## publish_wechat.py 自动行为

1. 扫描 `<img src="相对路径">`
2. 上传本地图片到微信永久素材库（`material/add_material`）
3. 替换 `src` 为微信 CDN URL（`http://mmbiz.qpic.cn/...`）
4. 创建草稿 → 老板人工群发

## 渲染脚本关键差异

| 脚本 | 输出 | 可发布 |
|---|---|---|
| `render_互构谐变_v8.py` | base64 内联 HTML | ❌ |
| `render_互构谐变_v8_localimg.py` | 相对路径 HTML | ✅ |

## 配图规范

- **比例：** 21:9 (2.35:1) — 1260×540（正文图）/ 900×383（封面图）
- **风格：** cinematic industrial photography（影视感）
- **色板：** 暗金 + 暖橙 + 高对比 / 暖白照明
- **模型：** minimax-portal/image-01，aspectRatio=21:9，1 张 ≈ 1 积分
- **提示词模板：**
  ```
  [主题] + cinematic industrial photography + 暗金色调 + 暖白照明
  + no text, no labels, no signs, no watermarks + photorealistic, magazine-quality
  ```

## 5 张正文配图 + 1 张封面

- 5 张正文：每节一图（按 v7 铁律）
- 1 张封面：21:9（1260×540 → 900×383 传给微信）
- **关键：** 全部用相对路径引用 + 自动上传 CDN

## 踩坑时间线

- 10:47 老板要求入草稿箱 → 40164（IP 白名单）
- 10:52 老板加白 + 重跑入箱成功，但**配图没显示**
- 10:58 排查根因：base64 内联不处理
- 11:00 改用相对路径 + 重跑 → 5 张图全上传 CDN ✅

## 草稿箱工作流（修正版）

```
渲染 v*_pub.html（用相对路径）
   ↓
python publish_wechat.py <HTML> --cover-image <PNG> --author "老板" --title "..."
   ↓
dry-run 验证凭据
   ↓
真实入草稿箱
   ↓
老板人工群发（订阅号无 freepublish API 权限）
```

## 老板反馈

> 配图必须用相对路径，否则就是「写了但不显示」 — 老板 2026-06-29

---

*🦞 元子公众号图文系列 · 知识舱 · 04 配图发布铁律*