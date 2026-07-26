---
name: word-template-filler
description: Word模板智能填充工具。解析Word模板中的{{占位符}}，AI生成主题内容并填充模板生成新文档。触发场景：(1) 用户上传Word模板需要填充内容 (2) 处理包含占位符的Word文档 (3) 批量生成基于模板的文档 (4) 关键词：模板填充、Word模板、占位符、文档生成、{{}}替换。
---

# Word 模板填充器

自动解析 Word 模板中的 `{{占位符}}`，根据用户指定主题 AI 生成内容，填充并生成新文档。

## 工作流程

```
用户上传模板 → 解析占位符 → AI生成内容 → 填充模板 → 上传返回链接
```

## 使用方法

### 1. 解析模板占位符

当用户提供 Word 模板文件时，首先解析占位符：

```bash
python3 scripts/parse_template.py <模板文件.docx>
```

返回示例：
```json
{
  "success": true,
  "placeholders": ["标题", "正文内容", "日期", "作者"],
  "count": 4
}
```

### 2. AI 生成内容

根据用户描述的主题，为每个占位符生成合适内容。示例提示：

> 用户主题：「新产品发布会邀请函」
> 
> 占位符：标题、正文内容、日期、作者
> 
> 生成内容：
> - 标题：诚邀莅临「创新未来」新品发布会
> - 正文内容：尊敬的嘉宾...

### 3. 填充模板

使用生成的内容填充模板：

```bash
python3 scripts/fill_template.py <输入模板.docx> <输出文件.docx> '{"占位符名": "填充内容"}'
```

JSON 内容需要正确转义，建议写入临时文件：

```bash
python3 scripts/fill_template.py input.docx output.docx "$(cat values.json)"
```

### 4. 上传并返回链接

使用 `uploader` 技能上传生成的文件，返回公开下载链接。

## 端到端示例

用户请求：
> 这是一个合同模板，帮我填充一份「软件开发服务合同」，甲方是星云科技，乙方是智创数码

执行步骤：

1. **解析模板**：运行 `parse_template.py` 获取占位符列表
2. **生成内容**：根据合同类型、甲乙方信息生成各字段内容
3. **填充模板**：运行 `fill_template.py` 生成新文档
4. **上传文件**：调用 uploader 技能获取下载链接
5. **返回结果**：告知用户下载链接

## 依赖与环境设置

需要 `python-docx` 库。首次使用前设置虚拟环境：

```bash
# 创建虚拟环境（只需一次）
python3 -m venv /root/.openclaw/workspace/skills/word-template-filler/.venv

# 安装依赖
/root/.openclaw/workspace/skills/word-template-filler/.venv/bin/pip install python-docx

# 后续使用虚拟环境的 Python
/root/.openclaw/workspace/skills/word-template-filler/.venv/bin/python scripts/parse_template.py <文件>
```

## 占位符格式

支持的占位符格式：
- `{{变量名}}` - 标准格式
- `{{ 变量名 }}` - 支持空格
- 占位符区分大小写

## 注意事项

- 填充时会保留原始文档格式（字体、样式、表格结构）
- 未提供值的占位符保持原样
- 复杂格式（文本框、艺术字）可能需要特殊处理
