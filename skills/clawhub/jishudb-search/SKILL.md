---
name: jishudb-search
description: >-
  Search existing JishuDB documents, list files, read text, and check import status; answer with source citations. No public-web research. / 查询JishuDB已有资料、文件清单、文档正文和导入进度，依据真实结果标注来源，不用于公网研究。
compatibility: >-
  Requires an authorized JishuDB connection. Document inventory, text, metadata,
  and job status need the corresponding host MCP tools. The bundled HTTP helper
  only lists knowledge bases and searches passages; it requires Bash, curl, and
  a reachable JISHUDB_URL, with JISHUDB_TOKEN when authentication is enabled.
metadata:
  author: jishushell-team
  version: "0.1.1"
  openclaw:
    homepage: https://github.com/x-aijishu/jishudb-skills/tree/main/skills/jishudb-search
# JishuDB Knowledge Search / JishuDB知识库检索助手
tags: [knowledge, rag, search, kb, retrieval]
slash_command: /kb
---

Retrieve facts from existing JishuDB documents and answer with source citations.
Use the actual inventory, document, search, or job tools for each request.

先检索JishuDB已有资料，再依据真实结果回答并标注来源；清单、正文和任务进度使用对应工具。

## At a glance

| Item | Details |
| --- | --- |
| Use when | Questions concern documents, file inventory, or import status already in JishuDB. |
| Delivers | Answers with source filenames, verified inventories, document text, or observed job status. |
| Requires | An authorized JishuDB connection; the HTTP helper needs Bash and curl and only lists KBs or searches. |
| Does not | Import new material, research the public web, or infer file counts from search passages. |

## Use this skill when

- The user asks a factual question about material already stored in JishuDB.
- The user wants an exact knowledge-base or document inventory.
- The user asks to read a particular document or inspect its current metadata.
- The user asks whether an import has finished or uses `/kb` as a search request.

## Do not use this skill when

Do not use this skill to import new material or research the public web.
Use `jishudb` for setup or connection repair, `research-report-hunter` to discover
external reports, and `jishudb-plaud-import` to archive selected Plaud material.
The `/kb` field is a legacy hint, not a portable command registration; use the
host's supported Skill loader if no such command exists.

## Agent workflow

### Route the request to the matching tool

- Knowledge-base names, IDs, or counts: call `kb_list` and use this run's results.
- Exact file names or counts: call `kb_list_documents` and follow every `nextCursor`.
  List only returned documents; search passages and job records are not file inventories.
- Current document metadata: identify the file with `kb_list_documents`, then call `kb_get_document`.
- Full document content: call `kb_read_document_text`; snippets do not reconstruct a full document.
- Semantic facts: call `kb_search`, synthesize returned passages, and cite sources.
- Import progress: call `kb_list_jobs` or `kb_get_job`. Jobs are processing attempts,
  so one document may have several jobs; do not equate job count with file count.
- If the needed tool fails or is unavailable, state what could not be verified.

The packaged `kb-search.sh` helper uses curl for the KB HTTP API. Set `JISHUDB_URL`
for the actual backend; JishuShell panel bindings inject it automatically. The
helper's default is `http://host.docker.internal:18089`. Set `JISHUDB_TOKEN`
through the approved environment when authentication is enabled.

### List knowledge bases when the target is unknown

These examples use repository-root paths. For a separately installed package,
resolve `kb-search.sh` relative to the loaded Skill directory.

```bash
bash skills/jishudb-search/kb-search.sh list
```

Use a relevant returned ID; the output includes names and chunk counts.

### Search

```bash
bash skills/jishudb-search/kb-search.sh search "question or keywords" <kb-id>
```

An optional third argument sets `topK` (default 6). When a panel binding supplies
`JISHUDB_DEFAULT_KB`, the KB ID may be omitted:

```bash
bash skills/jishudb-search/kb-search.sh "question or keywords"
```

### Answer from retrieved evidence

Synthesize the returned passages and cite their actual source filenames. If the
helper returns `No matching passages found`, report no matches for this search;
try other keywords or a relevant KB from `list` without inventing evidence.
Treat low-relevance passages cautiously and disclose uncertainty.

### Errors and completion

The helper is read-only and can be called for several relevant queries. Keep a
missing curl dependency distinct from a backend connectivity failure; verify
the backend's actual running state and configured address. Complete the answer
only to the extent supported by observed tool output.

### Chinese reference / 中文操作参考

#### 请求必须路由到对应工具

- 问“有哪些知识库”、知识库名称、标识或数量：调用 `kb_list`，只按本轮工具结果回答。
- 问某个知识库“有哪些文件”、精确文件名或文件数量：调用 `kb_list_documents`；若返回 `nextCursor`，继续翻页直到结束。只列返回的 `documents`，不得从检索片段、正文、历史对话或任务记录补出文件名。
- 问某个文件的当前状态或元数据：先用 `kb_list_documents` 确认文件，再调用 `kb_get_document`。
- 问某个文件具体写了什么：调用 `kb_read_document_text`；不要仅凭搜索摘要还原全文。
- 问资料中的语义事实：调用 `kb_search`，只依据返回片段综合，并标注来源。搜索结果不是完整文件清单。
- 问导入进度：调用 `kb_list_jobs` 或 `kb_get_job`。任务是处理尝试，同一文件可能对应多条任务，任务数不能当作文件数。
- 对应工具失败或不可用时，如实说明无法核实，不要根据记忆或字段名称猜测。

本技能目录里有一个零依赖脚本 `kb-search.sh`（用 curl 调 KB 的 HTTP API）。KB 地址由环境变量 `JISHUDB_URL` 配置（JishuShell 面板绑定时会自动注入；独立使用时自行 export，默认 `http://host.docker.internal:18089`）；若 KB 开了鉴权，另设 `JISHUDB_TOKEN`。

#### 1. 不确定有哪些知识库时，先列出

```bash
bash skills/jishudb-search/kb-search.sh list
```

输出每个库的 `id` / 名称 / 块数。挑一个相关的 `id` 用于检索。

#### 2. 检索

```bash
bash skills/jishudb-search/kb-search.sh search "用户的问题或关键词" <kb-id>
```

- 第 3 个参数可选 `topK`（默认 6）。
- 若面板绑定时设了默认库（`JISHUDB_DEFAULT_KB`），可省略 `<kb-id>`，直接：
  ```bash
  bash skills/jishudb-search/kb-search.sh "用户的问题"
  ```

返回形如:

```
Top 6 passages (cite the source filename in your answer):

[1] 01-quick-start.md  (relevance: high)
    JishuShell 是面向 Arm 边缘设备的 AI Agent 管理面板 …

[2] README.md  (relevance: medium)
    …
```

#### 3. 据检索结果作答

- **综合**这些片段写出答案，用自己的话组织。
- **标注来源**：在答案里点名引用的文件名（如「据 `01-quick-start.md`…」），或在末尾列出来源。
- 若返回 `No matching passages found`，**如实告知**知识库里没有相关内容，不要编造；可建议换关键词或换一个库（先 `list`）。
- 相关度 `low` 的片段要谨慎使用，必要时说明置信度不高。

#### 备注

- 脚本只读、无副作用，可安全多次调用（同一轮可对不同关键词检索几次再综合）。
- 若 `kb-search: curl not found` / 无法连接：说明运行环境缺 curl 或网络不通 KB，提示用户检查 KB 应用是否在面板里处于运行状态。

## Resources

- [`kb-search.sh`](kb-search.sh): Use the read-only HTTP helper for knowledge-base listing or passage search when its documented environment is available; other operations require host MCP tools.

## Discovery

### Keywords

- English: JishuDB search, /kb, passage retrieval, document inventory, ingest job status.
- Chinese: 查知识库、内部资料、文件清单、文档正文、导入进度.

### Example requests

- “Search the existing knowledge base and cite the source filenames.”
- “Read this document's contents rather than reconstructing it from snippets.”
- “查知识库里的产品文档：支持哪些导入格式？标注来源。”
- “这个知识库有哪些文件？那份文档导入完成了吗？”

### Nearby but different

- Application installation or connection repair → `jishudb`.
- Discover external research reports → `research-report-hunter`.
