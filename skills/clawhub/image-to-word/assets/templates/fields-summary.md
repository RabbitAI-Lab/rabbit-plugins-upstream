# 文档格式转化任务字段说明

## 输出字段（submit_task 提交后返回）

| 字段 | 类型 | 说明 |
|------|------|------|
| code | String | 状态码，`0` 表示成功 |
| msg | String | 结果描述 |
| data | Object | 任务提交结果 |
| data.output.task_status | String | 任务状态（pending / running / succeeded / failed / unknown） |
| data.output.task_id | String | 任务唯一标识，用于后续结果查询 |
| request_id | String | 请求唯一标识 |

## 结果字段（ocrdoc/result 轮询成功后返回）

| 字段 | 类型 | 说明 |
|------|------|------|
| code | String | 状态码，`0` 表示成功 |
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

## 下载地址说明

- `results` 中的下载地址后缀为 `.docx`（Word）。
- 下载地址为临时授权链接，请及时使用。
