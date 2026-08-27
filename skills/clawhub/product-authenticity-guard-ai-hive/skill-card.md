## Description:

商品真实性守门员｜AI-HIVE helps e-commerce and content teams compare real product references with generated or edited assets, identify differences in structure, color, packaging, accessories, function, and usage scenes, and guide authorized AI-HIVE remediation workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce teams, merchants, content generation teams, and product reviewers use this skill to compare product references against generated or edited commerce assets and produce authenticity-focused difference reports. It also guides authorized AI-HIVE image and video generation workflows when new remediation assets are needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated media and uploaded references are externally processed through AI-HIVE workflows.

Mitigation: Use only files the user is authorized to upload and confirm parameters before starting any billable image or video task.

Risk: The skill can support product authenticity review, but it is not a legal, compliance, or physical inspection authority.

Mitigation: Mark uncertain differences for human review and keep final decisions with qualified reviewers for regulated, legal, brand, or safety-sensitive claims.

Risk: API keys may be exposed if copied into scripts, logs, screenshots, or repositories.

Mitigation: Use environment variables or the local AI-HIVE config file, keep placeholder keys in examples, and remove secrets from shared artifacts.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/wubin1836/skills/product-authenticity-guard-ai-hive)
- [AI-HIVE product entry](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown with structured sections, inline bash code blocks, and optional JSON or media file paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local blueprint JSON and download generated image or video files when the user authorizes AI-HIVE API calls.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
