# 微信公众号 Markdown 发布助手

## Metadata

- **name**: wechat-publisher
- **description**: 将 Markdown 文章自动转换为微信公众号格式并发布到草稿箱，支持图片上传、HTML 转换、access_token 管理
- **version**: sha256:1a2b3c4d5e6f
- **language**: zh-CN

---

## 触发短语

用户说出以下任意一句话时，激活此 Skill：

1. "发布到微信公众号"
2. "发到公众号"
3. "微信公众号发布"
4. "发公众号文章"
5. "帮我发微信"
6. "写公众号文章"
7. "微信公众号草稿"
8. "发布微信文章"
9. "微信图文发布"
10. "用 Markdown 发公众号"

---

## 功能列表

此 Skill 提供以下能力：

1. **Markdown → 微信 HTML 转换**：将标准 Markdown 转换为微信公众号支持的 HTML 格式
2. **access_token 管理**：自动获取和刷新微信公众号调用凭证
3. **封面图片上传**：上传封面图并获取永久 media_id（thumb_media_id）
4. **文章图片上传**：上传文章内所有图片，返回微信可用的图片 URL
5. **草稿箱创建**：将转换后的 HTML 内容提交到微信草稿箱
6. **图文发布**：将草稿箱中的草稿正式发布到公众号
7. **多图文支持**：支持单图文和多图文（多个 article 节点）

---

## 使用前提

使用此 Skill 前，必须准备以下信息：

| 所需项 | 说明 | 获取方式 |
|--------|------|----------|
| AppID | 微信公众号应用唯一标识 | 微信公众平台 → 设置与开发 → 基本配置 |
| AppSecret | 微信公众号应用密钥 | 同上（需重置后获取） |
| access_token | API 调用凭证 | 通过 AppID + AppSecret 自动获取 |
| 草稿箱权限 | 账号需有草稿箱功能 | 服务号默认有，订阅号部分有 |
| 发布权限 | 账号需有群发权限 | 需已认证的公众号 |

**注意**：个人主体账号、企业主体未认证账号（2025年7月起）可能被回收 API 调用权限。

---

## 详细操作步骤

### 第一步：获取 access_token

access_token 是调用所有微信 API 的凭证，有效期 2 小时（7200 秒）。

**调用方式**：
```
GET https://api.weixin.qq.com/cgi-bin/token
?grant_type=client_credential
&appid=你的AppID
&secret=你的AppSecret
```

**返回示例**：
```json
{
  "access_token": "ACCESS_TOKEN",
  "expires_in": 7200
}
```

**刷新逻辑**：
- 每次调用前检查 token 是否过期（剩余时间 < 300 秒则刷新）
- 将 token 缓存到 `~/.openclaw/workspace/memory/wechat_token.json`
- 格式：`{"token": "...", "expires_at": 1234567890}`

### 第二步：上传封面图（获取 thumb_media_id）

封面图必须使用**永久** media_id，因此需通过 `media/upload` 上传为永久素材。

**调用方式**：
```
POST https://api.weixin.qq.com/cgi-bin/media/upload
?access_token=ACCESS_TOKEN
&type=thumb
```

**请求体**：multipart/form-data，字段名 `media`，文件为图片（jpg/png，最大 2MB）

**返回示例**：
```json
{
  "media_id": "THUMB_MEDIA_ID",
  "url": "http://mmbiz.qpic.cn/..."
}
```

**重要**：`thumb_media_id` 必须是永久 media_id，否则新建草稿接口会报错。

### 第三步：上传文章内图片（获取可用 URL）

**这是最容易出错的一步！**

微信公众号文章中的图片**必须**使用微信图床 URL，外部 URL（如七牛、阿里云OSS等）会被过滤，导致图片不显示。

**调用方式**：
```
POST https://api.weixin.qq.com/cgi-bin/media/uploadimg
?access_token=ACCESS_TOKEN
```

**请求体**：multipart/form-data，字段名 `media`，图片文件

**返回示例**：
```json
{
  "url": "https://mmbiz.qlogo.cn/mmbiz/..."
}
```

返回的 `url` 即为可在文章中使用的图片地址。

### 第四步：Markdown → 微信 HTML 转换

#### 转换规则表

| Markdown 语法 | 微信 HTML | 说明 |
|---------------|-----------|------|
| `# 一级标题` | `<h1>一级标题</h1>` | 微信 h1 字体较大 |
| `## 二级标题` | `<h2>二级标题</h2>` | 推荐使用 h2 |
| `### 三级标题` | `<h3>三级标题</h3>` | h3 字体与正文相近 |
| `**加粗**` | `<strong>加粗</strong>` | 或 `<b>` |
| `*斜体*` | `<em>斜体</em>` | 或 `<i>` |
| `` `行内代码` `` | `<code>行内代码</code>` | 灰色背景代码 |
| ````` ```代码块``` ``` `` | `<section class="code-snippet"><pre>代码块</pre></section>` | 代码段样式 |
| `---` | `<hr/>` | 分隔线 |
| `[链接文字](url)` | `<a href="url">链接文字</a>` | 支持外部链接 |
| `![图片](url)` | `<p><img src="替换后的微信URL" /></p>` | **url 需替换为上传后的微信地址** |
| `> 引用文字` | `<blockquote>引用文字</blockquote>` | 灰色背景块 |
| `- 无序列表项` | `<ul><li>无序列表项</li></ul>` | |
| `1. 有序列表项` | `<ol><li>有序列表项</li></ol>` | |
| `--- 表格 ---` | `<table>...</table>` | 需转换为 table 标签 |
| 换行 | `<br/>` | 段间需手动加空行 |

#### 代码块特殊处理

微信编辑器对 `<pre>` 和 `<code>` 支持较好，建议：

```html
<section class="code-snippet">
  <pre><code>你的代码内容</code></pre>
</section>
```

#### 注意事项

- **图片 URL 必须替换**：所有 `![img](外部URL)` 必须先上传到微信图床，用返回的 URL 替换
- **不支持的标签**：`script`、`style`、`iframe`、`object`、`embed` 会被移除
- **不支持的 CSS**：复杂 CSS（如 `position:fixed`、动画等）会被移除
- **字符限制**：标题 ≤ 32 字，作者 ≤ 16 字，摘要 ≤ 128 字
- **内容大小**：最终 HTML 内容不超过 2KB（注意是最终 HTML，不是 Markdown 源）

### 第五步：创建草稿

**调用方式**：
```
POST https://api.weixin.qq.com/cgi-bin/draft/add
?access_token=ACCESS_TOKEN
```

**请求体**：
```json
{
  "articles": [
    {
      "title": "文章标题",
      "author": "作者名",
      "digest": "摘要（不填则自动取前54字）",
      "content": "<h1>文章内容HTML</h1><p>...</p>",
      "content_source_url": "https://原始链接.com",
      "thumb_media_id": "永久封面图media_id",
      "need_open_comment": 1,
      "only_fans_can_comment": 0
    }
  ]
}
```

**返回示例**：
```json
{
  "media_id": "媒体ID，可用于发布"
}
```

### 第六步：发布草稿（可选）

将草稿箱中的内容正式发布到公众号。

**调用方式**：
```
POST https://api.weixin.qq.com/cgi-bin/freepublish/submit
?access_token=ACCESS_TOKEN
```

**请求体**：
```json
{
  "media_id": "草稿的media_id"
}
```

**返回示例**：
```json
{
  "publish_id": 12345,
  "msg_data_id": 12345
}
```

**发布后**：
- 草稿箱中的该草稿会被自动移除
- 发布任务进入审核队列（部分类型需审核）
- 可通过 `/cgi-bin/freepublish/get` 查询发布状态

---

## 输出格式

用户使用此 Skill 后，会得到以下输出：

1. **access_token 状态**：获取成功/失败原因
2. **图片上传结果**：每张图片的微信 URL 映射表
3. **封面图结果**：thumb_media_id
4. **HTML 转换结果**：预览转换后的 HTML（可选输出）
5. **草稿创建结果**：
   - 成功：返回 `media_id`，告知草稿已加入草稿箱
   - 失败：返回具体错误码和解决方案
6. **发布结果**（如选择发布）：返回 `publish_id` 和状态

---

## 示例对话

### 示例一：发布单篇文章

**用户**：帮我把这篇 Markdown 发到微信公众号草稿箱

```markdown
# 我的第一篇公众号文章

这是一篇测试文章。

## 准备工作

首先你需要：
- 一个微信公众号
- AppID 和 AppSecret

## 代码示例

这是一个代码块：

```javascript
console.log('Hello WeChat!');
```

> 这是引用文字。
```

**AI 回复**：

```
📤 正在发布到微信公众号...

✅ 第一步：获取 access_token
   Token: 有效（剩余 6800 秒）

✅ 第二步：上传封面图
   media_id: Bxxxxxxxxx
   URL: https://mmbiz.qlogo.cn/...

✅ 第三步：处理文章图片
   发现 0 张外部图片，跳过

✅ 第四步：Markdown → HTML 转换
   标题：我的第一篇公众号文章
   作者：未填写（可选）
   摘要：自动截取前54字

✅ 第五步：创建草稿
   media_id: Gxxxxxxxxx

🎉 完成！草稿已加入微信草稿箱。
   前往 https://mp.weixin.qq.com 检查并发布。
```

### 示例二：处理含外部图片的文章

**用户**：发一篇公众号，图片在七牛云上

```markdown
![封面图](https://cdn.example.com/cover.jpg)

这是正文内容，包含一张截图：

![截图](https://qiniu.example.com/screenshot.png)
```

**AI 回复**：

```
📤 正在发布到微信公众号...

✅ 获取 access_token

⚠️ 检测到 2 张外部图片，正在上传到微信图床...

   图片1 (cover.jpg):
   ✅ 上传成功 → https://mmbiz.qpic.cn/...
   
   图片2 (screenshot.png):
   ✅ 上传成功 → https://mmbiz.qpic.cn/...

✅ HTML 转换完成（已替换所有图片URL）
✅ 草稿创建成功：media_id = Gxxxxxxxxx

🎉 完成！共上传 2 张图片到微信图床。
```

### 示例三：发布并直接群发

**用户**：把这篇文章发到公众号并发布（不是只存草稿）

**AI 回复**：

```
📤 正在发布到微信公众号...

✅ access_token: 有效
✅ 封面图: 已上传 (thumb_media_id: Bxx)
✅ 文章图片: 已处理
✅ HTML: 已转换
✅ 草稿: 已创建 (media_id: Gxx)

📢 正在提交发布...

⚠️ 注意：发布后需等待微信审核，部分内容可能被拦截。
   发布任务 ID: 12345

🎉 草稿已提交发布！
   状态查询：可使用 /cgi-bin/freepublish/get 接口
```

---

## 安装配置步骤

### 步骤一：获取 AppID 和 AppSecret

1. 登录 [微信公众平台](https://mp.weixin.qq.com)
2. 进入「设置与开发」→「基本配置」
3. 找到 AppID 和 AppSecret（如未显示，点击重置）
4. **注意**：AppSecret 只有一次完整显示的机会，请妥善保存

### 步骤二：在 OpenClaw 中配置

创建配置文件 `~/.openclaw/workspace/memory/wechat_config.json`：

```json
{
  "appid": "wx_your_appid_here",
  "appsecret": "your_appsecret_here"
}
```

同时将以下信息写入 `TOOLS.md` 以便 Skill 读取：

```
### 微信公众号
- appid: wx_xxxxx
- appsecret: （已加密存储在 wechat_config.json）
- token缓存: ~/.openclaw/workspace/memory/wechat_token.json
```

### 步骤三：验证配置

让 AI 执行一次「获取 access_token」测试，确认配置正确。

### 步骤四：设置封面图默认来源（可选）

在 `wechat_config.json` 中可指定默认封面图路径：

```json
{
  "appid": "wx_xxx",
  "appsecret": "xxx",
  "default_thumb": "/path/to/default_cover.jpg"
}
```

---

## 注意事项

### API 限制

| 接口 | 限制 |
|------|------|
| access_token | 每日获取次数有限（约 2000 次），必须缓存复用 |
| 新增草稿 | 内容 HTML ≤ 2KB，字符 ≤ 2万，文件 ≤ 1M |
| 上传图片（正文用） | 图片 ≤ 10M，支持 jpg/png |
| 上传封面图 | ≤ 2MB，仅 jpg/png |
| 发布接口 | 个人/未认证账号可能无权限（2025年7月起） |

### HTML 转换规则重点

1. **图片必须上传到微信图床**：所有外部图片 URL 必须通过 `media/uploadimg` 上传并替换
2. **不支持的标签会被移除**：JavaScript、CSS 动画、iframe 等
3. **代码块用 `<pre><code>`**：这是微信对代码最友好的格式
4. **标题层级**：建议 h2 作为文章内一级标题，h3 作为二级，避免用 h1（微信会渲染得非常大）

### 常见错误及解决

| 错误码 | 含义 | 解决方案 |
|--------|------|----------|
| 40001 | access_token 无效 | 重新获取 token，检查 AppID/AppSecret |
| 40007 | thumb_media_id 无效 | 确认封面图是永久 media_id，而非临时 |
| 40013 | AppID 无效 | 检查配置文件中的 AppID |
| 40125 | AppSecret 无效 | 重置 AppSecret |
| 44002 | 空 content | 转换后的 HTML 为空，检查 Markdown 内容 |
| 44004 | 草稿数超限 | 删除草稿箱中的旧草稿 |
| 53404 | 账号被限制带货 | 删除商品信息后重试 |

### 安全建议

1. **AppSecret 不要写入代码**：统一放在 `wechat_config.json`，并加入 `.gitignore`
2. **token 缓存文件权限**：设为 `600`（仅本人可读写）
3. **不要在群聊中分享草稿内容**：确认发布的文章内容无误后再发布

---

## 附：完整 API 速查

```
获取 access_token:
  GET https://api.weixin.qq.com/cgi-bin/token
  ?grant_type=client_credential&appid=APPID&secret=APPSECRET

上传文章图片（图床）:
  POST https://api.weixin.qq.com/cgi-bin/media/uploadimg
  ?access_token=TOKEN

上传封面图（永久素材）:
  POST https://api.weixin.qq.com/cgi-bin/media/upload
  ?access_token=TOKEN&type=thumb

新建草稿:
  POST https://api.weixin.qq.com/cgi-bin/draft/add
  ?access_token=TOKEN

发布草稿:
  POST https://api.weixin.qq.com/cgi-bin/freepublish/submit
  ?access_token=TOKEN
```

---

**版本**：v1.0  
**作者**：OpenClaw CCD  
**适用平台**：OpenClaw + 微信公众号服务号  
**最后更新**：2026-07-04
