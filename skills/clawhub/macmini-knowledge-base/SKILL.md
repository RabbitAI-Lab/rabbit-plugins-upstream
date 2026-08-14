---
name: macmini-knowledge-base
version: 1.4.0
description: |
  在 Mac Mini (M4) 上快速搭建本地知识库 + RAG 自然语言搜索系统。
  适用场景：
  - 新 Mac 配置知识库：从零开始安装配置 Ollama、embedding模型、定时任务、文档解析
  - 遇到 PDF 提取乱码、定时任务超时、skill 加载失败等问题
  - 想要建立每日自动分析文档 + 08:00发送摘要到飞书的流程
  - 迁移或复现知识库：打包整个 knowledge 目录和配置到新电脑
  - **v1.4 新增**：CMap 残缺度自检（不预设来源）+ 50万字完整提取 + OCR fallback 到 .doc
  本 skill 会引导完成：目录结构创建、依赖安装、脚本部署、定时任务注册、OpenClaw 配置。
---

# Knowledge Base Setup

在 Mac Mini 上快速搭建本地知识库 + RAG 搜索系统。

## 核心功能（v2.0）

- **kreuzberg 统一提取层**：PDF / DOCX / XLSX / PPTX / MD / 图片 OCR 全自动路由
- **antiword 极速专线**：.doc 文件专用提取，成功率 85%，169MB 文件 0.02 秒完成
- **智能兜底**：antiword 失败自动走 soffice 转换，60 秒硬超时无误判
- **自动分类**：关键词匹配驱动，中英文双语标签
- **定时任务**：每天 23:00 分析新文档，08:00 发送摘要到飞书

## 快速开始

### 一键安装

```bash
cd ~/.openclaw/workspace/skills/knowledge-base-setup/scripts
bash setup.sh <飞书用户ID>
```

### 手动分步安装

**Step 1: 系统依赖**
```bash
brew install antiword tesseract pandoc
```

**Step 2: Python 依赖**
```bash
pip3 install kreuzberg pytesseract pymupdf docx openpyxl python-pptx
```

**Step 3: Ollama + embedding 模型**
```bash
# 安装 Ollama: https://ollama.com/download
ollama pull nomic-embed-text
```

**Step 4: 创建目录结构**
```bash
mkdir -p ~/.openclaw/workspace/knowledge/.analysis/summaries/archives
mkdir -p ~/.openclaw/workspace/knowledge/temp_docs
touch ~/.openclaw/workspace/knowledge/文章目录/文章目录.md
```

**Step 5: 部署脚本**
```bash
cp ~/.openclaw/workspace/skills/knowledge-base-setup/scripts/*.py \
   ~/.openclaw/workspace/knowledge/.analysis/
chmod +x ~/.openclaw/workspace/knowledge/.analysis/*.py
```

**Step 6: 配置 OpenClaw**

编辑 `~/.openclaw/openclaw.json`，加入：
```json
{
  "models": {
    "providers": {
      "ollama": {
        "baseUrl": "http://127.0.0.1:11434",
        "api": "ollama",
        "models": [
          {"id": "nomic-embed-text", "name": "Nomic Embed Text"}
        ]
      }
    }
  },
  "agents": {
    "defaults": {
      "memorySearch": {
        "provider": "ollama",
        "model": "nomic-embed-text"
      }
    }
  }
}
```

确保 tools 区块有：
```json
"tools": {
    "alsoAllow": ["exec", "process"]
}
```

然后重启：`openclaw gateway restart`

**Step 7: 注册定时任务**
```bash
# 23:00 分析新文档
openclaw cron add \
  --name "23:00分析新文档" \
  --cron "0 23 * * *" \
  --tz "Asia/Shanghai" \
  --session isolated \
  --timeout-seconds 600 \
  --message "cd ~/.openclaw/workspace/knowledge/.analysis && python3 run_analysis.py && python3 generate_catalog.py" \
  --announce --channel feishu --to "user:<飞书用户ID>"

# 08:00 发送文档摘要
openclaw cron add \
  --name "08:00发送文档摘要" \
  --cron "0 8 * * *" \
  --tz "Asia/Shanghai" \
  --session isolated \
  --timeout-seconds 120 \
  --message "读取 summaries/ 目录发送摘要到飞书" \
  --announce --channel feishu --to "user:<飞书用户ID>"
```





## summary 文件名 sanitize（v1.4.1 新增）

防止 `OSError: [Errno 63] File name too long`（NAME_MAX=255 bytes）：

```python
SUMMARY_NAME_MAX = 200

def sanitize_filename(name, max_length=SUMMARY_NAME_MAX):
    """截断超长文件名，保留扩展名 + 8 位 MD5 hash 防冲突"""
    name_bytes = name.encode('utf-8')
    if len(name_bytes) <= max_length:
        return name
    
    base, ext = os.path.splitext(name)
    ext_bytes = ext.encode('utf-8')
    base_bytes = base.encode('utf-8')
    
    import hashlib
    h = hashlib.md5(name_bytes).hexdigest()[:8]
    
    reserve = len(ext_bytes) + 1 + 8  # "_" + hash + ext
    available = max_length - reserve
    
    if available > 0 and len(base_bytes) > available:
        truncated = base_bytes[:available].decode('utf-8', errors='ignore')
        return f"{truncated}_{h}{ext}"
    
    return name[:max_length]
```

主循环的异常捕获重试：

```python
try:
    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write(content)
except OSError as e:
    if e.errno == 63:  # ENAMETOOLONG
        short_name = sanitize_filename(filename, max_length=180)
        summary_file = os.path.join(
            SUMMARY_DIR,
            f"{timestamp}_{short_name}.summary.txt"
        )
        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write(content)
```

**触发场景：** 畸形 PDF 文件名（如下载错误的 `_; filename_=utf-8''...` 双名拼接），原文件名 244+ bytes + 时间戳超 255 bytes 限制。

**实测案例：** `20260730-Nomura-Asia Insights：China：The Politburo meeting indicated a shift to _countercyclical" policies-260730.pdf_; filename_=utf-8''...pdf` (原 248 bytes) → sanitize 后 200 bytes + 8位 hash → 安全创建。

### temp_docs 畸形文件清理（v1.4.1 新增）

下载失败的 PDF 在文件名里重复了两次（`_; filename_=utf-8''` 分隔），实际只需保留前半。一次性清理脚本：

```python
import os, shutil
temp_docs = os.path.expanduser("~/.openclaw/workspace/knowledge/temp_docs")
trash_dir = os.path.expanduser("~/.openclaw/workspace/knowledge/.trash/temp_docs_<时间戳>")
os.makedirs(trash_dir, exist_ok=True)

for f in os.listdir(temp_docs):
    if "_; filename_=utf-8''" in f:
        full = os.path.join(temp_docs, f)
        parts = f.split("_; filename_=utf-8''")
        real_name = parts[0]
        target = os.path.join(temp_docs, real_name)
        if not os.path.exists(target):
            shutil.move(full, target)
            print(f"重命名: {real_name}")
```



## CMap 残缺度自检（v1.4 新增）

不预设"哪个 PDF 来源会乱码"——实测 **72% 的乱码来自非 lightpdf PDF**（PPT 转 PDF、扫描件等），
改用**自适应检测**：

```python
def is_cmap_broken(text, threshold=0.03):
    """检测文本是否含异常字符（CMap 残缺/PUA 污染/未映射 CID）"""
    if not text or len(text.strip()) < 50:
        return False
    total = len(text)
    pua_count = sum(1 for c in text if 0xE000 <= ord(c) <= 0xF8FF)
    cjk_ext = sum(1 for c in text if 0x20000 <= ord(c) <= 0x2EBEF)
    cjk_compat = sum(1 for c in text if 0xF900 <= ord(c) <= 0xFAFF)
    cid_count = text.count('(cid:')
    bad_ratio = (pua_count + cjk_ext + cjk_compat + cid_count) / total
    return bad_ratio > threshold or cid_count > 10
```

**3 类乱码特征：**
1. **PUA 私用区** (U+E000-F8FF) —— 残缺 CMap fallback
2. **CJK 扩展区** (U+20000-2EBEF) —— 字符找不到映射
3. **`(cid:xxxx)` 字面值** —— pdfplumber 提取失败标志

**集成位置：** `extract_pdf_text()` 在 kreuzberg / pymupdf 提取后调 `is_cmap_broken()`，
通过即返回，失败即触发 OCR 路径。

### OCR 性能实测（2026-08-12 验证）

| 文件 | 大小 | OCR 耗时 | 备注 |
|---|---|---|---|
| lightpdf PDF | 4 页 | 13.5 秒 | CMap 残缺，自动 OCR |
| 大型 PPT 转 PDF      | 90 页 | 0.5 秒 | 默认路径（无需 OCR）|
| 65MB .doc | 169MB 文件 | 0.1 秒 | antiword 极速专线 |
| 大型 docx（475K 字）| 562KB | 11.2 秒 | python-docx fallback |
| OCR 自检总开销 | - | < 200ms | 3 页抽样 + 字符统计 |

### 批量 OCR 修复脚本（v1.4 新增）

`re_ocr_corrupted.py` —— 批量扫描乱码 summary，自动用新版本 utils 重新提取：

```bash
# 干跑（不写文件）
python3 re_ocr_corrupted.py --dry-run --max 10

# 实际批量（处理所有乱码）
python3 re_ocr_corrupted.py --max 100

# 只处理指定 PDF
python3 re_ocr_corrupted.py --pdf-list "path1.pdf,path2.pdf"
```

行为：
1. 扫 archives/ 找出乱码 summary
2. 按 basename 匹配源 PDF
3. 调 `extract_pdf_text()` 重跑（自动 OCR fallback）
4. 写新 summary 到 summaries/（带新时间戳）
5. 覆盖 archives/ 里对应 basename 的所有乱码版本
6. 输出 JSON 报告（含每份文件路径/字数/成功状态）

## 文档解析架构（v2.0）

### 架构图

```
                    ┌──────────────────────────────────────┐
                    │         kreuzberg 统一提取层           │
                    │  (pypdfium2 / python-calamine / pandoc) │
                    └───┬────────────────────────────────┬───┘
                        │                              │
                自动判断 │                              │
                        ▼                              ▼
              ┌─────────────────┐           ┌─────────────────────┐
              │  kreuzberg 直提  │           │  antiword 极速专线  │
              │ PDF/DOCX/XLSX/  │           │   (.doc 文件专用)    │
              │ PPTX/MD/图片OCR │           │   成功率 85%，<1秒   │
              └─────────────────┘           └─────────────────────┘
                        │                              │
                        │         ┌──────────────────────────────┐
                        │         │     soffice 兜底转换          │
                        │         │ (.doc/.xls/.ppt antiword失败) │
                        │         │  60秒硬超时（消除误判watchdog）│
                        │         └──────────────────────────────┘
                        ▼                              │
              ┌──────────────────────────────────────────────┐
              │              文本输出（content）              │
              │  → summaries/ 摘要文件 → generate_catalog.py  │
              └──────────────────────────────────────────────┘
```

### 文件类型 × 提取方式

| 格式 | 主方案 | 依赖 | 成功率 | 单文件速度 |
|------|--------|------|--------|-----------|
| PDF | kreuzberg (pypdfium2) | 无 | ~100% | 0.05-0.7s |
| DOCX | kreuzberg + pandoc | pandoc 3.9+ | 100% | 0.12-3s |
| XLSX | kreuzberg (python-calamine) | 无 | 100% | 0.1-0.5s |
| PPTX | kreuzberg + pandoc | pandoc 3.9+ | 100% | 0.02-0.2s |
| MD | kreuzberg + pandoc | pandoc 3.9+ | 100% | <0.01s |
| **.doc** | **antiword 优先** | antiword | **85%**，<1秒 | <0.02s |
| .doc（失败） | soffice 兜底 | LibreOffice | ~15% | 2-21s |
| .xls | soffice → XLSX | LibreOffice | ~95% | 2-10s |
| .ppt | soffice → PPTX | LibreOffice | ~95% | 2-10s |
| 图片 | kreuzberg 内置 OCR | tesseract | ~90% | 3-10s |

### antiword 极速专线

```python
# 实测数据：
# 169MB 超大文件 → 26万字符，0.02秒完成
# 正常 .doc（0.1-15MB）→ <1秒
# 成功率 85%，覆盖绝大多数 .doc 文件
result = subprocess.run(['antiword', filepath], capture_output=True, timeout=10)
```

### kreuzberg 统一提取层

kreuzberg 是专业的非结构化文档文本提取库（支持 20+ 格式），内部自动路由：
- PDF → pypdfium2
- XLSX → python-calamine
- DOCX/PPTX/MD → pandoc
- 图片 → 内置 OCR（tesseract）

## 关键词库（中英双语）

**中文（47个）：** 房产、房价、房地产、居民、消费、股市、经济、政策、利率、通胀、人民币、A股、美联储、PBOC、GDP、股票、资产、投资、债券、银行、PPI、CPI、PMI、M2、就业、失业、汽车、新能源、AI 等

**英文（70+个）：** property、real estate、GDP、inflation、CPI、PPI、PMI、PBOC、Fed、consumer、economy、growth、housing、stock market、EV、AI 等

**标签输出语言：** 自动判断——英文内容匹配英文关键词输出英文标签，中文内容匹配中文关键词输出中文标签

## 定时任务兼容性

| 任务 | ID | 调用方式 | 结论 |
|------|------|---------|------|
| 23:00分析新文档 | f3536e18 | 绝对路径 `python3 run_analysis.py` | ✅ 无需修改 |
| 07:00生成财经早报 | b741c6d5 | Node.js 脚本 | ❌ 不相关 |
| 08:00发送财经早报 | a7cbaacc | 读取文件发送 | ❌ 不相关 |
| 09:00发送文档摘要 | 89b4cf75 | 读取 summaries 目录 | ❌ 不相关 |

## 迁移到新电脑

1. 复制整个目录：
   ```bash
   scp -r ~/.openclaw/workspace/knowledge user@new-mac:~/.openclaw/workspace/
   ```
2. 在新电脑运行 `bash setup.sh <飞书用户ID>`
3. 重新注册定时任务（Job ID 会变）

## 避坑指南

| 问题 | 原因 | 解决 |
|------|------|------|
| LibreOffice 超时 | watchdog 误判大文件为卡死 | v2.0 移除 watchdog，60秒硬超时 |
| .doc 提取慢 | 统一走 LibreOffice | antiword 专线，169MB 文件 0.02秒 |
| DOCX/PPTX 处理失败 | pandoc 未安装 | `brew install pandoc` |
| PDF 提取乱码（OCR 不工作） | ocrmypdf `--skip-text` 跳过乱码页 | v1.4 改为 `--force-ocr` 强制 OCR |
| PDF 漏检 CMap 残缺 | 没主动判断是否乱码 | v1.4 `is_cmap_broken()` 自检（阈值 0.03）|
| 文本被截断到 8000 字 | 硬编码 `[:8000]` 太短 | v1.4 `MAX_EXTRACT_LEN = 500_000` |
| .doc 提取失败 | lightpdf 处理过的 .doc 乱码 | v1.4 `ocr_office_via_ocr()` 兜底 |
| summary 文件名过长失败 | 畸形 PDF 名 244+ bytes + 时间戳超 NAME_MAX | v1.4.1 `sanitize_filename()` + Errno 63 重试 |
| 静默失败（不知道哪个文件）| 不抛异常 | v1.4 `PDFExtractError` / `ExtractError` 含路径 |
| 飞书无 exec 工具 | tools 策略限制 | 添加 `alsoAllow: [exec, process]` |
| BGE-M3 卡顿 | 16GB 内存不足 | 继续用 nomic-embed-text |

## 关键路径

| 内容 | 路径 |
|------|------|
| Skill 目录 | `~/.openclaw/workspace/skills/knowledge-base-setup/` |
| 知识库 | `~/.openclaw/workspace/knowledge/` |
| 分析脚本 | `~/.openclaw/workspace/knowledge/.analysis/` |
| 目录缓存 | `~/.openclaw/workspace/knowledge/.analysis/.catalog_cache.json` |
| 摘要输出 | `~/.openclaw/workspace/knowledge/.analysis/summaries/` |
| 文章目录 | `~/.openclaw/workspace/knowledge/文章目录/文章目录.md` |
| OpenClaw 配置 | `~/.openclaw/openclaw.json` |

## 版本历史

| 版本 | 日期 | 更新内容 |
|------|------|---------|
| 1.0.0 | 2026-05-10 | 初始版本，PyMuPDF + LibreOffice 链路 |
| 1.1.0 | 2026-05-13 | 三步 PDF 处理，关键词库，双语标签 |
| 1.2.0 | 2026-05-21 | 分批处理优化，280秒断点 |
| 1.2.1 | 2026-05-22 | utils.py 共享模块重构，LibreOffice 熔断机制 |
| 1.3.0 | 2026-05-28 | kreuzberg 统一提取层 + antiword 专线 + pandoc |
| 1.4.0 | 2026-08-12 | CMap 残缺度自检 + 50万字完整提取 + OCR fallback 到 .doc |
| **1.4.1** | **2026-08-12** | **run_analysis.py: sanitize_filename + Errno 63 重试 + 清理 temp_docs 畸形文件** |
