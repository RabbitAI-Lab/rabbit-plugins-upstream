## Description:

Helps Chinese-language video production teams inspect AI-generated commerce, advertising, social, and short-drama videos for visible continuity issues, then produce timecoded findings, repair options, and optional AI-HIVE generation or editing commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External video production, commerce, advertising, social media, and short-drama teams use this skill to turn AI video QA requests into continuity checklists, timecoded issue reports, remediation plans, and auditable task records. Developers can also use its scripts to create project briefs, call AI-HIVE media generation APIs, and perform deterministic ffmpeg video edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE image or video generation helpers may submit paid tasks.

Mitigation: Review prompts, model mode, routing, and price snapshot before execution; start with a small sample before batch generation.

Risk: Media uploads and generated outputs can involve copyrighted, branded, personal, or otherwise restricted material.

Mitigation: Use only authorized source media and keep human review for brand, legal, privacy, regulated-product, and real-person claims.

Risk: Continuity findings can overstate what was actually observed in available frames or task records.

Mitigation: Mark unobserved frames and uncertain facts as unverified, include timestamps or screenshots for each finding, and require manual frame-level review for high-risk ads or long-form content.

Risk: API keys may be exposed if copied into scripts, logs, screenshots, or repositories.

Mitigation: Keep AI_HIVE_API_KEY in environment variables or local config only, avoid echoing secrets, and review logs before sharing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-video-continuity-check-ai-hive)
- [AI-HIVE chat entry](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with timecoded QA findings, checklists, prompts, JSON task records, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local media paths, AI-HIVE task IDs, pricing snapshots, routing mode, model selection, and downloaded output locations when generation helpers are used.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
