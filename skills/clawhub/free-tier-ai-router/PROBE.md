# PROBE.md — raw evidence behind every claim in SKILL.md

All probes ran 2026-07-30 against live APIs with real completions.

## Live probe: 74/113 models answered

| provider | model | http | sec |
|---|---|---|---|
| gemini | `gemini-3-flash-preview` | 200 | 1.05 |
| gemini | `gemini-3.1-flash-lite` | 200 | 0.63 |
| gemini | `gemini-3.1-flash-lite-preview` | 200 | 0.55 |
| gemini | `gemini-3.5-flash` | 200 | 5.0 |
| gemini | `gemini-3.5-flash-lite` | 200 | 0.54 |
| gemini | `gemini-3.6-flash` | 200 | 1.47 |
| gemini | `gemini-flash-latest` | 200 | 1.24 |
| gemini | `gemini-flash-lite-latest` | 200 | 0.63 |
| gemini | `gemini-robotics-er-1.6-preview` | 200 | 1.51 |
| gemini | `gemma-4-26b-a4b-it` | 200 | 1.59 |
| gemini | `gemma-4-31b-it` | 200 | 1.94 |
| kilo | `cohere/north-mini-code:free` | 200 | 2.68 |
| kilo | `inclusionai/ling-3.0-flash:free` | 200 | 1.35 |
| kilo | `kilo-auto/free` | 200 | 1.35 |
| kilo | `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | 200 | 1.9 |
| kilo | `nvidia/nemotron-3-super-120b-a12b:free` | 200 | 1.44 |
| kilo | `nvidia/nemotron-3-ultra-550b-a55b:free` | 200 | 6.17 |
| kilo | `nvidia/nemotron-3.5-content-safety:free` | 200 | 2.44 |
| kilo | `openrouter/free` | 200 | 8.49 |
| kilo | `poolside/laguna-s-2.1:free` | 200 | 0.9 |
| kilo | `poolside/laguna-xs-2.1:free` | 200 | 2.7 |
| kilo | `stepfun/step-3.7-flash:free` | 200 | 5.96 |
| mistral | `codestral-2508` | 200 | 0.34 |
| mistral | `codestral-latest` | 200 | 0.3 |
| mistral | `devstral-2512` | 200 | 0.33 |
| mistral | `devstral-latest` | 200 | 0.38 |
| mistral | `devstral-medium-latest` | 200 | 0.39 |
| mistral | `magistral-medium-2509` | 200 | 1.89 |
| mistral | `magistral-medium-latest` | 200 | 2.96 |
| mistral | `magistral-small-2509` | 200 | 0.88 |
| mistral | `magistral-small-latest` | 200 | 0.42 |
| mistral | `ministral-14b-2512` | 200 | 0.41 |
| mistral | `ministral-14b-latest` | 200 | 0.4 |
| mistral | `ministral-3b-2512` | 200 | 0.34 |
| mistral | `ministral-3b-latest` | 200 | 0.34 |
| mistral | `ministral-8b-2512` | 200 | 0.32 |
| mistral | `ministral-8b-latest` | 200 | 0.32 |
| mistral | `mistral-code-agent-latest` | 200 | 0.51 |
| mistral | `mistral-code-fim-latest` | 200 | 0.31 |
| mistral | `mistral-code-latest` | 200 | 0.34 |
| mistral | `mistral-large-2512` | 200 | 0.53 |
| mistral | `mistral-large-latest` | 200 | 0.53 |
| mistral | `mistral-medium` | 200 | 0.36 |
| mistral | `mistral-medium-2505` | 200 | 0.39 |
| mistral | `mistral-medium-2508` | 200 | 0.37 |
| mistral | `mistral-medium-2604` | 200 | 0.39 |
| mistral | `mistral-medium-3` | 200 | 0.4 |
| mistral | `mistral-medium-3-5` | 200 | 0.7 |
| mistral | `mistral-medium-3.5` | 200 | 0.38 |
| mistral | `mistral-medium-latest` | 200 | 0.35 |
| mistral | `mistral-small-2506` | 200 | 0.39 |
| mistral | `mistral-small-2603` | 200 | 0.41 |
| mistral | `mistral-small-latest` | 200 | 0.37 |
| mistral | `mistral-tiny-2407` | 200 | 0.32 |
| mistral | `mistral-tiny-latest` | 200 | 0.32 |
| mistral | `mistral-vibe-cli-fast` | 200 | 0.42 |
| mistral | `mistral-vibe-cli-latest` | 200 | 0.42 |
| mistral | `mistral-vibe-cli-with-tools` | 200 | 0.37 |
| mistral | `open-mistral-nemo` | 200 | 0.33 |
| mistral | `open-mistral-nemo-2407` | 200 | 0.37 |
| mistral | `voxtral-small-2507` | 200 | 0.34 |
| mistral | `voxtral-small-latest` | 200 | 0.38 |
| openrouter | `cohere/north-mini-code:free` | 200 | 4.93 |
| openrouter | `inclusionai/ling-3.0-flash:free` | 200 | 1.24 |
| openrouter | `nvidia/nemotron-3-nano-30b-a3b:free` | 200 | 0.45 |
| openrouter | `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | 200 | 1.21 |
| openrouter | `nvidia/nemotron-3-super-120b-a12b:free` | 200 | 1.01 |
| openrouter | `nvidia/nemotron-3-ultra-550b-a55b:free` | 200 | 0.68 |
| openrouter | `nvidia/nemotron-3.5-content-safety:free` | 200 | 1.81 |
| openrouter | `nvidia/nemotron-nano-12b-v2-vl:free` | 200 | 3.63 |
| openrouter | `nvidia/nemotron-nano-9b-v2:free` | 200 | 2.63 |
| openrouter | `openai/gpt-oss-20b:free` | 200 | 3.15 |
| openrouter | `poolside/laguna-s-2.1:free` | 200 | 1.72 |
| openrouter | `poolside/laguna-xs-2.1:free` | 200 | 1.58 |

## Failures

| provider | model | http | reason |
|---|---|---|---|
| cerebras | `gemma-4-31b` | 402 | Payment required to access this resource. Visit your billing tab. |
| cerebras | `gpt-oss-120b` | 402 | Payment required to access this resource. Visit your billing tab. |
| cerebras | `zai-glm-4.7` | 402 | Payment required to access this resource. Visit your billing tab. |
| gemini | `antigravity-preview-05-2026` | 400 | This model only supports Interactions API. |
| gemini | `deep-research-max-preview-04-2026` | 400 | This model only supports Interactions API. |
| gemini | `deep-research-preview-04-2026` | 400 | This model only supports Interactions API. |
| gemini | `deep-research-pro-preview-12-2025` | 400 | This model only supports Interactions API. |
| gemini | `gemini-2.0-flash` | 429 | You exceeded your current quota, please check your plan and billing de |
| gemini | `gemini-2.0-flash-001` | 429 | You exceeded your current quota, please check your plan and billing de |
| gemini | `gemini-2.0-flash-lite` | 429 | You exceeded your current quota, please check your plan and billing de |
| gemini | `gemini-2.0-flash-lite-001` | 429 | You exceeded your current quota, please check your plan and billing de |
| gemini | `gemini-2.5-computer-use-preview-10-2025` | 429 | You exceeded your current quota, please check your plan and billing de |
| gemini | `gemini-2.5-flash` | 404 | This model models/gemini-2.5-flash is no longer available to new users |
| gemini | `gemini-2.5-flash-image` | 429 | You exceeded your current quota, please check your plan and billing de |
| gemini | `gemini-2.5-flash-lite` | 404 | This model models/gemini-2.5-flash-lite is no longer available to new  |
| gemini | `gemini-2.5-flash-preview-tts` | 400 | The requested combination of response modalities (TEXT) is not support |
| gemini | `gemini-2.5-pro` | 429 | You exceeded your current quota, please check your plan and billing de |
| gemini | `gemini-2.5-pro-preview-tts` | 429 | You exceeded your current quota, please check your plan and billing de |
| gemini | `gemini-3-pro-image` | 429 | You exceeded your current quota, please check your plan and billing de |
| gemini | `gemini-3-pro-image-preview` | 429 | You exceeded your current quota, please check your plan and billing de |
| gemini | `gemini-3-pro-preview` | 429 | You exceeded your current quota, please check your plan and billing de |
| gemini | `gemini-3.1-flash-image` | 429 | You exceeded your current quota, please check your plan and billing de |
| gemini | `gemini-3.1-flash-image-preview` | 429 | You exceeded your current quota, please check your plan and billing de |
| gemini | `gemini-3.1-flash-lite-image` | 429 | You exceeded your current quota, please check your plan and billing de |
| gemini | `gemini-3.1-flash-tts-preview` | 400 | Request contains an invalid argument. |
| gemini | `gemini-3.1-pro-preview` | 429 | You exceeded your current quota, please check your plan and billing de |
| gemini | `gemini-3.1-pro-preview-customtools` | 429 | You exceeded your current quota, please check your plan and billing de |
| gemini | `gemini-omni-flash-preview` | 429 | You exceeded your current quota, please check your plan and billing de |
| gemini | `gemini-pro-latest` | 429 | You exceeded your current quota, please check your plan and billing de |
| gemini | `gemini-robotics-er-1.5-preview` | 404 | This model models/gemini-robotics-er-1.5-preview is no longer availabl |
| gemini | `lyria-3-clip-preview` | 429 | You exceeded your current quota, please check your plan and billing de |
| gemini | `lyria-3-pro-preview` | 429 | You exceeded your current quota, please check your plan and billing de |
| gemini | `nano-banana-pro-preview` | 429 | You exceeded your current quota, please check your plan and billing de |
| kilo | `google/lyria-3-clip-preview` | 402 | Add credits to continue, or switch to a free model |
| kilo | `google/lyria-3-pro-preview` | 402 | Add credits to continue, or switch to a free model |
| mistral | `labs-leanstral-1-5` | 403 | Model labs-leanstral-1-5 is a Labs model. To use Labs models, an admin |
| mistral | `labs-leanstral-1-5-1` | 403 | Model labs-leanstral-1-5-1 is a Labs model. To use Labs models, an adm |
| openrouter | `google/gemma-4-26b-a4b-it:free` | 200 | Internal Server Error |
| openrouter | `google/gemma-4-31b-it:free` | 429 | Provider returned error |

## Quality: 5 objective questions

| score | sec | provider | model |
|---|---|---|---|
| 5/5 | 0.43 | mistral | `mistral-medium-latest` |
| 5/5 | 0.63 | gemini | `gemini-3.1-flash-lite` |
| 5/5 | 0.66 | gemini | `gemini-3.5-flash-lite` |
| 5/5 | 0.93 | openrouter | `inclusionai/ling-3.0-flash:free` |
| 5/5 | 1.46 | kilo | `kilo-auto/free` |
| 5/5 | 1.5 | gemini | `gemini-3-flash-preview` |
| 5/5 | 1.53 | gemini | `gemini-3.5-flash` |
| 5/5 | 2.3 | kilo | `nvidia/nemotron-3-ultra-550b-a55b:free` |
| 5/5 | 2.77 | openrouter | `nvidia/nemotron-3-super-120b-a12b:free` |
| 5/5 | 3.41 | kilo | `stepfun/step-3.7-flash:free` |
| 4/5 | 0.45 | mistral | `mistral-small-latest` |
| 4/5 | 0.46 | mistral | `mistral-large-latest` |
| 4/5 | 0.49 | mistral | `ministral-3b-latest` |
| 4/5 | 0.68 | mistral | `open-mistral-nemo` |
| 4/5 | 0.72 | mistral | `mistral-tiny-latest` |
| 4/5 | 1.22 | mistral | `ministral-8b-latest` |
| 4/5 | 1.4 | openrouter | `nvidia/nemotron-3-ultra-550b-a55b:free` |
| 4/5 | 4.81 | mistral | `magistral-medium-latest` |
| 4/5 | 5.89 | kilo | `openrouter/free` |
| 3/5 | 0.59 | mistral | `codestral-latest` |
| 2/5 | 0.85 | openrouter | `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` |
| 1/5 | 0.48 | openrouter | `poolside/laguna-s-2.1:free` |
| 1/5 | 0.88 | openrouter | `openai/gpt-oss-20b:free` |
| 0/5 | 0.23 | gemini | `gemini-3.6-flash` |
| 0/5 | 0.25 | gemini | `gemini-flash-latest` |
| 0/5 | 0.58 | kilo | `cohere/north-mini-code:free` |

Reproduce: `python3 probe.py && python3 quality.py && python3 ratelimit.py`