# Scnet 文档格式转化服务 API 文档

## 1. 功能介绍

Scnet 文档格式转化服务，支持将文档异步转换为可编辑的 Office 文件（Word / PPT），适用于大批量文档处理场景。

核心流程：

1. **任务提交**：通过 `doc/convert/task` 接口提交待转换的文件 URL 或本地文件，获取任务 ID；
2. **状态查询**：通过 `ocrdoc/result` 接口轮询任务状态，获取处理结果；
3. **结果获取**：任务成功后返回转换后的 Word / PPT 文件下载地址。

### 支持的文件类型

**文档格式**

| 类型 | 扩展名 |
|------|--------|
| PDF | .pdf |

**图片格式**

| 类型 | 扩展名 |
|------|--------|
| JPEG | .jpg / .jpeg |
| PNG | .png |
| BMP | .bmp |
| TIFF | .tiff / .tif |
| WebP | .webp |

说明：请根据转换类别（`ocr_type`）选择对应的输入文件——`PDF_TO_WORD` 输入 PDF，`IMAGE_TO_WORD` 与 `IMAGE_TO_PPT` 输入图片。

---

## 2. 文档格式转化任务提交 API

将文档解析（还原）为可编辑的 Office 文件，任务成功后返回 Word（`.docx`）或 PPT（`.pptx`）的 MinIO 文件下载地址。任务提交后同样通过任务状态查询 API 轮询结果。

### 2.1 端点信息

| 项目 | 内容 |
|------|------|
| URL | POST `/api/llm/v1/doc/convert/task` |
| Content-Type | `multipart/form-data` |
| 认证 | `Authorization: Bearer <token>` |

### 2.2 请求参数

**Header 参数**

| 名称 | 类型 | 必填 | 示例值 |
|------|------|------|--------|
| Content-Type | string | 是 | multipart/form-data |
| Authorization | string | 是 | Bearer `<API Key>` |

**Form 参数**

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| file | file | 否 | 本地上传的待转换文件。`file` 与 `file_url` 二选一，同时传入时优先使用 `file`。 |
| file_url | string | 否 | 待转换文件的公网可访问下载地址。`file` 与 `file_url` 二选一。 |
| ocr_type | string | 是 | 转换类别，可选值：`PDF_TO_WORD`（PDF 转 Word）、`IMAGE_TO_WORD`（图片转 Word）、`IMAGE_TO_PPT`（图片转 PPT）。 |
| page_index | string | 否 | 页码范围（如 `1` 或 `1-5`），默认全部解析。 |
| is_table_cls | boolean | 否 | 是否开启表格细分处理，默认 `false`。 |
| is_doc_ori | boolean | 否 | 是否开启文档方向矫正，默认 `false`。 |
| enforce_seal | boolean | 否 | 是否开启强制二次印章检测，默认 `false`。 |
| is_inline_formula | boolean | 否 | 是否开启行内公式检测，默认 `false`。 |

说明：`file` 与 `file_url` 二选一，必须至少提供一个，否则返回参数错误。

### 2.3 请求示例

**本地文件上传**

```bash
curl --location 'https://api.scnet.cn/api/llm/v1/doc/convert/task' \
--header 'Authorization: Bearer <API Key>' \
--form 'file=@"/path/to/document.pdf"' \
--form 'ocr_type="PDF_TO_WORD"'
```

**文件 URL 提交**

```bash
curl --location 'https://api.scnet.cn/api/llm/v1/doc/convert/task' \
--header 'Authorization: Bearer <API Key>' \
--form 'file_url="https://oss.ksai.scnet.cn:58043/ocr/doc/xxxxxx"' \
--form 'ocr_type="PDF_TO_WORD"'
```

### 2.4 响应参数

| 参数名称 | 参数类型 | 描述 |
|----------|----------|------|
| code | String | 状态码 |
| msg | String | 结果描述 |
| output | Object | 任务提交结果 |
| output.task_status | String | 任务状态（`pending` 待执行、`running` 执行中、`succeeded` 成功、`failed` 失败、`unknown` 任务不存在或未知状态） |
| output.task_id | String | 任务唯一标识，用于后续结果查询 |
| request_id | String | 请求唯一标识 |

### 2.5 响应示例

**成功响应**

```json
{
  "code": "0",
  "msg": "",
  "data": {
    "output": {
      "task_status": "pending",
      "task_id": "0385dc79-5ff8-4d82-bcb6-xxxxxx"
    },
    "request_id": "4909100c-7b5a-9f92-bfe5-xxxxxx"
  }
}
```

**失败响应**

```json
{
  "code": "10011",
  "msg": "Burst rate limit exceeded for model"
}
```

### 2.6 结果获取

文档格式转化任务通过任务状态查询 API 轮询状态。任务成功后，`output.results` 数组返回转换后的 Word 或 PPT 文件的 MinIO 下载地址。

```json
{
  "code": "0",
  "msg": "success",
  "data": [
    {
      "output": {
        "results": [
          "https://minio.fanhualuomu.top:8088/doc-convert/results/2026/05/19/2056703208598626305/document.docx?..."
        ],
        "task_id": "2056703208598626305",
        "task_status": "succeeded",
        "submit_time": "2026-05-19 19:47:11",
        "end_time": "2026-05-19 19:47:40"
      },
      "request_id": "5e726f4f7d518259"
    }
  ]
}
```

说明：`results` 中的下载地址后缀为 `.docx`（Word）或 `.pptx`（PPT），具体格式由转换任务的目标类型决定。下载地址为临时授权链接，请及时使用。

---

## 3. 任务状态查询 API

### 3.1 端点信息

| 项目 | 内容 |
|------|------|
| URL | POST `/api/llm/v1/ocrdoc/result` |
| 认证 | `Authorization: Bearer <token>` |

### 3.2 请求参数

**Header 参数**

| 名称 | 类型 | 必填 | 示例值 |
|------|------|------|--------|
| Authorization | string | 是 | Bearer `<API Key>` |

**Body 参数**

| 名称 | 类型 | 必填 | 描述 |
|------|------|------|------|
| task_ids | array | 是 | 任务 ID 列表 |

### 3.3 请求体示例

```json
{
  "task_ids": [
    "2056706028668284929",
    "2056703208598626305"
  ]
}
```

### 3.4 响应参数

| 参数名称 | 参数类型 | 描述 |
|----------|----------|------|
| code | String | 状态码 |
| msg | String | 结果描述 |
| data | Array | 任务结果列表（每个 task_id 对应一个元素） |
| data[].request_id | String | 请求唯一标识 |
| data[].output | Object | 任务结果 |
| data[].output.task_id | String | 任务唯一标识 |
| data[].output.task_status | String | 任务状态 |
| data[].output.submit_time | String | 任务提交时间 |
| data[].output.end_time | String | 任务结束时间（成功/失败时返回） |
| data[].output.results | Array | 结果文件下载地址列表（成功时返回） |
| data[].output.error_code | String | 错误码（失败时返回） |
| data[].output.error_message | String | 错误信息（失败时返回） |

### 3.5 响应示例

**任务成功**

```json
{
  "code": "0",
  "msg": "success",
  "data": [
    {
      "output": {
        "results": [
          "https://minio.fanhualuomu.top:8088/doc-convert/results/2026/05/19/2056703208598626305/document.docx?..."
        ],
        "task_id": "2056703208598626305",
        "task_status": "succeeded",
        "submit_time": "2026-05-19 19:47:11",
        "end_time": "2026-05-19 19:47:40"
      },
      "request_id": "5e726f4f7d518259"
    }
  ]
}
```

**任务进行中**

```json
{
  "code": "0",
  "msg": "",
  "data": [
    {
      "request_id": "8ae698ba-df2d-966c-abcf-xxxxxx",
      "output": {
        "task_id": "e56d806f-76f9-4037-aefa-xxxxxx",
        "task_status": "running",
        "submit_time": "2026-04-20 19:33:50.425"
      }
    }
  ]
}
```

**任务失败**

```json
{
  "code": "0",
  "msg": "",
  "data": [
    {
      "request_id": "c61fe158-c0de-40f0-b4d9-964625119ba4",
      "output": {
        "task_id": "86ecf553-d340-4e21-xxxxxxxxx",
        "task_status": "failed",
        "submit_time": "2025-11-11 11:46:28.116",
        "end_time": "2025-11-11 11:46:28.255",
        "error_code": "10011",
        "error_message": "Burst rate limit exceeded for model xxx"
      }
    }
  ]
}
```

---

## 4. 任务状态说明

| 状态 | 描述 |
|------|------|
| pending | 任务已提交，等待处理 |
| running | 任务处理中 |
| succeeded | 任务处理成功 |
| failed | 任务处理失败 |
| unknown | 任务不存在或未知状态 |

---

## 5. 错误码说明

| 错误码 | 描述 |
|--------|------|
| 10001 | Unknown error |
| 10002 | Unsupported modal type xxx |
| 10003 | Unsupported provider xxx |
| 10004 | Unsupported model xxx |
| 10005 | Model xxx not found |
| 10006 | Task not found |
| 10007 | Concurrency conflict for request, please try again later |
| 10008 | Provider xxx process error |
| 10009 | Model xxx route failed |
| 10010 | Illegal content detected by content approval |
| 10011 | Burst rate limit exceeded for model xxx |
| 10012 | An system error has occurred, please try again later |
| 10013 | Parameter illegal |
| 10014 | Incorrect API key provided |
| 10015 | Task timeout, please try again later |
