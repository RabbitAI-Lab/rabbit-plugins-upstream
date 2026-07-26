# vod_aigc_video — 详细参数与示例
> 此文件由 references 拆分生成，对应脚本：`scripts/vod_aigc_video.py`

## 参数说明
### 基础参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `--model` | enum | ✅ | 模型名称（GV/Hailuo/Kling/Jimeng/Vidu/Hunyuan/Mingmou/OS/Seedance/PixVerse） |
| `--model-version` | string | - | 模型版本（不填则使用默认版本） |
| `--prompt` | string | ❌* | 生成视频的提示词（当没有参考文件时必填） |
| `--negative-prompt` | string | ❌ | 要阻止模型生成视频的提示词（负面提示词） |
| `--enhance-prompt` | enum | ❌ | 是否自动优化提示词（Enabled: 开启, Disabled: 关闭） |

### 参考文件参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `--file-id` | string | ❌ | 参考文件的媒体文件 ID（单个值；多个参考图请使用 `--file-infos`） |
| `--file-url` | string | ❌ | 参考文件的 URL（单个值；多个参考图请使用 `--file-infos`） |
| `--file-infos` | JSON | ❌ | 多个参考图的 JSON 数组，格式：`[{"Type":"Url","Url":"...","Category":"Image","Usage":"Reference","Text":"pic1","ReferenceType":"subject","ObjectId":"..."}]`；支持 SDK 全字段：`Type`/`FileId`/`Url`/`Base64`/`Category`/`Usage`/`Text`/`ReferenceType`/`ObjectId`/`VoiceId`/`KeepOriginalSound` |
| `--file-category` | enum | ❌ | 单参考文件的分类：`Image`（图片）/ `Video`（视频）；用于 Kling motion_control / avatar_i2v 等场景区分图片/视频 |
| `--file-usage` | enum | ❌ | 单参考文件的用途：`FirstFrame`（首帧）/ `Reference`（参考帧）；PixVerse、Vidu、Kling 多模式区分用 |
| `--file-text` | string | ❌ | 单参考文件的命名/描述（仅 PixVerse 多图主体参考生效，用于 Prompt 中 `@name` 引用，例如 Text=`pic1` 后可在 Prompt 写 `@pic1 走路`）|
| `--reference-type` | enum | ❌ | 单参考文件的参考类型：`subject`（主体）/ `background`（背景）/ `mask`（蒙版）；PixVerse 视频编辑用 subject/background；GV/Kling 也适用 |

### 首尾帧生成参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `--last-frame-file-id` | string | ❌ | 尾帧文件的媒体文件 ID（用于首尾帧生成） |
| `--last-frame-url` | string | ❌ | 尾帧文件的 URL（用于首尾帧生成） |

### 输出配置参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `--output-storage-mode` | enum | ❌ | 存储模式（Permanent: 永久存储, Temporary: 临时存储，默认 Temporary） |
| `--output-media-name` | string | ❌ | 输出文件名（最长 64 个字符） |
| `--output-class-id` | int | ❌ | 分类 ID（默认 0，表示其他分类） |
| `--output-expire-time` | string | ❌ | 输出文件的过期时间（ISO 8601 格式，如 2026-12-31T23:59:59+08:00） |
| `--output-duration` | int | ❌ | 生成视频的时长（秒，不同模型支持的时长不同） |
| `--output-resolution` | enum | ❌ | 生成视频的分辨率（不同模型支持的分辨率不同） |
| `--output-aspect-ratio` | enum | ❌ | 指定所生成视频的宽高比（不同模型支持的宽高比不同） |
| `--output-audio-generation` | enum | ❌ | 是否生成音频（Enabled: 开启, Disabled: 关闭，默认 Disabled；GV/OS/Vidu 支持） |
| `--output-person-generation` | enum | ❌ | 是否允许人物或人脸生成（AllowAdult: 允许, Disallowed: 禁止） |
| `--output-enhance-switch` | enum | ❌ | 是否启用视频增强（Enabled/Disabled；分辨率超过模型直出能力时默认启用） |
| `--output-off-peak` | enum | ❌ | 是否开启错峰（Enabled: 开启, Disabled: 关闭） |
| `--output-frame-interpolate` | enum | ❌ | 是否开启 Vidu 智能插帧（Enabled: 开启, Disabled: 关闭） |
| `--output-logo-add` | enum | ❌ | 是否开启图标水印（Enabled: 开启, Disabled: 关闭；目前仅 Vidu 支持） |
| `--input-compliance-check` | enum | ❌ | 是否开启输入内容的合规性检查（Enabled: 开启, Disabled: 关闭） |
| `--output-compliance-check` | enum | ❌ | 是否开启输出内容的合规性检查（Enabled: 开启, Disabled: 关闭） |

### 其他参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `--procedure` | string | ❌ | 任务流名称，生成视频后自动执行指定任务流 |
| `--seed` | int | ❌ | 模型随机种子（指定后可复现生成结果） |
| `--input-region` | enum | ❌ | 输入文件的区域信息（Mainland: 国内, Oversea: 国外，默认 Mainland） |
| `--scene-type` | enum | ❌ | 场景类型（motion_control: 动作控制/Kling, avatar_i2v: 数字人/Kling, lip_sync: 对口型/Kling, template_effect: 特效模板/Vidu, subject_reference: 固定主体参考/Vidu） |
| `--subject-infos` | JSON | ❌ | 固定主体 JSON 数组，格式：`[{"Id":"...","Name":"..."}]`（⚠️ SDK 暂不支持，参数可传入但当前不生效） |
| `--element-ids` | string | ❌ | 高级自定义主体 ID（逗号分隔，如 `865750283577090106`），与 `--ext-info` 互斥，优先级更高 |
| `--elements-file` | path | ❌ | 从 JSON 文件读取主体 ID 列表（如 `mem/elements.json`），与 `--element-ids` 互斥 |
| `--session-id` | string | ❌ | 用于去重的识别码（最长 50 个字符，三天内重复会返回错误） |
| `--session-context` | string | ❌ | 来源上下文，用于透传用户请求信息（最长 1000 个字符） |
| `--tasks-priority` | int | ❌ | 任务优先级（数值越大优先级越高，范围 -10 到 10） |
| `--ext-info` | string | ❌ | 保留字段，特殊用途时使用（与 `--element-ids` 互斥，优先级更低） |

### 通用参数（仅 `create` 子命令支持）

| 参数 | 类型 | 说明 |
|------|------|------|
| `--sub-app-id` | int | 子应用 ID（从 2023 年 12 月 25 日起开通点播的客户必须填写，也可通过环境变量 TENCENTCLOUD_VOD_SUB_APP_ID 设置） |
| `--region` | string | 腾讯云区域（默认 ap-guangzhou） |
| `--json` | flag | JSON 格式输出 |
| `--dry-run` | flag | 只打印请求参数预览，不发送请求 |
| `--no-wait` | flag | 仅提交任务，不等待结果（默认自动等待） |
| `--max-wait` | int | 最大等待时间（秒，默认 1800） |

> ⚠️ **注意**：`vod_aigc_video.py` **没有 `query` 子命令**。查询生视频任务状态请使用 `vod_describe_task.py --task-id <task_id>`。

### 模型参数限制对比

#### Hailuo（海螺）

| 参数 | 支持值 |
|------|--------|
| 版本 | 02, 2.3, 2.3-fast |
| 时长 | **02：6/8/10/12/15/20s（实测最长 20s+）；2.3 / 2.3-fast：6s, 10s（默认 6s）** |
| 分辨率 | 768P, 1080P（默认 768P） |
| 宽高比 | 不支持 |
| 首尾帧生成 | 不支持 |
| 音频生成 | 不支持 |
| 备注 | 02 是最新版本，时长上限远超 2.3 系列；接口实测确认 02 最长可达 20s 以上 |

#### Kling（可灵）

| 参数 | 支持值 |
|------|--------|
| 版本 | 1.6, 2.0, 2.1, 2.5, O1, 2.6, 3.0, 3.0-Omni, 3.0-turbo |
| 时长 | 5s, 10s（默认 5s） |
| 分辨率 | **720P, 1080P, 4K（默认 720P；接口实测 2.1/3.0/3.0-Omni/3.0-turbo/O1/2.6 都接受 4K）** |
| 宽高比 | 16:9, 9:16, 1:1（默认 16:9） |
| 首尾帧生成 | 支持（2.1 版本必须指定 1080P） |
| 场景类型 | motion_control（动作控制）, avatar_i2v（数字人）, lip_sync（对口型） |
| 音频生成 | 3.0-Omni 支持有声/无声（OutputConfig.AudioGeneration: Enabled/Disabled） |

#### Jimeng（即梦）

| 参数 | 支持值 |
|------|--------|
| 版本 | 3.0pro |
| 分辨率 | **通过 ExtInfo `width`/`height` 自定义**；示例 `--ext-info '{"AdditionalParameters": "{\"width\":1920, \"height\":1080}"}'` |
| 首尾帧生成 | 不支持 |
| 音频生成 | 不支持 |
| 备注 | 即梦视频侧不支持 OutputConfig.Resolution / AspectRatio，需通过 ExtInfo 透传分辨率 |

#### Vidu（生数）

| 参数 | 支持值 |
|------|--------|
| 版本 | q2, q2-turbo, q2-pro, q3, q3-pro, q3-turbo, q3-mix, q3-drama |
| 时长 | 1-10 秒（自定义） |
| 分辨率 | 720P, 1080P（默认 720P） |
| 宽高比 | 16:9, 9:16, 1:1, 3:4, 4:3（默认 16:9） |
| 首尾帧生成 | 支持（q2-pro, q2-turbo; q3-pro 仅支持文生和图生） |
| 多图参考 | q2 支持 1-7 张，通过 FileInfos 中的 ObjectId 作为主体 ID 传入 |
| 场景类型 | template_effect（特效模板）, subject_reference（固定主体参考） |
| 特色 | q3-mix: 画面质感强，支持智能切镜，动态效果好；q3: 支持智能切镜，多机位一致性出色 |
| 备注 | **🚨 q3-mix / q3-drama 必须传参考图且 `Usage=Reference`**（接口实测：纯文生会报错 `only supports reference generation`）；q3-mix 暂不支持主体库调用 |

#### Hunyuan（混元）

| 参数 | 支持值 |
|------|--------|
| 版本 | 1.5, 3d_2.0 |
| 场景类型 | `3d_scene`（仅 3d_2.0：混元世界模型生 3D 场景视频）|
| 时长 | 3d_2.0 + 3d_scene 推荐 16s（OutputConfig.Duration）|
| 分辨率 | 3d_2.0 + 3d_scene 推荐 1080P |
| 音频生成 | 3d_2.0 + 3d_scene 支持 `OutputConfig.AudioGeneration: Enabled` |
| 存储模式 | **3d_2.0 仅支持 `Temporary`**（接口实测：传 Permanent 会报 `StorageMode Permanent is not supported for model Hunyuan 3d_2.0`）|
| 首尾帧生成 | 不支持 |
| 输出产物 | 3d_2.0 + 3d_scene 输出多个文件：spz（高斯溅射）/ ply（点云）等，可导入 Unity/Unreal Engine |
| 备注 | **3d_2.0** 配合 `--scene-type 3d_scene` 用于生成 3D 可漫游场景视频（混元世界模型）；**1.5** 是早期通用视频版本 |

#### Mingmou（明眸）

| 参数 | 支持值 |
|------|--------|
| 版本 | 1.0 |
| 分辨率 | **通过 ExtInfo `width`/`height` 自定义**；示例 `--ext-info '{"AdditionalParameters": "{\"width\":1920, \"height\":1080}"}'` |
| 首尾帧生成 | 不支持 |
| 音频生成 | 不支持 |

#### GV（GV，Google Veo）

| 参数 | 支持值 |
|------|--------|
| 版本 | 3.1, 3.1-fast, 3.1-lite |
| 时长 | 固定 8 秒 |
| 分辨率 | 720P, 1080P（默认 720P） |
| 宽高比 | 16:9, 9:16（默认 16:9） |
| 多图参考 | 最多 3 张 |
| 首尾帧生成 | 支持 |
| 音频生成 | 音画同出，支持有声/无声 |
| 备注 | 不拦截人脸；使用多图输入时不可同时使用 LastFrameFileId/LastFrameUrl |

#### OS（OS）

| 参数 | 支持值 |
|------|--------|
| 版本 | 2.0 |
| 时长 | 4s, 8s, 12s（默认 8s） |
| 分辨率 | 固定 720P |
| 宽高比 | 16:9, 9:16（默认 16:9） |
| 首尾帧生成 | 不支持 |

#### Seedance（豆包视频）

| 参数 | 支持值 |
|------|--------|
| 版本 | 1.0-pro, 1.0-lite-i2v, 1.0-pro-fast, 1.5-pro |
| 音频生成 | 1.5-pro 支持有声/无声（OutputConfig.AudioGeneration: Enabled/Disabled） |
| 分辨率 | 1.5-pro 不支持 1080P |
| 备注 | **接口名为 `Seedance`**（早先文档误写 `SV` 是错的，接口实测会报 `ModelName SV is invalid`）；Seedance 是 ByteDance 字节豆包视频系列 |

#### PixVerse（PixVerse）

| 参数 | 支持值 |
|------|--------|
| 版本 | v5.6, v6, c1 |
| 音频生成 | v5.6（无声）；v6/c1 支持有声/无声 |
| 时长 | c1/v6：1-15 秒（1080P 最高 15s）；v5.6：5/8/10s（1080p 不支持 10s）|
| 分辨率 | **360P, 540P, 720P, 1080P, 4K**（接口实测 v5.6/v6/c1 都接受 4K）|
| 多图参考 | c1/v6：最多 7 张主体；v5.6：最多 7 张参考视频 |
| 首尾帧生成 | 支持（搭配 `--file-usage FirstFrame` + `--last-frame-url/--last-frame-file-id`）|
| 多图主体（@name 引用）| c1/v6 多图模式必须 `Category=Image` + `Usage=Reference`；通过 `--file-text` 或 file-infos `Text` 给图命名（如 `pic1`），Prompt 内用 `@pic1` 精确引用 |
| 视频编辑 | v5.6/v6/c1 支持视频编辑：参考视频用 `--file-category Video` + `--reference-type subject`（改主体）或 `background`（改背景）|
| 备注 | c1 是最新角色一致性版本；v6 通用旗舰；v5.6 上一代稳定版；不支持 SceneType（motion_control/avatar_i2v/lip_sync 仅 Kling 用）|

### 任务状态说明

| 状态 | 说明 |
|------|------|
| WAIT | 等待中 |
| RUN | 处理中 |
| FINISH | 已完成 |
| FAIL | 失败 |

### API 接口对应关系

| 功能 | API 接口 | 文档链接 |
|------|---------|---------|
| 创建 AIGC 生视频任务 | `CreateAigcVideoTask` | https://cloud.tencent.com/document/api/266/126239 |
| 查询任务状态 | `DescribeTaskDetail` | https://cloud.tencent.com/document/api/266/33431 |

### 错误码说明

| 错误类型 | 原因 | 处理建议 |
|---------|------|---------|
| 模型版本不支持 | 指定的 ModelVersion 不存在 | 查看支持的模型列表，选择正确的版本 |
| 分辨率不支持 | 指定的 Resolution 模型不支持 | 查看模型特性表格，选择支持的分辨率 |
| 宽高比不支持 | 指定的 AspectRatio 模型不支持 | 查看模型特性表格，选择支持的宽高比 |
| 参考图数量超限 | 提供的参考图数量超过模型限制 | 查看模型特性表格，限制在允许范围内 |
| Prompt 必填 | 未提供 Prompt 且没有参考图 | 添加 --prompt 参数或提供参考图 |
| SubAppId 必填 | 未指定子应用 ID | 添加 --sub-app-id 参数或设置环境变量 |
| 首尾帧限制 | Kling 2.1 首尾帧必须指定 1080P | 调整分辨率为 1080P 或更换模型版本 |
| 会话重复 | SessionId 在 3 天内重复使用 | 更换 SessionId 或等待过期 |

---


---


## 使用示例
### 1 基础文生视频

#### GV 模型文生视频
```bash
python3 scripts/vod_aigc_video.py create \
    --model GV \
    --prompt "一只小狗在草地上奔跑，阳光明媚"
```

#### Hailuo 模型（指定分辨率和时长）
```bash
python3 scripts/vod_aigc_video.py create \
    --model Hailuo \
    --model-version 2.3 \
    --prompt "海边日落的延时摄影" \
    --output-resolution 1080P \
    --output-duration 10
```

#### Kling 模型（高清 1080P，5 秒）
```bash
python3 scripts/vod_aigc_video.py create \
    --model Kling \
    --model-version 2.1 \
    --prompt "城市夜景的航拍镜头" \
    --output-resolution 1080P \
    --output-duration 5 \
    --output-aspect-ratio 16:9
```

#### Kling O1 模型 + 自定义主体（element-ids）
> ⚠️ **注意**：`--model` 只传 `Kling`，版本号 `O1` 通过 `--model-version` 单独传入，禁止写成 `--model "Kling O1"`。
> ⚠️ **注意**：使用 `--element-ids` 时，`--prompt` 中必须用 `<<<element_1>>>` 占位符替换主体称谓。
```bash
python3 scripts/vod_aigc_video.py create \
    --model Kling \
    --model-version O1 \
    --element-ids "866084540648271963" \
    --prompt "<<<element_1>>>在海边行走" \
    --sub-app-id 1500046725
```

### 2 图生视频

#### 使用 FileId 作为首帧
```bash
python3 scripts/vod_aigc_video.py create \
    --model Kling \
    --model-version 2.1 \
    --file-id 3704211509819 \
    --prompt "让图片中的人物慢慢走动起来"
```

#### 使用 URL 作为首帧
```bash
python3 scripts/vod_aigc_video.py create \
    --model GV \
    --file-url "https://example.com/first_frame.jpg" \
    --prompt "相机缓慢向前推进"
```

### 3 首尾帧生视频

```bash
python3 scripts/vod_aigc_video.py create \
    --model GV \
    --file-url "https://example.com/first.jpg" \
    --last-frame-url "https://example.com/last.jpg" \
    --prompt "smooth transition between the two scenes"
```

### 4 默认等待任务完成

```bash
# 生视频耗时较长（已设置默认 1800 秒超时）
python3 scripts/vod_aigc_video.py create \
    --model GV \
    --prompt "一只猫在窗边晒太阳"

# 不等待，仅提交任务
python3 scripts/vod_aigc_video.py create \
    --model GV \
    --prompt "一只猫在窗边晒太阳" \
    --no-wait
```

### 5 永久存储

```bash
python3 scripts/vod_aigc_video.py create \
    --model Hailuo \
    --prompt "风景视频" \
    --output-storage-mode Permanent \
    --output-media-name "我的生成视频"
```

### 6 查看支持的模型

```bash
python3 scripts/vod_aigc_video.py models
```

## 7 PixVerse 高级特性

### 7.1 多图主体参考（@name 引用）

c1 / v6 支持最多 7 张参考图，通过 `Text` 给每张图命名，Prompt 内用 `@name` 精确引用。

**JSON 多图模式（推荐）：**

```bash
python3 scripts/vod_aigc_video.py create \
    --model PixVerse --model-version c1 \
    --prompt "@pic1 中身着古装的女性拿着 @pic2 (闭合状态)，慢慢展开折扇" \
    --file-infos '[
        {"Type":"Url","Url":"https://e.com/woman.jpg","Category":"Image","Usage":"Reference","Text":"pic1"},
        {"Type":"Url","Url":"https://e.com/fan.jpg","Category":"Image","Usage":"Reference","Text":"pic2"}
    ]' \
    --output-storage-mode Temporary \
    --output-duration 8 --output-aspect-ratio 3:4 \
    --output-audio-generation Enabled \
    --sub-app-id 1308104797
```

> ⚠️ **必须满足**：每张图都要 `Category=Image` + `Usage=Reference` + `Text=<name>`；Prompt 引用 `@name` 后必须有空格（如 `@pic1 走路`）；Text 仅纯中英文，不能含特殊字符。

### 7.2 视频编辑（subject / background）

v5.6 / v6 / c1 支持以一段视频为输入做"换主体"或"换背景"，通过 `ReferenceType` 区分。

**示例 1：替换主体（女主裙子换白色）：**

```bash
python3 scripts/vod_aigc_video.py create \
    --model PixVerse --model-version v5.6 \
    --prompt "把视频女主角裙子的颜色改成白色" \
    --file-url "https://e.com/source.mp4" \
    --file-category Video \
    --reference-type subject \
    --output-storage-mode Permanent \
    --output-media-name "PixVerse视频编辑" \
    --sub-app-id 1308104797
```

**示例 2：首尾帧（FirstFrame + LastFrame）：**

```bash
python3 scripts/vod_aigc_video.py create \
    --model PixVerse --model-version v6 \
    --prompt "smooth transition from sunrise to sunset" \
    --file-url "https://e.com/first.jpg" \
    --file-usage FirstFrame \
    --last-frame-url "https://e.com/last.jpg" \
    --output-duration 5 \
    --sub-app-id 1308104797
```

> ⚠️ **首帧 vs 参考**：单图 PixVerse 默认首帧；如要参考生视频则必须 `--file-usage Reference`（或 file-infos 里 Usage=Reference）；多图模式默认参考生（每张图都需带 Usage）。

### 7.3 PixVerse 与其他模型对比

| 能力 | c1 | v6 | v5.6 |
|---|---|---|---|
| 文生视频 | ✅ | ✅ | ✅ |
| 图生视频 | ✅ | ✅ | ✅ |
| 参考生视频 | ✅ | ✅ | （仅参考视频）|
| 最大参考图 | 7 张 | 7 张 | 7 张 |
| 1080P 最长 | 15s | 15s | 8s |
| 音画同出 | ✅ | ✅ | ❌ |

## 8 Hunyuan 3D 模型生视频（混元世界模型）

`Hunyuan 3d_2.0` 配合 `--scene-type 3d_scene` 生成 3D 可漫游场景视频，支持音画同出。

### 8.1 文生 3D 场景视频

```bash
python3 scripts/vod_aigc_video.py create \
    --model Hunyuan --model-version 3d_2.0 \
    --scene-type 3d_scene \
    --prompt "故宫太和殿正午阳光，超写实历史复原风格，PBR 材质" \
    --output-storage-mode Temporary \
    --output-duration 16 \
    --output-resolution 1080P \
    --output-audio-generation Enabled \
    --sub-app-id 1308104797
```

> ⚠️ **3d_2.0 仅支持 Temporary 存储**——传 `Permanent` 会被接口拒绝。Temporary 模式下产物有效期 7 天。

> 📦 **输出产物**：本场景输出 6 个文件，包含 1 个 `.spz`（高斯溅射模型）+ 多个 `.ply`（点云）等，原生支持 Unity/Unreal Engine 导入。

### 8.2 与混元 1.5 / 3d_panorama 区别

| 用途 | 模型 + 版本 | 接口 | SceneType |
|---|---|---|---|
| 通用视频（旧版）| `Hunyuan 1.5` | `vod_aigc_video.py` | （无）|
| 360° 全景图（生图侧）| `Hunyuan 3d_2.0` | `vod_aigc_image.py` | `3d_panorama` |
| 3D 场景视频（生视频侧）| `Hunyuan 3d_2.0` | `vod_aigc_video.py` | `3d_scene` |

> 混元世界模型的 3D 场景视频输出可包含 3DGS（高斯溅射）/ Mesh（GLB/FBX/OBJ）/ PLY（点云）/ 全景视频，原生支持 Unity/Unreal Engine。

## 9 Kling 高级场景（动作控制 / 对口型 / 数字人）

Kling 通过 `--scene-type` 区分高级场景，复杂参数通过 `--ext-info` 透传 JSON。

### 9.1 动作控制（motion_control）

**版本要求**：`3.0` 用 3.0 版动作控制；`2.6` 用旧版（2.6 也是 motion_control 的标准入口）。

```bash
python3 scripts/vod_aigc_video.py create \
    --model Kling --model-version 2.6 \
    --scene-type motion_control \
    --prompt "参考视频生成一个新视频" \
    --file-infos '[
        {"Type":"Url","Url":"https://e.com/ref.mp4","Category":"Video"},
        {"Type":"Url","Url":"https://e.com/face.webp","Category":"Image"}
    ]' \
    --ext-info '{"AdditionalParameters":"{\"keep_original_sound\":\"no\",\"character_orientation\":\"video\"}"}' \
    --sub-app-id 1308104797
```

**ExtInfo 关键参数**：
- `keep_original_sound`: `yes`（保留原声）/ `no`
- `character_orientation`: `image`（与图片人物朝向一致，参考视频 ≤ 10s）/ `video`（与视频人物朝向一致，参考视频 ≤ 30s）

### 9.2 对口型（lip_sync，需先调 DescribeAigcFaceInfo）

**两步流程**：
1. 先用 `DescribeAigcFaceInfo` 获取 `SessionId` 和 `FaceId`（注：当前 skill **未实现**该接口，需手工调 SDK 或 API）
2. 再调 `CreateAigcVideoTask`，`SceneType=lip_sync` + `ExtInfo` 透传 face 信息

```bash
python3 scripts/vod_aigc_video.py create \
    --model Kling --model-version 2.6 \
    --scene-type lip_sync \
    --prompt "对口型" \
    --ext-info '{"AdditionalParameters":"{\"session_id\":\"845736590818832460\",\"face_choose\":[{\"face_id\":0,\"sound_file\":\"https://e.com/audio.mp3\",\"sound_start_time\":0,\"sound_end_time\":5000,\"sound_insert_time\":2000,\"sound_volume\":2,\"original_audio_volume\":0}]}"}' \
    --sub-app-id 1308104797
```

> ⚠️ **lip_sync 不传 FileInfos**——音频/视频信息全部走 `ExtInfo`（session_id + face_choose）；FileInfos 留空。

### 9.3 数字人（avatar_i2v）

```bash
python3 scripts/vod_aigc_video.py create \
    --model Kling --model-version 2.6 \
    --scene-type avatar_i2v \
    --prompt "dance" \
    --file-url "https://e.com/portrait.png" \
    --file-category Image \
    --ext-info '{"AdditionalParameters":"{\"sound_file\":\"https://e.com/audio.mp3\"}"}' \
    --sub-app-id 1308104797
```

**ExtInfo 关键参数**：
- `sound_file`：音频 URL 或 Base64（mp3/wav/m4a/aac，≤5MB，2-300 秒）
- `audio_id`：音频 ID（与 sound_file 二选一）
- `sound_file` 与 `audio_id` 不能同时为空，也不能同时有值

## 10 AIGC 超分输出策略

通过 `--output-resolution` + `--output-enhance-switch` 组合实现"模型直出低分辨率 + 超分到高分辨率"的成本优化方案。

### 10.1 超分到 1080P（成本优化）

```bash
# 模型直出 720P，再超分到 1080P（比直接 1080P 便宜）
python3 scripts/vod_aigc_video.py create \
    --model GV --model-version 3.1 \
    --prompt "让文字飞起来" \
    --file-url "https://e.com/logo.webp" \
    --output-resolution 1080P \
    --output-enhance-switch Enabled \
    --sub-app-id 1308104797
```

### 10.2 输出 2K / 4K（默认开启超分）

```bash
# 选 2K/4K 时 EnhanceSwitch 默认 Enabled，无需手动指定
python3 scripts/vod_aigc_video.py create \
    --model GV --model-version 3.1 \
    --prompt "微笑的向我走来" \
    --output-resolution 2K \
    --sub-app-id 1308104797
```

### 10.3 各模型分辨率支持速查

| 模型 | 支持的分辨率 |
|---|---|
| Kling | **720P, 1080P, 4K**（默认 720P；接口实测全版本接受 4K）|
| Jimeng | **仅 ExtInfo `width`/`height`** 自定义（不支持 OutputConfig.Resolution）|
| Hailuo | 768P, 1080P（默认 768P）|
| Vidu | 720P, 1080P（默认 720P）|
| GV | 720P, 1080P（默认 720P）|
| OS | 720P 标准；也支持 ExtInfo `width`/`height` 自定义 |
| PixVerse | **360P, 540P, 720P, 1080P, 4K**（接口实测全版本接受 4K）|
| Seedance | 1.0-pro/1.0-pro-fast 多档；1.5-pro 不支持 1080P |
| Mingmou | **仅 ExtInfo `width`/`height`** 自定义 |
| Hunyuan 1.5 | **仅 ExtInfo `size`** 自定义 |
| Hunyuan 3d_2.0 + 3d_scene | 1080P（推荐）|

> 上表为模型直出能力。**所有模型**都可叠加 `--output-enhance-switch Enabled` 输出 2K/4K（选 2K/4K 时默认开启）。

---

## 11 视频侧 ExtInfo 自定义分辨率（width/height/size）

部分视频模型不支持 `--output-resolution` 标准参数，需通过 `--ext-info` 透传自定义分辨率（与生图侧 §13 类似）。

### 11.1 Jimeng 3.0pro 自定义 width/height

```bash
python3 scripts/vod_aigc_video.py create \
    --model Jimeng --model-version 3.0pro \
    --prompt "古风少女舞剑" \
    --ext-info '{"AdditionalParameters": "{\"width\":1920, \"height\":1080}"}' \
    --output-storage-mode Temporary \
    --sub-app-id 1308104797
```

### 11.2 Hunyuan 1.5 自定义 size

```bash
python3 scripts/vod_aigc_video.py create \
    --model Hunyuan --model-version 1.5 \
    --prompt "云朵飘动" \
    --ext-info '{"AdditionalParameters": "{\"size\":\"1280x720\"}"}' \
    --output-storage-mode Temporary \
    --sub-app-id 1308104797
```

### 11.3 OS 2.0 自定义 width/height

```bash
python3 scripts/vod_aigc_video.py create \
    --model OS --model-version 2.0 \
    --prompt "abstract liquid flowing" \
    --ext-info '{"AdditionalParameters": "{\"width\":1920, \"height\":1080}"}' \
    --output-storage-mode Temporary \
    --sub-app-id 1308104797
```

### 11.4 Mingmou 1.0 自定义 width/height

```bash
python3 scripts/vod_aigc_video.py create \
    --model Mingmou --model-version 1.0 \
    --prompt "城市黄昏天际线" \
    --ext-info '{"AdditionalParameters": "{\"width\":1920, \"height\":1080}"}' \
    --output-storage-mode Temporary \
    --sub-app-id 1308104797
```

### 11.5 视频侧 ExtInfo 自定义分辨率 vs OutputConfig 对比

| 模型 | 标准 `--output-resolution` | ExtInfo 自定义分辨率 |
|---|---|---|
| **Jimeng 3.0pro** | ❌ 不支持 | ✅ `width`/`height` |
| **Hunyuan 1.5** | ❌ 不支持 | ✅ `size` |
| **OS 2.0** | ✅ 720P 直出 | ✅ `width`/`height` 也支持 |
| **Mingmou 1.0** | ❌ 不支持 | ✅ `width`/`height` |
| 其他模型（Kling/Vidu/GV/Hailuo/PixVerse/Seedance）| ✅ 支持 | — |

---

## 12 接口实测发现的关键约束

> 这些约束已通过真接口提交验证（2026-06-30）

### 12.1 ModelName 接口名实测

| ModelName | 接口实测 | 说明 |
|---|---|---|
| `Seedance` | ✅ 接受 | **真接口名**（豆包视频系列）|
| `SV` | ❌ **拒绝**：`ModelName SV is invalid` | 早先 skill 写法错误，已修正 |
| `GV` | ✅ 接受 | Google Veo（无别名，`Veo`/`GoogleVeo` 都被拒）|
| `Hailuo` | ✅ 接受 | MiniMax 海螺（无别名，`MiniMax` 被拒）|
| `Kling`/`Jimeng`/`Vidu`/`Hunyuan`/`Mingmou`/`OS`/`PixVerse` | ✅ 接受 | 接口唯一名，无别名 |

### 12.2 Vidu q3-mix / q3-drama 限制

接口实测：

```
model Vidu q3-mix only supports reference generation, all FileInfos must have Usage=Reference
model Vidu q3-drama only supports reference generation, FileInfos or SubjectInfos is required
```

**正确用法**：

```bash
python3 scripts/vod_aigc_video.py create \
    --model Vidu --model-version q3-mix \
    --prompt "电影级镜头，光影自然" \
    --file-url "https://e.com/ref.jpg" \
    --file-usage Reference \
    --sub-app-id 1308104797
```

---


