# 各识别类型的字段说明（elements 内容）

根据 ocrType 不同，返回的 `elements` 对象包含以下字段：

## TABLE_RECOGNITION (表格识别)

- `tables`: 表格列表，List<Object>
- `type`: 表格类型（wired_table 有线表格；wireless_table 无线表格），String
- `bbox`: 表格坐标位置，[x1, y1, x2, y2]，分别为左上和右下坐标，List<Integer>
- `html`: 表格识别内容，html格式，String
