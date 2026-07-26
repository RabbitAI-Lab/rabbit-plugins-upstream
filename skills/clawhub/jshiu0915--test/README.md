# 音频转文字 Skill

使用百度智能云语音识别API将音频文件转换为文字。

## 功能特点

- 支持多种音频格式：wav、pcm、amr、m4a
- 支持多种语言：普通话、英语、粤语、四川话
- 批量处理音频文件
- 自动保存识别结果为文本文件和JSON文件
- 生成处理报告

## 前置要求

1. 百度智能云账号
2. 开通语音识别服务
3. 获取API Key和Secret Key

## 安装依赖

```bash
pip install -r requirements.txt
```

## 配置

1. 复制配置文件示例：
   ```bash
   cp config.example.json config.json
   ```

2. 编辑`config.json`文件，填入你的百度智能云API信息：
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

## 参数说明

- `api_key`: 百度智能云API Key（必填）
- `secret_key`: 百度智能云Secret Key（必填）
- `audio_dir`: 音频文件目录（默认：`./音频`）
- `text_dir`: 文字输出目录（默认：`./文字`）
- `file_format`: 音频文件格式（支持：pcm、wav、amr、m4a，默认：wav）
- `rate`: 采样率（支持：16000、8000，默认：16000）
- `dev_pid`: 语言模型ID
  - 1537: 普通话（默认）
  - 1737: 英语
  - 1637: 粤语
  - 1837: 四川话

## 使用方法

### 方法一：使用配置文件

```bash
python audio_to_text.py --config config.json
```

### 方法二：使用命令行参数

```bash
python audio_to_text.py \
  --api-key YOUR_API_KEY \
  --secret-key YOUR_SECRET_KEY \
  --audio-dir ./音频 \
  --text-dir ./文字 \
  --file-format wav \
  --rate 16000 \
  --dev-pid 1537
```

### 方法三：使用环境变量

```bash
export BAIDU_API_KEY=your_api_key
export BAIDU_SECRET_KEY=your_secret_key
python audio_to_text.py
```

### 方法四：在Claude Code中使用Skill命令

```bash
/claude skill 音频转文字 --api-key YOUR_API_KEY --secret-key YOUR_SECRET_KEY
```

## 文件结构

```
项目目录/
├── 音频/                    # 音频文件目录
│   ├── 录音1.wav
│   └── 录音2.wav
├── 文字/                    # 输出目录（自动创建）
│   ├── 录音1.txt           # 识别文本
│   ├── 录音1.json          # 完整JSON结果
│   ├── 录音2.txt
│   ├── 录音2.json
│   └── 处理报告_时间戳.json # 处理报告
└── .claude/skills/音频转文字/
    ├── skill.yaml          # Skill配置
    ├── audio_to_text.py    # 主程序
    ├── requirements.txt    # 依赖
    ├── config.example.json # 配置示例
    └── README.md           # 说明文档
```

## 输出文件

1. **文本文件（.txt）**: 纯文本识别结果
2. **JSON文件（.json）**: 完整的API响应，包含置信度等信息
3. **处理报告**: 包含所有文件处理状态的汇总报告

## 音频文件要求

- 支持格式：wav、pcm、amr、m4a
- 推荐采样率：16000Hz
- 声道：单声道
- 文件大小：建议不超过10MB
- 时长：建议不超过60秒（长音频可分片）

## 错误处理

- 自动重试获取访问令牌
- 详细的错误日志
- 失败文件单独记录
- 网络超时处理

## 注意事项

1. 百度语音识别API有调用频率限制，请勿频繁调用
2. 音频文件过大可能导致识别失败，建议分片处理
3. 确保网络连接正常
4. API Key和Secret Key请妥善保管

## 许可证

MIT