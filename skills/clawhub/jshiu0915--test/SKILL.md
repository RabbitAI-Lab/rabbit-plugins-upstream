# 音频转文字 Skill

在Claude Code中使用百度智能云语音识别API将音频文件转换为文字。

## 可用命令

- `音频转文字` - 中文命令
- `audio2text` - 英文命令

## 参数说明

所有参数都可以通过命令行传递，也可以通过配置文件或环境变量设置。

| 参数 | 类型 | 必填 | 默认值 | 描述 |
|------|------|------|--------|------|
| `api_key` | string | 是 | - | 百度智能云API Key |
| `secret_key` | string | 是 | - | 百度智能云Secret Key |
| `audio_dir` | string | 否 | `./音频` | 音频文件目录 |
| `text_dir` | string | 否 | `./文字` | 文字输出目录 |
| `file_format` | string | 否 | `wav` | 音频文件格式（pcm、wav、amr、m4a） |
| `rate` | integer | 否 | `16000` | 采样率（16000或8000） |
| `dev_pid` | integer | 否 | `1537` | 语言模型ID（1537-普通话，1737-英语，1637-粤语，1837-四川话） |

## 使用方法

### 方法1：使用命令行参数（推荐）

```bash
# 基本用法
/claude skill 音频转文字 \
  --api-key YOUR_API_KEY \
  --secret-key YOUR_SECRET_KEY

# 完整参数示例
/claude skill audio2text \
  --api-key YOUR_API_KEY \
  --secret-key YOUR_SECRET_KEY \
  --audio-dir ./音频 \
  --text-dir ./文字 \
  --file-format wav \
  --rate 16000 \
  --dev-pid 1537
```

### 方法2：使用配置文件

1. 创建配置文件 `config.json`：

```json
{
  "api_key": "你的API Key",
  "secret_key": "你的Secret Key",
  "audio_dir": "./音频",
  "text_dir": "./文字",
  "file_format": "wav",
  "rate": 16000,
  "dev_pid": 1537
}
```

2. 运行skill：

```bash
/claude skill 音频转文字 --config config.json
```

### 方法3：使用环境变量

```bash
# 设置环境变量
export BAIDU_API_KEY="你的API Key"
export BAIDU_SECRET_KEY="你的Secret Key"

# 运行skill（自动使用环境变量）
/claude skill 音频转文字
```

## 使用示例

### 示例1：转换普通话音频

```bash
/claude skill 音频转文字 \
  --api-key abc123def456 \
  --secret-key ghi789jkl012
```

### 示例2：转换英语音频

```bash
/claude skill audio2text \
  --api-key abc123def456 \
  --secret-key ghi789jkl012 \
  --dev-pid 1737  # 英语模型
```

### 示例3：自定义目录和格式

```bash
/claude skill 音频转文字 \
  --api-key abc123def456 \
  --secret-key ghi789jkl012 \
  --audio-dir /path/to/my/audio \
  --text-dir /path/to/output/text \
  --file-format pcm \
  --rate 8000
```

### 示例4：处理特定语言的音频

```bash
# 普通话（默认）
--dev-pid 1537

# 英语
--dev-pid 1737

# 粤语
--dev-pid 1637

# 四川话
--dev-pid 1837
```

## 文件结构要求

### 输入目录结构
```
项目目录/
└── 音频/                    # 音频文件目录（可通过--audio-dir修改）
    ├── 录音1.wav
    ├── 录音2.pcm
    └── 录音3.amr
```

### 输出目录结构
```
项目目录/
└── 文字/                    # 文字输出目录（可通过--text-dir修改）
    ├── 录音1.txt           # 识别文本
    ├── 录音1.json          # 完整JSON结果
    ├── 录音2.txt
    ├── 录音2.json
    └── 处理报告_时间戳.json # 处理报告
```

## 支持的音频格式

- **wav** (推荐) - 最高兼容性
- **pcm** - 原始音频数据
- **amr** - 自适应多速率音频
- **m4a** - MPEG-4音频

## 音频文件要求

- **采样率**: 16000Hz 或 8000Hz
- **声道**: 单声道
- **文件大小**: 建议小于10MB
- **时长**: 建议小于60秒（长音频可分片）

## 输出说明

### 文本文件 (.txt)
包含识别出的纯文本内容。

### JSON文件 (.json)
包含完整的API响应，包括：
- 识别文本
- 置信度分数
- 识别时长
- 原始API响应数据

### 处理报告 (.json)
包含批量处理的汇总信息：
- 处理文件总数
- 成功/失败数量
- 每个文件的处理状态
- 错误信息（如果有）

## 错误处理

skill会自动处理以下情况：
- API密钥无效或过期
- 网络连接问题
- 音频格式不支持
- 文件读取错误

错误信息会记录在日志和处理报告中。

## 注意事项

1. **API限制**: 百度语音识别API有每日免费额度，超出后会产生费用
2. **频率限制**: 避免频繁调用API，建议处理间隔至少1秒
3. **音频质量**: 清晰的音频可以获得更好的识别效果
4. **长音频处理**: 超过60秒的音频建议分割成小片段
5. **重要数据**: 建议先测试小片段，确认识别效果

## 故障排除

### 常见问题

1. **"获取token失败"**
   - 检查API Key和Secret Key是否正确
   - 确认百度智能云语音识别服务已开通

2. **"未找到音频文件"**
   - 检查`--audio-dir`参数指定的目录是否存在
   - 确认音频文件格式受支持（.wav, .pcm, .amr, .m4a）

3. **"音频格式不支持"**
   - 检查`--file-format`参数设置是否正确
   - 确认音频文件的采样率和声道符合要求

4. **网络连接问题**
   - 检查网络连接是否正常
   - 如果使用代理，确保正确配置

### 获取帮助

查看详细文档：
- [README.md](README.md) - 完整使用指南
- [audio_to_text.py](audio_to_text.py) - 源代码
- [config.example.json](config.example.json) - 配置文件示例

## 版本信息

- **当前版本**: 1.0.0
- **更新日期**: 2026-03-15
- **作者**: Claude Code

## 许可证

MIT