# content-writer - 自媒体文章写作助手

_帮你完成自媒体文章全流程：选题、查资料、写文章、配图、排版、发布_

## 触发条件

用户说"写文章"、"自媒体"、"公众号"、"小红书"、"发文章"、"创作"等相关意图时激活。

---

## 完整流程

### 第1步：确定写作方向

**询问用户要写什么方向**，关键词是什么（支持逗号分隔多个）。

> 示例提问："你想写什么主题的文章？输入关键词，比如：职场、效率、副业"

### 第2步：热门选题

根据用户输入的关键词（支持逗号分隔），**搜索热门选题**：

**搜索工具（推荐 ddgs，免费）：**
```python
from ddgs import DDGS
ddgs = DDGS()
results = ddgs.text("关键词 平台 热门", max_results=5)
```

**搜索命令示例：**
```bash
# 搜索小红书热门
python3 -c "
from ddgs import DDGS
ddgs = DDGS()
for r in ddgs.text('关键词 小红书 热门', max_results=5):
    print(r['title'], '|', r['href'])
"

# 搜索公众号热门
python3 -c "
from ddgs import DDGS
ddgs = DDGS()
for r in ddgs.text('关键词 公众号 热门', max_results=5):
    print(r['title'], '|', r['href'])
"

# 搜索知乎热门
python3 -c "
from ddgs import DDGS
ddgs = DDGS()
for r in ddgs.text('关键词 知乎 热门', max_results=5):
    print(r['title'], '|', r['href'])
"
```

**输出**：提供5个热门选题，并推荐1-2个，最终由**用户确定具体选题**。

### 第3步：查找资料

根据选定选题，**使用 web_search + web_fetch 收集资料**：

1. 搜索相关高质量内容
2. 使用 web_fetch 抓取关键页面内容
3. 整理成参考资料摘要

> 优先使用用户已配置的模型（如 Kimi）进行资料整理和文章生成。

### 第4步：生成文章

根据资料**生成 Markdown 文章**，包含：
- 吸引人的标题
- 开头引入
- 主体内容（分章节，建议5-6个章节）
- 总结/互动引导

**生成后询问用户保存方式**：
1. 保存到电脑本地（默认下载文件夹 ~/Downloads/）
2. 保存到飞书文档
3. 保存到 Obsidian（如果安装）

**Obsidian 路径检测**：
```bash
ls -la ~/Library/Application\ Support/obsidian/ 2>/dev/null || ls -la ~/Obsidian/ 2>/dev/null
```

### 第5步：文章调整

- 如果文章不合适，**根据用户反馈进行修改**
- 用户说"调整XX部分"、"修改XX"、"重写XX"等，定位并更新对应内容

### 第6步：配图（重要）

**配图是文章的重要部分，需要认真对待：**

#### 6.1 确认风格

**先让用户选择风格**，展示7张示例图供预览：

1. **手写手账** - examples/1-handwritten-journal.jpg
2. **板报风格** - examples/2-blackboard-style.jpg
3. **科技版式** - examples/3-tech-style.jpg
4. **日常科普** - examples/4-flat-edu-style.jpg
5. **扁平简约** - examples/5-minimalist-style.jpg
6. **孟菲斯** - examples/6-memphis-style.jpg
7. **蒸汽波** - examples/7-vaporwave-style.jpg

> 发送示例图给用户预览，用户选择后，用该风格生成实际配图

**确认风格时的话术**：
> 「你想用哪种风格？是否需要看一下示例图？」

#### 6.2 确认布局和尺寸

**默认配置**：
- 布局：混合布局（mixed layout）
- 风格：Corporate-memphis
- 尺寸：16:9 横屏（2K 或 1920x1080）

> 询问用户是否需要调整默认配置。

#### 6.3 生成配图

**为每个章节生成一张配图**，使用火山引擎 API：

```bash
curl -X POST "https://ark.cn-beijing.volces.com/api/v3/images/generations" \
  -H "Authorization: Bearer $VOLCENGINE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "doubao-seedream-5-0-260128",
    "prompt": "描述内容（根据章节主题）",
    "response_format": "url",
    "size": "2K"
  }'
```

**配图生成规则**：
1. 根据每个章节主题生成对应的配图
2. 配图插入到对应章节的标题后面、第一个段落前面
3. 统一使用淡紫色系配色（#9B8AA5, #C9A8D4）

#### 6.4 自动裁剪去水印

**重要**：AI 生成的图片底部可能有水印，需要自动裁剪：

```python
from PIL import Image

def crop_watermark(image_path, output_path, crop_ratio=0.8):
    """裁剪掉图片底部约20%（去水印区域）"""
    img = Image.open(image_path)
    width, height = img.size
    new_height = int(height * crop_ratio)
    img_cropped = img.crop((0, 0, width, new_height))
    img_cropped.save(output_path, quality=95)
```

> 裁剪比例建议 80%（去掉底部20%），根据实际水印位置调整。

### 第7步：排版与发布

#### 7.1 排版选项

**标题样式**：
- 居中/左对齐
- 背景覆盖文字部分（不整行覆盖）
- 配色：跟随图片色系 或 用户自定义

**配色方案**：
- 用户可自定义配色（如需提供RGB色号）

**排版确认时的话术**：
> 「标题居中还是左对齐？配色用哪种？可以提供RGB色号」

**段落间距**：紧凑 / 标准 / 宽松

**重点标记**：加粗 / 高亮（使用与标题一致的配色）

#### 7.2 输出格式

生成 HTML 文件（可在浏览器打开预览），包含：
- 标题样式（CSS）
- 章节配图（插入对应位置）
- 引用块样式
- 重点内容高亮
- **章节之间不使用横线分隔**

#### 7.3 发布

询问用户：
1. **一键复制**：生成可直接粘贴到公众号的内容
2. **保存本地**：HTML 文件保存在 Downloads 文件夹
3. **飞书**：保存到飞书文档

---

## 文件结构

```
~/skills/content-writer/
├── SKILL.md           # 主技能文件
├── prompts.md         # 提示词模板
├── reference/
│   ├── templates.md   # 文章模板
│   └── styles.md     # 配图风格指南
└── examples/         # 风格示例图
```

---

## 模型调用

- **写文章**：优先使用用户已配置的模型（Claude Opus > Kimi > minimax > Gemini）
- **查资料**：web_search + web_fetch
- **配图**：火山引擎 doubao-seedream-5-0（推荐）

---

## API 配置

### 图片生成 API（用户可自行配置）

支持多种图片生成API，用户可根据需要配置：

#### 方案1：火山引擎 Seedream 5.0（推荐）

| 配置项 | 值 |
|--------|-----|
| 端点 | `https://ark.cn-beijing.volces.com/api/v3/images/generations` |
| 模型 | `doubao-seedream-5-0-260128` |
| 环境变量 | `VOLCENGINE_API_KEY` |
| 参数 | `size: "2K"`, `response_format: "url"` |

```bash
# 设置API Key
export VOLCENGINE_API_KEY="你的Key"
```

#### 方案2：OpenAI DALL-E 3

| 配置项 | 值 |
|--------|-----|
| 环境变量 | `OPENAI_API_KEY` |
| 模型 | `dall-e-3` |
| 参数 | `size: "1024x1024"` |

#### 方案3：Google Gemini Image

| 配置项 | 值 |
|--------|-----|
| 环境变量 | `GEMINI_API_KEY` |
| 模型 | `gemini-2.0-flash-exp` |

#### 方案4：Stability AI

| 配置项 | 值 |
|--------|-----|
| 环境变量 | `STABILITY_API_KEY` |
| 模型 | `stable-diffusion-xl-1024-v1-0` |

#### 方案5：nano-banana (Banana Studio)

| 配置项 | 值 |
|--------|-----|
| 环境变量 | `NANO_BANANA_API_KEY` |
| 模型 | `banana-v2` |
| 端点 | `https://api.banana.sh/v1/image/generate` |

#### 方案6：Replicate (支持多种模型)

| 配置项 | 值 |
|--------|-----|
| 环境变量 | `REPLICATE_API_KEY` |
| 支持模型 | stable-diffusion, flux, playground-v2 等 |

#### 方案7：Midjourney (通过Discord)

需配置 Discord Bot 或使用第三方 API 服务

### 用户配置流程

当用户需要使用图片生成功能时：

1. **询问用户**：「你想用哪个图片生成模型？」

2. **用户提供**：
   - 模型名称（如 nano-banana, DALL-E 3 等）
   - API Key 获取方式/文档链接

3. **复制接口文档**：请用户提供 API 文档链接或直接粘贴接口说明

4. **配置并测试**：获取 API Key 后进行测试生成

**示例对话**：
```
用户：我要用nano-banana生成图片
助手：请提供你的 nano-banana API Key，以及API文档链接
用户：API Key是 xxx，文档在 https://...
助手：好的，我来配置并测试...
```

### 搜索 API（热门选题）

**ddgs (DuckDuckGo) - 推荐（免费）：**
```bash
pip install ddgs
```

```python
from ddgs import DDGS
ddgs = DDGS()
results = ddgs.text("关键词", max_results=5)
```

**备选方案：**
- Brave Search：需要 `BRAVE_API_KEY`
- Tavily：需要 API key

### 公众号发布（可选）

在 `TOOLS.md` 中添加：

```markdown
### 公众号
- appid: xxx
- secret: xxx
```

---

## 注意事项

1. **配图流程**：
   - 先确认风格（提供选项）
   - 再确认布局尺寸（默认 corporate-memphis, 16:9）
   - 每个章节生成对应配图
   - 自动裁剪去水印（底部约20%）
   - 插入到对应章节段落前

2. **配色一致性**：
   - 排版配色跟随配图色系
   - 标题、强调、边框使用统一配色

3. **发布前确认**：
   - 让用户预览最终效果
   - 确认后再复制或发布

4. **文章结构**：
   - 建议5-6个章节
   - 每个章节至少一个案例
   - 结尾有互动引导
