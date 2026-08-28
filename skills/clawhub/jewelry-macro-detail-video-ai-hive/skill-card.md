## Description:

This skill helps jewelry, ecommerce, advertising, and content teams turn jewelry macro-video requests into production briefs, shot plans, prompts, AI-HIVE video tasks, runnable commands, and review checklists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, brand teams, ecommerce operators, and advertising teams use this skill to plan and generate jewelry macro-detail videos with controlled lighting, slow camera motion, material prompts, and acceptance checks. Developers can also use its scripts to create briefs, submit AI-HIVE video jobs, upload authorized media, poll task status, download results, and perform deterministic ffmpeg edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses an AI-HIVE API key that may be stored locally.

Mitigation: Use a scoped key where possible, keep it out of logs and version control, and rely on the script's local config permissions or environment variables.

Risk: Selected images, videos, or audio can be uploaded to AI-HIVE for generation.

Mitigation: Upload only assets the user is authorized to process and avoid sensitive, private, or unlicensed materials.

Risk: Generation tasks may be billable and may run asynchronously.

Mitigation: Review prompts, model choices, routing mode, and price snapshots before submission; use a small sample before batch generation.

Risk: Jewelry material, certificate, weight, grade, or performance claims could be inaccurate if supplied facts are incomplete.

Mitigation: Mark uncertain claims for human verification and do not treat model output as a substitute for product records, platform data, legal review, or professional gemological assessment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/jewelry-macro-detail-video-ai-hive)
- [ClawHub publisher profile](https://clawhub.ai/user/wubin1836)
- [AI-HIVE chat and API access](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON task records, production checklists, and generated local media files when AI-HIVE tasks are run.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload user-selected reference media to AI-HIVE, poll asynchronous generation tasks, and download resulting videos or images.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
