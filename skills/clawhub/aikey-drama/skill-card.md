## Description:

AI KEY·短剧编剧 helps creators turn a premise or rough idea into a vertical short-drama script, either as a standalone 1-3 minute episode or a paid-series development pack, with optional shot lists and Seedance-ready video prompts after cost confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and small production teams use this skill to develop Chinese vertical short-drama scripts, paid-series outlines, and optional AI-video prompt handoffs from a premise or rough idea.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill expects broader AI KEY configuration and reference files; missing inputs can weaken its compliance and workflow safeguards.

Mitigation: Install the required AI KEY config and references before use; the skill is designed to stop and report missing required files instead of proceeding from memory.

Risk: The workflow may read or write configured memory and draft locations.

Mitigation: Review configured draft and memory paths before running the skill in a shared or sensitive workspace.

Risk: Optional video-generation handoff can incur paid usage.

Mitigation: Confirm the number of images or video clips, durations, and selected model before submitting generation work.

Risk: Generated scripts and AI-video outputs may still require originality, platform-rule, filing, or AI-labeling review before publication.

Mitigation: Review scripts and generated media against current platform rules and local publication requirements before release.

## Reference(s):

- [AI KEY·短剧编剧 on ClawHub](https://clawhub.ai/iamzifei/skills/aikey-drama)
- [剧本格式](artifact/references/剧本格式.md)
- [编剧方法卡](artifact/references/编剧方法卡.md)
- [合规与原创红线](artifact/references/合规与原创红线.md)
- [分镜与生成提示词](artifact/references/分镜与生成提示词.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown scripts, outline tables, checklists, and video prompt text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose configured draft or memory file writes and optional paid video-generation handoff only after user confirmation.]

## Skill Version(s):

0.2.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
