## Description:

Helps beauty brands, makeup merchants, creators, and content teams turn authorized portraits, product shade facts, channel requirements, and constraints into AI-HIVE makeup preview plans, prompts, commands, generated image workflows, and review checklists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External beauty brands, cosmetics merchants, creators, and content marketing teams use this skill to plan and optionally generate AI makeup preview assets for ecommerce, advertising, social content, livestream commerce, and promotional workflows. The skill emphasizes authorized inputs, real product shade anchors, AI visual preview labeling, and human review before paid generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorized portraits, product assets, or other reference media may be sent to AI-HIVE during upload or generation.

Mitigation: Use only images and materials the user is authorized to process, confirm rights before upload, and avoid using the skill for unauthorized likeness, brand, copyright, or privacy-sensitive content.

Risk: AI-HIVE generation calls may incur cost, especially for batch jobs or repeated retries.

Mitigation: Review prompts, model, routing mode, parameters, pricing snapshot, and batch size before submission; start with a small sample before scaling.

Risk: Generated makeup previews could be mistaken for verified product effects, skin improvement claims, exact color proof, or user testimony.

Mitigation: Label outputs as AI visual previews, verify factual claims against authoritative product data, and do not present generated results as clinical, legal, platform, or commercial performance proof.

Risk: The AI-HIVE API key may be exposed through local files, logs, screenshots, or committed artifacts.

Mitigation: Prefer environment variables or the local config file, keep config permissions restricted, and do not echo, log, screenshot, or commit real API keys.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/beauty-makeup-preview-ai-hive)
- [AI-HIVE access page](https://ai-hive.iclip.cn/chat)
- [AI-HIVE OpenAPI base endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with runnable shell commands, generated prompt and checklist content, optional JSON task records, and optional downloaded media files from the helper script.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create a blueprint JSON file, upload authorized reference media to AI-HIVE, submit asynchronous generation tasks, poll task status, and download generated image or video files when the user confirms paid generation parameters.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
