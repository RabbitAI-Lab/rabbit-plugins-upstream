## Description: <br>
Converts a user-confirmed local video into bilingual ASS and SRT subtitles using OkFile upload, Alibaba Fun-ASR word timestamps, and either qwen-mt-plus or the current Agent model for translation review and QA. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aiaaaa4](https://clawhub.ai/user/aiaaaa4) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to turn local recorded videos into bilingual Chinese/source-language ASS and SRT subtitles after confirming the video path, translation mode, output location, and external processing consent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected video audio and subtitle text may be sent to external providers. <br>
Mitigation: Proceed only after explicit external-processing consent; use the fixed OkFile and Alibaba endpoints or the selected current Agent model, and review provider retention policies for sensitive videos. <br>
Risk: Alibaba and OkFile credentials are required for the workflow. <br>
Mitigation: Keep API keys in the local .env file and do not paste them into chat. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aiaaaa4/skills/video-translate) <br>
- [Video Translation Execution Contract](references/execution-contract.md) <br>
- [Screen Context Rules](references/screen_context.md) <br>
- [ASR Hotwords - English Trading Videos](references/asr_hotwords_en.md) <br>
- [Trading Translation Glossary](references/trading_glossary.md) <br>
- [Term Repair Rules](references/term_repair_rules.json) <br>
- [OkFile API keys](https://www.okfile.com/en/account/api-keys) <br>
- [Alibaba Model Studio API key](https://help.aliyun.com/zh/model-studio/get-api-key) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance and shell commands; final subtitle artifacts are ASS and SRT files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces one bilingual ASS file and one bilingual SRT file after source analysis, translation review, deterministic QA, and final whole-document QC pass.] <br>

## Skill Version(s): <br>
1.5.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
