# 深知公文写作（Clawhub Public 版）

这是深知写作助手的 Clawhub 分发版本，显示名称为“深知公文写作”。功能逻辑与主干完整版保持一致，但不内置深知搜索 API Key；ClawHub 渠道只处理搜索 Key 获取方式和渠道注册链接差异。

## 能力范围

- 深知可信搜索：通过 `scripts/dkag_search.py` 调用搜索接口获取政策、数据和案例素材。
- 公文范文大纲：通过 `scripts/outline_reference.py` 在搜索前获取范文参考大纲和搜索建议。
- 公文写作流程：由 `SKILL.md` 进行任务路由，按任务复杂度选择直接生成、追问、搜索、审查或严格流水线。
- 搜索策略：`reference/search_policy.md` 保留深知搜索逻辑、素材四分类和来源限制。
- 任务路由：`reference/task_router.md` 定义简单任务、常规任务、复杂任务和高风险任务的处理方式。
- 质量审查：`reference/review_checklist.md` 定义公文内容、素材来源、文种专项和 Word 输出检查项。
- Word 排版：通过 `scripts/format_document.py` 生成普通格式 `.docx`。
- 素材来源说明：执行过搜索时，通过 `scripts/source_note_html.py` 生成独立 HTML 溯源页。
- 红头文件：通过 `scripts/template_generator.py` 代码化生成红头和表尾，不依赖 `templates/` 中的 Word 模板。
- PDF：当前版本不支持自动生成 PDF；用户明确要求 PDF 时，交付 `.docx` 并建议用户使用本机 Word/WPS 另存或导出为 PDF。

## 依赖

```bash
pip3 install python-docx requests
```

`Python`、`python-docx` 和 `requests` 是运行本 Skill 的必备前置条件。初始化检查如显示 `ready=false`，应先征得用户同意后安装缺失依赖，并重新检查通过后再继续执行搜索、Word、红头或素材来源 HTML 生成。

标准公文字体不随 Skill 分发，字体也不作为初始化阻断项。Word 文档会写入公文常用字体名称；如打开端缺少对应字体，Word/WPS 可能自动替换，需以本机打开后的显示为准。

如需要由 Agent 协助完成深知搜索账号注册，还需要 Node.js 18+：

```bash
node --version
```

当前版本不内置 PDF 生成或转换依赖。正式公文主交付物为 `.docx`；如用户需要 PDF，应使用 Word/WPS 打开 `.docx` 后另存或导出。

## API Key 配置

ClawHub Public 版不内置 API Key。当前版本将 `config.ini` 和有效 API Key 作为启动门禁：首次调用后必须先完成初始化检查，只有本地存在有效 `config.ini` 且配置了 API Key，才可以继续写作、改写、润色、审查、范文大纲、深知搜索、Word 生成或红头生成。

如果本地没有可用 `config.ini`，用户可选择以下任一方式配置：

1. 由 Agent 协助注册：用户明确同意后，Agent 调用 `scripts/register.mjs` 发送短信验证码、完成注册，并把返回的 API Key 写入本 Skill 根目录下的 `config.ini`。
2. 手动注册配置：用户通过 MaaS 管理平台获取 API Key 后，自行按本地环境配置。

未配置有效 API Key 前，不输出正文、草稿、大纲、示例通知、Word 文件或任何可替代正式写作结果。

MaaS 管理平台地址：

```text
https://platform.dknowc.cn/
```

新用户注册后会有 300 次体验额度；体验额度用完后，可到 MaaS 管理平台充值。完成实名认证后，平台也可能提供 100 元赠金，具体以 MaaS 平台页面展示为准。

ClawHub 版默认使用：

- 接入点 `type=6`，即深知可信搜索。
- 渠道码 `2787E171-B0E5-4328-9946-47AC52434D1F`。
- 搜索接口 `https://open.dknowc.cn/dependable/search/`。

协助注册第 1 步，发送短信验证码：

```bash
node scripts/register.mjs send --phone 13812345678
```

返回 `status=true` 后，暂停并请用户提供收到的 6 位验证码。

协助注册第 2 步，注册并获取 API Key：

```bash
node scripts/register.mjs register --phone 13812345678 --vcode 123456 --organ 个人 --name 用户
```

成功后，脚本会把 API Key 自动写入本 Skill 根目录下的 `config.ini`，不会在标准输出中返回完整 Key。`config.ini` 是敏感凭据文件，只存在于用户本地安装后的 Skill 目录中，不得上传、打包或公开分享。

手动配置入口：

```text
https://platform.dknowc.cn/
```

## 版本说明

当前 Clawhub Public 版为 `3.2.5`。

## 常用测试

语法检查：

```bash
python3 -m py_compile scripts/outline_reference.py scripts/dkag_search.py scripts/merge_search_results.py scripts/format_document.py scripts/template_generator.py scripts/initialize.py scripts/check_release.py scripts/source_note_html.py
node --check scripts/register.mjs
```

范文大纲生成：

```bash
python3 scripts/outline_reference.py "请写一份关于基层治理工作的调研报告，重点包括背景、做法、问题和建议。"
```

普通 Word 生成：

```bash
python3 scripts/format_document.py official-docs/input/dknowc-test.md --output dknowc-test.docx
```

红头 Word 生成：

```bash
python3 scripts/template_generator.py 通知 --input dknowc-test.docx --org "XX单位" --doc-number "XX〔2026〕1号" --output dknowc-test-red.docx
```

搜索结果保存：

```bash
python3 scripts/dkag_search.py "人才服务政策" --area 某省 --clean --output result_gd.json
```

多次搜索合并：

```bash
python3 scripts/merge_search_results.py result_gd.json result_bj.json --output merged.json
```

素材来源说明 HTML：

```bash
python3 scripts/source_note_html.py official-docs/input/source-note.json --output source-note.html
```

## Public 版说明

- 本版本不内置 API Key。
- 显示名称为“深知公文写作”，原“深知写作助手”作为项目/历史名称继续保留。
- API Key 是启动门禁；未配置有效 Key 前，不输出正文、草稿、大纲、示例通知、Word 或红头文件。
- 用户可选择 Agent 协助注册，也可选择到 MaaS 管理平台手动获取并配置。
- 公文范文大纲、深知搜索、素材分类、素材来源 HTML、Word 生成、红头文件、异常处理等功能逻辑与主干完整版一致。
