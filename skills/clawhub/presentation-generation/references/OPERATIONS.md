# 操作字段、大纲与导出

## 整理演示材料

`presentation.inspect` 接收 `brief` 或最大 10 MiB 的 TXT、Markdown、DOCX、PDF、CSV、XLSX。文件加密、按用户隔离并七日过期；PDF 只读本地文字层，不调用收费 OCR。结果保留 section ID、原位置、表格行引用、指纹和局限。

## 生成并审核大纲

`presentation.outline` 接收当前用户七日内成功的 `inspect_task_id`、`audience`、`purpose`、6–15 的 `slide_count`、`theme` 与可选 `instructions`。主题限 `clear`、`midnight`、`warm`；版式限 `title`、`section`、`bullets`、`two-column`、`quote`、`metric-cards`、`table`、`chart`、`timeline`、`summary`。数字结论必须引用已知 section ID。

## 生成文件

`presentation.generate` 接收当前用户成功的 `outline_task_id`、可选 `outline_edits` 与 `formats`。编辑限标题、顺序、正文、要点、备注和版式；格式限 `pptx`、`pdf`、`png`。生成阶段不调用模型，只使用内置主题、本地字体和锁定版本渲染器。
