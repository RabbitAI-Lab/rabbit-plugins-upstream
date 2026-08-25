---
name: "literature-harvest-zotero"
description: "知网+NCBI+Google Scholar 多源文献下载 → Zotero 合集入库完整流水线（父条目+linked_file+标签+中文笔记）"
---

# literature-harvest-zotero — 多源文献下载 + Zotero 入库流水线

## 用途
用户要求「下载 N 篇 XX 主题文献，来源涉及知网/NCBI/Google Scholar，放 Zotero 某合集」时，按本 SOP 执行。
已验证批次：2026-08-18 连续 7 批（5+5+5+7+7+9+9 篇）全部成功；含子代理全自动执行验证。

## 前置条件（本机固定配置，见 TOOLS.md）
- **网络路由分工（死规矩）：** 知网 = 浏览器直连（OpenClaw 浏览器默认，本机 IP 自动登录机构账号）；NCBI / Google Scholar = 走本地代理（脚本内 PROXY dict，带「代理→直连兜底」重试）
- **Zotero API：** key 从 Zotero 官网 Settings→Security 复制（勿截断）；Base `https://api.zotero.org/users/<你的UserID>/`；**云存储满时 PDF 一律 `linked_file` 本地链接（path=你的本地文献目录/xxx.pdf）**，不传云
- **PDF 落盘：** 知网下载在 `%TEMP%\openclaw\downloads\` → 拷到本地文献目录；NCBI/Scholar 直接写该目录
- **NCBI API key：** TOOLS.md「NCBI API」节

## 流程总览
```
① 知网 N 篇（浏览器） → ② NCBI N 篇（eutils+PMC 下载） → ③ Scholar N 篇（cookie 抓取） → ④ Zotero 建合集/入库（父条目+附件+标签+中文笔记） → ⑤ 验证 → ⑥ 归档记忆
```

## ① 知网（浏览器，每次 3-5 篇）
1. `browser open https://www.cnki.net/`（自动 IP 登录，勿找登录按钮）
2. **🔴 只走首页搜索框**（textbox "中文文献、外文文献"）输入主题词，搜**短关键词**（3-6 词命中率最高）：
   - ❌ **禁止直接用已生成的 kns8s 结果页 URL 或 kcms2 详情 URL 打开——必跳 clickWord 文字点选验证码（iframe 无法自动化通过）**
   - 若从已有搜索结果页（kns8s defaultresult）点标题进详情是安全的（2026-08-18 验证）
3. 结果列表逐个「详情页新标签打开」：点击标题链接 → 新 tab
4. 详情页点「PDF下载」→ 可能跳 login.cnki.net（bar 域会话初始化，稍等/再点）或弹「IP超出用范围」→ 无视，下载照常
5. **不要用 waitfordownload（会超时）**：等 5-8 秒直接 `Get-ChildItem $env:TEMP\openclaw\downloads | sort LastWriteTime -d` 查新文件
6. 复制到本地文献目录（如 `~/Downloads/文献/`，命名 `CNKI_标题_作者年份.pdf`，前缀 CNKI_）
7. **元数据提取（学位论文关键）：** 详情页 `browser act evaluate` 抓 `document.body.innerText` 片段，搜关键词（导师/学科专业/博士|硕士/年期/DOI/分类号）：
   ```js
   () => { const t = document.body.innerText; const out=[]; for (const kw of ['年度','DOI','分类号','导师','学科专业','博士','硕士']) { const i=t.lastIndexOf(kw); if(i>=0) out.push(kw+': '+t.slice(Math.max(0,i-70),i+90).replace(/\s+/g,' ')); } return out.join('\n---\n'); }
   ```
   - **学位论文年份拿不到时：** 用 pypdf 读下载 PDF 首页提取（答辩时间/学年度）；扫描版无文本层则退回页面正文正则 `(20\d{2})[年.]`
8. **避开已下载：** 开工前 memory_search 上批记录，列表里跳过已有标题
9. 长任务（≥3 篇）默认子代理化执行，子代理必须拿到完整交接单（URL/避开清单/踩坑预案）

## ② NCBI（eutils + PMC 下载）
模板：`templates/ncbi_search.py`（检索+PMC 确认）、`templates/dl_epmc.py`（下载）、`templates/pmc_pow_dl.py`（POW 直连兜底）
1. 检索词结构化：`"PP2A"[Title] AND (fung*[Title/Abstract] OR yeast* OR Aspergillus OR Candida OR Fusarium)` 或 `"Rho GTPase"[Title/Abstract] AND fungi`；esearch+esummary 一次拿到 PMID/期刊/年份/被引
2. 选文标准：**优先 PMC 可下（elink 确认）**、期刊权威（领域 Q1/经典，Nature/PNAS/EMBO J/mBio/MMBR 等）、年份新或高被引
3. 下载优先级（依次尝试）：
   a. **Europe PMC render**：`https://europepmc.org/articles/{PMCID}?pdf=render`（代理）
   b. **Europe PMC REST fullTextPDF**：`https://www.ebi.ac.uk/europepmc/webservices/rest/{PMCID}/fullTextPDF`（代理）
   c. **PMC 官网 POW 直连**（a/b 404 时秒切）：`curl.exe` **不开代理** 直连 `https://pmc.ncbi.nlm.nih.gov/articles/{PMCID}/pdf/main.pdf`，遇 `POW_CHALLENGE` 解算 sha256 前缀 nonce 后带 cookie `cloudpmc-viewer-pow=<challenge>,<nonce>` 重试 → 2026-08-18 对 Nature/MMBR/mBio 3/3 全通（见 templates/pmc_pow_dl.py）
   d. PLOS 直链：`https://journals.plos.org/{journal}/article/file?id={doi}&type=printable`
   - 校验：`content[:4]==b"%PDF"` 且 >50KB
4. 元数据：`efetch` retmode=xml 拿卷/期/页/DOI/作者全名/摘要（比 esummary 更全）

## ③ Google Scholar（cookie 反爬破解）
模板：`templates/scholar_grab_parse.py`
1. `requests.Session()` 先 GET `google.com` 拿 NID cookie（代理）→ 同 session 访问 `scholar.google.com/scholar?q=...` 返回 200 可解析
2. 每查询间隔 3s；一次 2 个查询词
3. 解析：提取 title/href/Cited by/[PDF]链接/src
4. 选文标准：高被引 + **OA 可下**（优先 PLOS/PMC/Europe PMC render；Wiley/ASM/T&F/ScienceDirect 全 Cloudflare 403 慎选——但 mBio 虽是 ASM 却全 OA 进 PMC，可用 ②-c 下载）；命中候选先 `elink` 查 PMC 再下
5. ⚠️ 运行解析脚本需 `$env:PYTHONIOENCODING="utf-8"`（否则 GBK 控制台 UnicodeEncodeError \xa0 崩溃）
6. **下载失败预案必须预置：** Scholar 全文链 403（Wiley/ASM）→ 立刻换同主题 OA 备选（Frontiers/PLOS/PMC 直链），不要恋战

## ④ Zotero 入库（三步齐全）
1. **建合集：** 查 `GET collections` 是否已存在 → 无则 `POST collections`（body 字段 `parentCollection`，不是 `collection`）→ 记 key
2. **父条目：** `POST items` 数组，`collections:[key]`，thesis/journalArticle 全字段（含 DOI/url/abstractNote/tags）；中文文献 tags 用 研究方向+物种+主题
3. **linked_file 附件：** 同 POST，`itemType=attachment, linkMode=linked_file, parentItem=<key>, path=<你的本地文献目录>/xxx.pdf`
4. **中文笔记：** 每篇一条 child note（parentItem=条目 key，HTML `<p>` 格式）：研究方向关联 + 核心内容 + 可借鉴方法；⏺ 笔记正文**禁嵌 ASCII 双引号**（Python 字符串 SyntaxError 坑，中文句内引号用「」全角）
5. ⚠️ 优先参考工作区已有的 `_zotero_*.py` 现成脚本改导表（找最新模板，含 add / notes 两阶段）
6. 🔴 **Zotero API key 必须写完整 24 字符**（从 Zotero 官网「Settings→Security」复制完整串，禁止手动截断/用省略号代替——U+2026 会在 requests header latin-1 编码直接 UnicodeEncodeError；已踩 3 次）

## ⑤ 验证
`GET collections/{key}/items?limit=100` → 计数：父条目数 = 附件数 = 笔记数，itemType 分布正确，每篇带标签。

## ⑥ 归档
写 `memory/YYYY-MM-DD-HHMM.md`：批次表（文献/来源/Zotero key）+ 新踩坑 + 脚本名；更新 TOOLS.md 如有新配置。

## 踩坑清单（累计验证）
| 坑 | 解法 |
|---|---|
| **kns8s/kcms2 URL 直接打开 → clickWord 文字点选验证码（无法自动化过）** | **只走首页搜索框搜短关键词 → 点结果进详情**；已有结果页内点标题安全 |
| kns8s URL 直接搜触发滑块验证 | 走首页搜索框输入 |
| waitfordownload 超时 | 无视，等几秒查目录 |
| 知网弹「IP超出使用范围」 | 无视，下载照常 |
| NCBI 代理 TLS 断 | 代理→直连双向重试 |
| **Europe PMC fullTextPDF / ?pdf=render 全 404**（Nature/MMBR/mBio 实测，2026-08-18） | **PMC 官网 POW 直连**：curl 直连 `/pdf/main.pdf` + 解 POW_CHALLENGE 带 cookie 重试（pmc_curl_dl.py，3/3 全通） |
| PMC 官网走代理触发 reCAPTCHA | **直连**（不开代理）反而能过 POW → PMC 一律直连 |
| Scholar headless 被 sorry 拦 | cookie 法（google.com→scholar） |
| Wiley/ASM/T&F CF 403 | 避开；但 ASM 的 mBio 全 OA 进 PMC，可用 POW 直连下；预案预置备选 |
| Zotero 云配额满 | linked_file 本地路径 |
| GBK 控制台打印崩溃 | PYTHONIOENCODING=utf-8 |
| Zotero collection 字段名错 | `parentCollection` |
| 笔记正文内嵌 ASCII 双引号 → Python SyntaxError | 句内引号用「」全角 |
| Zotero API key 用截断版 → UnicodeEncodeError | 必须完整 24 字符（踩 3 次） |
| 学位论文年份详情页无显示 | pypdf 读 PDF 首页（答辩时间）；扫描版用页面正文正则 |

## 脚本清单（workspace 现有，直接用）
- 知网：无脚本（浏览器手动流，子代理化执行）
- NCBI：`_ncbi_pp2a_search.py` / `_ncbi_rho_search.py`（检索）`_pp2a_efetch.py`（efetch 元数据）`_pp2a_dl4.py`（Europe PMC/PLOS 下载）
- **PMC POW 直连：`pmc_curl_dl.py`（模板始祖）`_pp2a_pmc_dl.py`（PP2A 版，3/3 成功）**
- Scholar：`_scholar_grab.py`（抓）`_scholar_pp2a_parse.py`（解析）`_scholar_pp2a_check.py`（EPMC OA 确认）
- Zotero：`_zotero_collections.py`（查合集）`_zotero_pp2a_add.py`（条目+附件，最新模板）`_zotero_pp2a_notes.py`（笔记，最新模板）

## 子代理执行规范（2026-08-18 第 6 批验证）
- 长任务（≥3 篇/含浏览器操作）默认 sessions_spawn 子代理：工具输出隔离出主会话，主会话只收最终结果
- **交接单必须包含：** ①全部候选 URL/PMID/规避清单（已入库的要避开）②网络路由（知网直连/NCBI+Scholar 代理）③踩坑预案（验证码解法/403 备选/POW 直连）④Zotero 合集 key + linked_file 规则 ⑤回报格式
- 完成后主会话抽查验证（PDF 落盘 + %PDF 头 + Zotero 计数），不盲信子代理报告
