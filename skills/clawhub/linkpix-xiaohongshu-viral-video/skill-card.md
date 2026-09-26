## Description:

Generates Xiaohongshu-ready short commerce videos through LinkPix and qhkit, using supported video models for product notes, review clips, lifestyle demos, image-to-video, and traffic-driving campaign assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, e-commerce operators, buyers, and social marketing teams use this skill to prepare Xiaohongshu product seeding and sales videos. It guides model selection, asset upload, credit estimation, task polling, and delivery through qhkit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys could be exposed if pasted into chat.

Mitigation: Use a managed secret or local environment variable for qhkit credentials whenever possible.

Risk: Runtime installation can install npm packages, Node binaries, or image tooling and may modify the local user environment.

Mitigation: Install only in a trusted environment and review package sources before running setup commands.

Risk: Video generation can consume account credits and submitted tasks may not be cancellable.

Mitigation: Estimate credits and obtain explicit user confirmation before running generation commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-xiaohongshu-viral-video)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys console](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)
- [Qinghu API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local image paths, selected model labels, video duration, orientation, language, task IDs, credits, and output video URLs.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
