## Description:

Generates short e-commerce product videos from product images and selling points, with scripts, voiceover, captions, and transitions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and marketers use this skill to turn product photos and selling points into short promotional videos for platforms such as TikTok and Douyin.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic installation or upgrade of unpinned Node/npm tooling can change the user's environment and run external packages.

Mitigation: Prefer a preinstalled, pinned qhkit version in a controlled environment and review installation or upgrades before execution.

Risk: Token configuration and media upload can expose credentials or product assets to an external service.

Mitigation: Confirm token entry and media uploads with the user; avoid sharing secrets in responses.

Risk: Video generation consumes credits and submitted tasks cannot be canceled.

Mitigation: Check available estimates and confirm credit costs and task details before submission.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-sales-video)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with CLI examples, task status, and video URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports task IDs and credit usage when available; completed media is linked by URL.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
