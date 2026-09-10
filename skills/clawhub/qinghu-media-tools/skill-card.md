## Description:

This skill helps agents route Qinghu AI qhkit video and image workflows for ecommerce media optimization, including watermark or subtitle removal, video super-resolution, background edits, object removal, text edits, compression, and watermarking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to prepare ecommerce video and image assets through qhkit, including cleanup, super-resolution, background editing, compression, and branded watermarking. It also guides setup, credential configuration, estimates, polling, and delivery of generated media outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or execute mutable third-party CLI code through npm, latest-version upgrades, or npx.

Mitigation: Review the package before use, prefer a pinned or locally reviewed qhkit version, and run it in an environment with appropriate least-privilege controls.

Risk: The skill can upload local image or video files to Qinghu/qhkit services for processing.

Mitigation: Use only media you are allowed to upload, avoid confidential or regulated files unless provider handling terms have been reviewed, and confirm upload intent for sensitive workflows.

Risk: Watermark or subtitle removal can create copyright, licensing, or marketplace policy issues when used on third-party media.

Mitigation: Use removal workflows only for owned or authorized media and remind users to confirm rights before commercial reuse.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-media-tools)
- [AutoAGC publisher profile](https://clawhub.ai/user/autoagc)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON CLI parameters, task identifiers, and media result URLs when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit status JSON, credit estimates, generated image or video URLs, and setup or troubleshooting guidance.]

## Skill Version(s):

0.1.0 (source: server evidence release.version and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
