## Description: <br>
Converts a user-selected local video into bilingual Chinese/source-language ASS and SRT subtitles after explicit consent for OkFile audio upload, Alibaba Fun-ASR transcription, and qwen-mt-plus or current-Agent text processing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aiaaaa4](https://clawhub.ai/user/aiaaaa4) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to produce quality-controlled bilingual subtitles for local recorded videos such as lectures, training content, interviews, podcasts, market reviews, and screen recordings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected audio and subtitle text may be processed by external services. <br>
Mitigation: Use the skill only for videos the user is allowed to send to OkFile, Alibaba Fun-ASR, and either qwen-mt-plus or the current Agent model service, and require explicit external-processing consent before processing. <br>
Risk: Provider credentials are required for transcription, upload, and optional qwen-mt-plus translation. <br>
Mitigation: Keep DASHSCOPE_API_KEY, ALIYUN_WORKSPACE_ID, and OKFILE_TOKEN in the local .env file only, and do not paste secrets into chat. <br>
Risk: ASR, translation, or alignment mistakes can produce misleading subtitles. <br>
Mitigation: Rely on the workflow's validation and QA gates before export, and review the resulting ASS/SRT files before using them in sensitive settings. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aiaaaa4/skills/video-translate) <br>
- [execution-contract.md](references/execution-contract.md) <br>
- [screen_context.md](references/screen_context.md) <br>
- [asr_hotwords_en.md](references/asr_hotwords_en.md) <br>
- [trading_glossary.md](references/trading_glossary.md) <br>
- [term_repair_rules.json](references/term_repair_rules.json) <br>
- [OkFile API keys](https://www.okfile.com/en/account/api-keys) <br>
- [Alibaba Model Studio API key](https://help.aliyun.com/zh/model-studio/get-api-key) <br>
- [Alibaba Fun-ASR recorded speech recognition API](https://help.aliyun.com/zh/model-studio/fun-asr-recorded-speech-recognition-http-api) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Bilingual ASS and SRT subtitle files with a concise Markdown delivery summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires explicit external-processing consent, local provider credentials, ffmpeg, and validated QA gates before export.] <br>

## Skill Version(s): <br>
1.7.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
