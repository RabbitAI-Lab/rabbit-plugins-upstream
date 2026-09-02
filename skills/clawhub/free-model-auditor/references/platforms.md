# 各平台审计知识库

按厂商的「如何判定模型免费」策略、已知免费模型、排除项与能力标记。这是免费模型审计员依赖的隐性知识——
通用 `/v1/models` 调用无法获得。

> **安装即用 / 路径自动识别**：本技能不依赖任何写死的绝对路径。启动时由
> `references/resolve_paths.py` 自动探测两处路径——配置根（按 `WORKBUDDY_CONFIG_DIR` →
> `CODEBUDDY_CONFIG_DIR` → `~/.workbuddy` 回退，指向 `models.json`）与工作区根（agent 当前 cwd
> 或 `--workspace` 参数，指向审计报告 + 每日日志）。**接手的其他用户无需改动任何路径配置**即可
> 直接运行；仅当 `models.json` 探测不到时才会向你询问具体路径。

## 海外主机集合（触发 SKILL.md 中的 VPN 门禁）

| 主机 | 厂商 | 需 VPN/代理 |
|---|---|---|
| `generativelanguage.googleapis.com` | Google Gemini | **需要**（地域封锁） |
| `integrate.api.nvidia.com` | NVIDIA NIM | 受限网络下需要（经 `127.0.0.1:7897` 走代理） |

其余厂商均为国内（中国部署），无需 VPN。

---

## 1. Google Gemini

- **端点**：`https://generativelanguage.googleapis.com/v1beta/openai`（OpenAI 兼容）。
  ⚠️ 路径**必须**是 `/v1beta/openai`；只用 `/v1beta` 会让 WorkBuddy 拼出错误 URL。
- **海外**：是 → 适用 VPN 门禁。
- **免费判定**：无目录计费字段。免费模型为公开的 `gemini-*-flash` 档位与 `*-latest` 自动跟随别名。
  通过对已知 flash 集 + 任何新的 `gemini-<ver>-flash` / `gemini-*-latest` 别名做实测来发现。
- **已知免费（已注册 8 个）**：代表性 id —— `gemini-3.1-flash-lite`、
  `gemini-3.5-flash`、`gemini-3.7-flash`、`gemini-3-flash-preview`、`gemini-flash-latest`、
  `gemini-flash-lite-latest`（另有两种 flash 变体）。确切当前集合以实时 `models.json` 为准——
  不要在这些模式之外硬编码。
- **能力**：flash-vision 档位 `supportsImages: true`；`supportsReasoning: false`
  （Gemini flash 不输出 `reasoning_content`）。
- **注意**：(1) `/v1beta/openai/models` 返回 **400**——OpenAI 兼容端点不支持模型*枚举*，故 `catalog`
  无法列出 Google 模型；改用已知 flash 集 + 活体 `test` 发现。(2) 即使走代理，某些网络仍地域封锁
  （`400` "User location not supported"）——这是**地域产物；绝不可据此移除模型**；保留并在可接受的
  网络区域验证。(3) 沙箱可能拦截 `googleapis`；改用沙箱绕过或系统代理重试。

## 2. NVIDIA NIM

- **端点**：`https://integrate.api.nvidia.com/v1`
- **海外**：是（受限网络下经代理走）。
- **免费判定**：目录（`/v1/models`，约 84 个模型）**不含计费字段**。通过**活体对话补全测试**判定：
  - `200` + 真实内容 → 免费 / 可用，**新增**。
  - `402` / `403` → 无免费额度 / 付费，**排除**。
  - `404` → 已列出但该免费端点未部署，**排除**。
  - `000`（连接重置）→ 网络/VPN 产物，经代理重试；不做判定。
- **已知免费（已注册）**：`nvidia/nemotron-3-ultra-550b-a55b`（推理）、
  `nvidia/nemotron-3-nano-30b-a3b`、`nvidia/nemotron-3.5-lightning-30b-a3b` 等。
- **能力**：按模型设定；推理变体会输出 `reasoning_content`（`supportsReasoning: true`）。
- **注意**：`kimi-k2.6`、`llama-3.1-nemotron-ultra-253b-v1` 返回 `404`（账户未部署）；
  部分「前沿」模型（`mistral-nemotron`、`deepseek-v4-pro-*`）反复 `000`/不可用——视为非免费，跳过。

## 3. SenseNova（商汤）

- **端点**：`https://token.sensenova.cn/v1/chat/completions`
- **海外**：否。
- **免费判定**：对 `GET https://token.sensenova.cn/v1/models` 返回的模型，当且仅当**所有计费值均为
  `"0"`** 时为免费。对**未出现在目录中**的模型（见目录说明，如 `kimi-k3` / `deepseek-v4-pro`），
  依官方 Token Plan 公告（0 元公测）+ 活体对话测试（200 + 内容 = 免费）判定。
- **目录**：`/v1/models` 端点仅返回 **6 个「经典」模型**（4 个对话 + 2 个图像生成 `u1-fast` /
  `u1.5-lite`）。⚠️ **Token Plan 可能暴露不在 `/v1/models` 返回的额外对话模型**——例如截至 2026-08-28，
  `kimi-k3` 与 `deepseek-v4-pro` 可通过 `token.sensenova.cn/v1/chat/completions` 调用
  （0 元公测）但未出现在目录中。这类模型应直接对文档给出的模型 id 做对话 `test` 来发现，**不要**靠目录枚举。
- **排除**：图像生成模型**不兼容对话补全 → 跳过**（与其他厂商非对话接口规则一致）。
- **能力**：对话模型的 `supportsImages` 因模型而异；取自目录的 `input_modalities` / `output_modalities`。

## 4. BigModel（智谱 GLM）

- **端点**：`https://open.bigmodel.cn/api/paas/v4`
- **海外**：否。
- **免费判定**：以官方计费文档为准。免费 flash 档位：
  `glm-4.7-flash`、`glm-4.6v-flash`（多模态/视觉）、`glm-4-flash-250414`、
  `glm-z1-flash`（推理）、`glm-5.3-flash`、`glm-4.5-flash`。
- **付费 / 排除**：`glm-5.3`（旗舰，付费——此处 `200` **仍会扣费**，勿添加）。`glm-4.6-flash` 返回
  `403`「无权访问」（跳过）。`glm-5.2-flash` / `glm-5.1-flash` / `glm-5-flash` 返回 `400`（不存在，跳过）。
- **能力**：`glm-4.6v-flash` → `supportsImages: true`；`glm-z1-flash`、`glm-5.3-flash`、
  `glm-4.5-flash` → `supportsReasoning: true`。
- **注意**：`429` = 限流，模型仍有效（保留）。

## 5. Agnes

- **端点**：`https://api.agnes-ai.cn/v1`
- **海外**：否。
- **免费判定**：`GET https://api.agnes-ai.cn/v1/models` 列出候选；以活体对话补全测试
  （`200` + 内容 = 免费）确认。
- **已知免费（已注册）**：`agnes-2.0-flash`、`agnes-2.5-pro`、`agnes-2.5-pro-alpha`，以及其它 flash 变体。
- **排除**：`agnes-2.5-pro-beta` **无 OpenAI 端点**（跳过）；图像/视频模型为非对话（跳过）。
- **能力**：flash → `supportsReasoning: false`；pro → 按响应而定。

## 6. SiliconFlow（硅基流动）

- **端点**：`https://api.siliconflow.cn/v1`
- **海外**：否（国内）。
- **免费判定 — 特殊情况 ⚠️**：`/v1/models` **无计费字段**；**无余额查询端点**；且**新账户会获赠欢迎额度**，
  因此付费模型也返回 `200`。故此处 **`200` 不能证明免费**。是否免费**只能**依据 SiliconFlow 官方「免费」标记：
  - 计费页（`siliconflow.cn/pricing`）将某模型标记为「免费」。
  - 社区 `free-model.com` 的 SiliconFlow 免费清单。
  - 已验证的「X 系列免费」公告（如「Qwen3 系列免费」）。
  活体测试**仅用于确认可达性 + 内容**，绝不据此推断免费状态。
- **已知免费对话/视觉（已注册 11 个）**：`deepseek-ai/DeepSeek-R1-0528-Qwen3-8B`（推理）、
  `Qwen/Qwen3-8B`、`Qwen/Qwen3-14B`、`Qwen/Qwen3-32B`、`Qwen/Qwen3-30B-A3B-Instruct-2507`、
  `Qwen/Qwen2.5-7B-Instruct`、`THUDM/GLM-Z1-9B-0414`（推理）、`THUDM/GLM-4-9B-0414`、
  `tencent/Hunyuan-MT-7B`（翻译）、`deepseek-ai/DeepSeek-OCR`（视觉）、
  `PaddlePaddle/PaddleOCR-VL-1.5`（视觉）。
- **待定 — 需用户复核**：`Qwen3-14B` / `Qwen3-32B` / `Qwen3-30B-A3B` 仅依据「Qwen3 系列免费」来源添加；
  在报告中标注，请于控制台确认。
- **排除（非对话）**：`BAAI/bge-*`（embedding/reranker）、`Qwen3-Embedding/Reranker`、`Qwen-Image`、
  `Kolors`、`Wan`、`CosyVoice`、`SenseVoice`（图像/语音）——不兼容对话 schema，即便免费也跳过。
- **排除（付费/前沿）**：`DeepSeek-V4-Flash/Pro`、`LongCat-2.0`、`GLM-5.2`、`Kimi-K2.7-Code`、
  `MiniMax-M2.5`、`Qwen3.5*/Qwen3.6*`、`Step-3.5-Flash`、`Seed-OSS-36B`（计费，需充值）→ 跳过。

## 跨厂商通用规则

- **始终排除非对话接口**：embedding / reranker / image-generation / ASR / TTS。
- **`429` 保留**（限流，仍有效）。
- **`000` 绝不移除**（网络/VPN 产物）。
- **推理模型**：活体测试分配 `max_tokens ≥ 80`，否则输出空白。
- **新增同厂商模型时**，复用注册表中已有条目的厂商 `apiKey`。
