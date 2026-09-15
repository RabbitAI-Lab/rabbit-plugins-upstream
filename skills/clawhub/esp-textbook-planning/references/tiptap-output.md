# Tiptap 输出协议

生成、修改或修正格式前读取本协议。它约定普通聊天正文中的成果格式，不代表宿主已经执行程序校验。

成果对象必须且只包含以下三个字段：

- `schema`：固定为 `"esp.writing-plan-generated-step/1"`。需求分析、教材结构和编写方案统一使用此值；字段名是 schema，不是 schemaVersion。
- `title`：非空字符串，简洁概括本次成果的课程或专业方向及成果类型。标题依据实际资料填写，不能照抄示例中的专业。
- `data`：完整的 Tiptap JSON 文档对象，不是字符串、数组、Markdown 文本或语义蓝图。

这三个字段直接位于聊天输出 JSON 的最外层。data 根节点只包含 type 和 content，type 固定为 `"doc"`，content 为非空节点数组。不再套 stepDocument，也不增加 schemaVersion、targetStep、overview、units、commonSections 或 progression 等业务包装字段。

schema、title 不属于文档节点，不能复制到 data 中。文档内部标题使用 heading 节点。

### Tiptap 文档结构

data.content 只包含本次目标成果的完整内容，不把它声明为已经合并后的整份教材。第一个节点必须是一级标题，按本次成果分别使用“步骤1：需求分析”“步骤2：教材结构”或“步骤3：最终编写方案”。

### 前端属性与内容属性的边界

教师提供的 Tiptap 文档可能是编辑器导出的完整文档。读取它时理解其正文和结构；返回新生成、重新生成或修改后的成果时，只返回内容与必要的结构属性。

blockId、id、data-toc-id、textAlign 这四个字段由前端负责生成或管理，在本次输出的整个 data 节点树中必须省略。即使输入文档含有这些字段，也不得复制、生成、改名转存，或用 null、空字符串等值占位；标题、段落、列表、列表项及任意嵌套节点均遵守此规则。

省略这些字段不表示删除当前编辑器中的标识或对齐状态。成果应用时，由前端按其既有规则管理这些属性；模型不通过这些字段定位节点或输出局部修改补丁。

不要删除所有 attrs：heading 必须保留 attrs.level，orderedList 在需要指定起始序号时保留 attrs.start；表格单元格保留必要的 colspan、rowspan 等结构属性。去掉前端属性后，没有其他必要属性的节点直接省略 attrs，不输出空的 attrs 对象。

节点自身的 type、正文 text、content 数组和文本 marks 仍按下文保留，不能误当成前端生成字段删除。

参考文档可能同时包含三个步骤；它只提供格式和可用内容依据。教师只要求某一步时，仅返回该步骤的完整成果，不因参考文档包含其他步骤而一并输出，也不照搬其中的专业、课时或单元数量作为当前课程事实。

### 节点规则

允许使用的节点为 doc、heading、paragraph、bulletList、orderedList、listItem、text、blockquote、hardBreak、table、tableRow、tableHeader、tableCell。根据内容需要选用，不要求每份成果包含所有节点，也不因为示例包含表格或引用而强行添加。

1. 每个节点都是对象，type 始终是节点名称字符串。type、attrs、content 属于同一节点的同级字段。所有节点的 content 只要出现就必须是数组，不能用单个对象、字符串或 null 替代。
2. doc 只作为 data 根节点。其 content 只能直接包含 heading、paragraph、bulletList、orderedList、blockquote、table，不能直接包含 text、hardBreak、listItem 或表格行与单元格，也不能嵌套另一个 doc。
3. heading 的 attrs 只包含 level，例如 `{"level":1}`。一级标题使用 1，内部标题使用 2—4。标题 content 为非空 text 节点数组。
4. 有正文的 paragraph 使用 text 节点组成 content，不输出 attrs。段内确需强制换行时，在两个 text 节点之间使用 `{"type":"hardBreak"}`，不添加 attrs、text 或 content；不同段落仍使用独立 paragraph。确需保留空段落时，可以使用 `{"type":"paragraph"}`；不要创建空 text 节点，也不要用空段落代替应当生成的内容。
5. bulletList 和 orderedList 的 content 是非空 listItem 数组。每个 listItem 的 content 是非空数组，第一项必须为 paragraph，之后可以包含段落或嵌套列表，不能直接放置 text。列表文字遵循 listItem → paragraph → text 的结构。
6. bulletList 和 listItem 不输出 attrs；orderedList 可通过 attrs.start 指定正整数起始序号，例如 `{"start":1}`，不需要指定时可省略 attrs，默认从 1 开始。
7. text 必须包含非空 text 字符串，可选 marks 是对象数组，每项只包含 type，允许 bold、italic、strike、code，例如 `{"type":"bold"}`。text 节点不含 attrs 或 content；非 text 节点不含 text 或 marks。
8. 不为不同节点复制同一份 attrs；按上述属性边界保留各节点实际需要的结构和文字格式。
9. 使用节点和 marks 表达格式，不用 HTML 标签或 Markdown 格式符号代替。保持 JSON 值合法，不能用 undefined、NaN 或省略号作为结构占位符。
10. 不生成 revision、哈希或其他正式标识，不以示例中的课程、课时或学生情况作为当前事实。
11. blockquote 不输出 attrs，content 为非空 paragraph 数组，用于确有需要的引用或独立说明。其文字仍放在 paragraph 的 text 节点中，不直接放在 blockquote 下；不要编造引文或来源。
12. table 不输出 attrs，content 为非空 tableRow 数组；tableRow 不输出 attrs，content 为非空 tableHeader 或 tableCell 数组。表头使用 tableHeader，普通单元格使用 tableCell，单元格内部使用 paragraph，文字置于 paragraph 的 text 节点中。
13. 普通表格单元格的 attrs 使用 `{"colspan":1,"rowspan":1}`，各行列数保持一致。仅在真实内容要求合并时使用大于 1 的跨度，并保证网格完整。colwidth、align 属于可选布局属性，无明确需求时省略；不复制导出文件中的空布局属性。表格行、单元格及其内部段落同样不得带前端生成的四个字段。

不能只返回标题、摘要、空数组或占位节点代替完整成果。

## JSON 语法检查

正确转义字符串中的引号、换行和反斜杠。不得输出尾逗号、undefined、NaN 或省略号占位。最终对象不得被序列化为字符串，也不得以 Markdown 代码围栏包裹。
