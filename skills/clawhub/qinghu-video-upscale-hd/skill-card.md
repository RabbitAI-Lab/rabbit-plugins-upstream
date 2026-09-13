## Description:

This skill helps agents use Qinghu AI and LinkPix to upscale short product videos, improve clarity, add frame interpolation, and keep audio synchronized.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to quote, submit, monitor, and deliver enhanced product videos through the Qinghu AI video upscale workflow. It is intended for authorized videos that need higher resolution, smoother motion, and clearer presentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may require installing or upgrading the mutable global @iqinghu/qhkit CLI.

Mitigation: Install only from trusted package sources, confirm upgrades before running them, and prefer a reviewed version when possible.

Risk: Using the skill uploads selected videos to an external Qinghu service and depends on a user token.

Mitigation: Use only owned or authorized media, protect the Qinghu token, and confirm the service is acceptable for the video's content.

Risk: Paid generation can consume Qinghu credits.

Mitigation: Run an estimate first, report the quoted credits and balance status, and wait for user confirmation before submitting a paid generation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/qinghu-video-upscale-hd)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API Keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces qhkit workflow commands, pricing and polling guidance, and final video delivery guidance.]

## Skill Version(s):

0.1.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
