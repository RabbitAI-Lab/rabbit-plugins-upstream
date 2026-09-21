# 从 ClawHub v1.0.14 升级

当前 2.x 版本改用 AI Skills 平台统一 API。升级前保留旧配置并记录正在使用的功能；不要把密钥写入命令历史之外的日志、截图或聊天回复。

## 必须修改

- API 地址从 `https://mongol.open-idea.net` 改为 `https://ai-skills.open-idea.net/api/v1/mongolian-ai`。
- 旧版环境变量是 `MONGOL_AI_SKILL_API_KEY`，当前变量是 `MENGGUYU_API_KEY`。在平台产品页确认旧密钥已迁移或创建新产品密钥，再执行 `openclaw config set env.MENGGUYU_API_KEY "你的平台APIKey"` 并重启 Gateway。新接口验证成功前保留旧变量，以便回退。
- 当前所有上传文件解码后最大 5 MB；旧版约 10 MB 的文件必须先压缩或拆分。
- 付费 POST 必须提供 1–160 字符的唯一 `Idempotency-Key`；同一请求重试沿用原键，不能换键绕过处理中状态。

## 能力差异

- 翻译仍支持 zh、mw、mn 六方向；单次正文最多 4000 字符，长文由调用侧按自然段或句子拆分。
- OCR 支持 JPG/JPEG/PNG/BMP/WebP/TIFF 或 Base64，不再声明支持 GIF。
- ASR 支持同步与异步任务、私有状态查询和单次结算；当前公共契约不提供旧版任务取消接口。
- TTS 规范语言码为 mn-Cyrl、mn-Mong、zh-Hans、en，并兼容 mn、mw、zh。
- 对话模型、temperature 与 max_tokens 由平台管理，不接受客户端覆盖。
- PDF 新增阅读顺序和图片块 OCR；`ocr_language` 仅支持 mw、mn、zh。

## 验证

升级后先用一个短句调用翻译接口，确认返回结果和 `X-AI-Skills-Billing-*` 响应头，再处理文件或异步任务。401/403 表示密钥或产品权限不正确；不要通过反复创建新密钥或新幂等键重放付费操作。
