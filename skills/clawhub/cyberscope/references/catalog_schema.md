# 目录数据模型与保真锚点（供参考 · 定性）

> 单一数据源：`data/catalog.json`（v2.0.0 由 v1.0.0 的 `src/lib/seed-data.ts` 忠实移植；
> v1 文件 SHA-256 `8c4597e63d8d94c782fbf9cd46542096012cd721941239666b35ac967149dd3b`
> 与 v1 README 声明一致，已核验）。

## 结构（schema_version: 2）

```
catalog = {
  schema_version: 2,
  catalog_name: "cyberscope",
  description: str,
  usage_rules: ["reference-only","lawful-use","no-weaponization","cite-dont-amplify"],
  categories: [{numeral "I".."X", name, slug, sortOrder 1..10}]          # 10 条
  methods:    [{methodNumber 1..62 唯一, categorySlug→categories.slug,
                title, description, keywords[str[]]}]                     # 62 条
  resources:  [{methodNumber→methods 外键, title, url(https), source,
                resourceType, description}]                               # 83 条，45 个不同 source
}
```

## 规模事实（自检锚定值）

- 10 类目 / 62 方法 / 83 资源 / 45 个不同来源；每方法 ≥1 资源。
- 单来源方法 43 个；重复 URL 恰 1 个（`freedomhouse.org/report/freedom-net` 用于 m33+m41）；
  ATT&CK 子技术 URL 用斜杠形式的 2 条（m30 `T1584/002`、m48 `T1195/002`；
  ATT&CK 规范 URL 为点号形式 `T1584.002`）。

## 保真锚点（selftest G1/G5 断言）

- 方法规范摘要：按 methodNumber 序拼接
  `"%d|%s|%s|%s\n" % (methodNumber, title, description, ",".join(sorted(keywords)))` 的 SHA-256
  = `32e47ddadd169a9af554f42fdd459fd658d64ec65f8294df23754c0c5b7e03ea`
- 资源规范摘要：按数组序拼接
  `"%d|%s|%s|%s|%s\n" % (methodNumber, title, url, source, resourceType)` 的 SHA-256
  = `62c22f3b51e27073b5ad6ef54d66c90cee7c28081203696fdb796a8eeb41001e`
- `checksums` 命令另给 `file_sha256`（文件字节，格式敏感）。
- 规范摘要对字段内容敏感、对 JSON 排版不敏感 → 改数据必变锚点，改排版不变。
- **锚点覆盖边界**：方法摘要覆盖 methodNumber/title/description/keywords；资源摘要覆盖
  methodNumber/title/url/source/resourceType——**不含 resources.description**。篡改资源描述文字
  不会改变锚点（锚点钉身份：哪条方法、什么标题、什么 URL、什么来源，而非描述措辞）。

## 路径

- 默认读 `<skill>/data/catalog.json`；环境变量 `CYBERSCOPE_CATALOG` 可指向其他 catalog
  （用于测试/扩展数据集；结构须满足上述 schema，否则退出码 3）。
