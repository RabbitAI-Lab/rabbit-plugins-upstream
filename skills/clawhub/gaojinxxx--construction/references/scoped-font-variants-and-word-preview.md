# 局部字体变体与真实 Word 预览

适用：用户要求将现有施工日志的施工内容栏改成手写体，并发送效果预览。此流程不改变日志事实或默认归档模板。

## 1. 发现字体、限定修改范围

Windows可读取字体注册表，按字体名称筛选中文行楷、楷体等，避免设置不存在的字体后静默替代：

```python
import winreg
key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
    r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts')
for i in range(winreg.QueryInfoKey(key)[1]):
    name, value, _ = winreg.EnumValue(key, i)
    if any(s in name.lower() for s in ('xing', 'kai', '行楷', '楷体', '手写')):
        print(name, value)
```

- 已安装时，华文行楷可作为自然中文手写效果的首个试样；不代表用户已指定该字体为长期默认。
- 中文内容不应只用英语手写字体；必须检查中文实际显示。
- C01-8的施工内容默认是第一个表格 Row 4，包含现场情况、材料、机械、人员。只修改该合并单元格一次。
- 原文件另存新变体；保持字号、文本、换行、行高、页边距和其他栏位不变。

```python
from docx import Document
from docx.oxml.ns import qn

doc = Document(source)
for para in doc.tables[0].rows[4].cells[0].paragraphs:
    for run in para.runs:
        if not run.text:
            continue
        run.font.name = '华文行楷'
        rf = run._element.get_or_add_rPr().get_or_add_rFonts()
        for attr in ('ascii', 'hAnsi', 'eastAsia', 'cs'):
            rf.set(qn('w:' + attr), '华文行楷')
doc.save(target)
```

不要重新设置 cell.text，也不要运行“所有行强制宋体”的生成后清理脚本覆盖本次有意设置的字体。

## 2. 验证只改了目标字体

- 编辑前记录源文件哈希，编辑后确认源文件哈希不变。
- 重读输出：Row 4文本及字号与源文件一致；四类字体属性为目标字体。
- 对Row 0、1、2、3、5逐行比较 `_tr.xml`，应与源文件完全一致。
- 若其他属性发生变化，先修复再交付。

## 3. 使用实际排版引擎渲染

先发现可用渲染器及Python依赖；不同解释器依赖可能不同，应分别探测所需模块，不能因生成文档用的解释器不带COM/PDF模块就断言机器不能渲染。

当Windows安装Word且有pywin32时，以下方法已实际完成真实Word导出：

```python
import win32com.client
word = win32com.client.DispatchEx('Word.Application')
word.Visible = False
word.DisplayAlerts = 0
doc = None
try:
    doc = word.Documents.Open(str(docx_path), ReadOnly=True,
                              AddToRecentFiles=False)
    doc.ExportAsFixedFormat(str(pdf_path), 17)  # wdExportFormatPDF
finally:
    if doc is not None:
        doc.Close(False)
    word.Quit()
```

必须使用绝对路径，保持只读、不加入最近文件、结束时关闭自己创建的Word实例。不要杀掉用户现有Word进程。使用有界超时；导出失败时如实说明，不能把自行绘制的图片冒充实际Word预览。

用PyMuPDF读取实际PDF并生成预览：

```python
import pymupdf
with pymupdf.open(pdf_path) as pdf:
    print('pages:', len(pdf))
    pdf[0].get_pixmap(matrix=pymupdf.Matrix(1.5, 1.5),
                      alpha=False).save(preview_path)
```

原PDF页面坐标中可选择目标区域生成局部预览，但先检查整页并确保截图包含完整施工内容。裁剪坐标依文档实际布局决定，不硬编码为所有日志通用。

## 批量处理全部历史日志

- 先递归清点 `施工日志_YYYYMMDD.docx`，按日期去重，优先月份主目录版本，排除草稿、备份、预览变体；不要按最近月份猜总数，也不补造缺失日期。
- 历史模板可能为6行（内容Row4/安全Row5）或5行（内容标题和正文合在Row3/安全Row4）；按标题识别目标，5行内容栏保留固定标题字体。
- 安全栏只改变完整标题之后、`项目技术负责人`或`施工记录：`之前的正文，兼容单段落软换行、多段落、标题与正文挤在同一行。混合run应在边界拆分，保留rPr除rFonts外的所有设置，不能重设cell.text导致原版格式丢失。
- 字号、粗细、段落、行高、所有文字及签名均保留。对所有原件先后SHA256比对；输出逐字/非字体格式比对。为减少无关变化，可只替换DOCX ZIP内word/document.xml，其余包成员逐字节保留。
- XML验证时 `doc._element.body.sectPr` 才是节属性；旧行可能没有trPr，比较前必须处理None。
- 只有字体改变也可能增加打印页数：实测早期一份原件1页，行楷副本变2页，另有5行模板及近期模板页数不变。不要承诺分页不变，未经用户要求不要悄悄缩字号或行距来压页。
- 批量ZIP检查唯一成员、文档总数、CRC，并逐字节/哈希对照生成副本；包内可附简短字体范围说明。最终说清覆盖日期、份数、原件未改及字体可能引起分页变化。

## 4. 前后分页比较与交付

如果输出为两页或发现天气栏文字被裁切：
1. 将原文件也用同一Word引擎导出到工作区临时PDF。
2. 对比原件和字体变体的页数及各页内容；区分源文件原有问题和新字体造成的问题。
3. 不因结构、字体验证通过就宣称“一页打印正常”。
4. 未获授权不改其他字段来强行压成一页；简短说明原件已有分页问题，字体修改是否改变了分页。

交付优先短回复：说明字体、修改范围、原件保留；附Markdown局部预览和Word下载。Windows链接使用正斜杠绝对路径并将目标用尖括号包住。不能将截图或PDF只是存在说成已经视觉检查，应实际加载预览检查可读性。
