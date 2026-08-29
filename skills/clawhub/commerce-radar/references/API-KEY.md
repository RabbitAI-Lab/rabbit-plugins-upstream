# API Key 配置


```bash
export COMMERCE_RADAR_API_KEY="ais_..."
export AI_SKILLS_API_URL="https://ai-skills.open-idea.net" # 可选，仅站点根
```

请求根地址必须这样构造，不能把 `/api/v1` 放进覆盖变量：

```bash
SITE_ROOT="${AI_SKILLS_API_URL:-https://ai-skills.open-idea.net}"
API_ROOT="${SITE_ROOT%/}/api/v1"
```

每次请求使用：

```text
Authorization: Bearer $COMMERCE_RADAR_API_KEY
```

Key 仅用于 Commerce Radar，其 abilities 为 `product.search`、`product.detail`、
`store.analyze`、`report.create`。Key 缺失时引导用户在平台创建；不要要求用户在对话中
粘贴 Key，也不要把它写入请求体、日志、结果或产物。
