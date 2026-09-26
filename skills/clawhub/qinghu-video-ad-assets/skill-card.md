## Description:

Generates Qinghu/QHKIT e-commerce video ad assets from product information for feed ads, brand promotion, social media marketing, and batch creative production.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External advertisers, marketers, and agent operators use this skill to prepare Qinghu/QHKIT commands for generating multiple e-commerce video ad creatives, estimating cost, polling job status, and returning completed video URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or upgrading the qhkit npm package changes the local execution environment.

Mitigation: Ask for user approval before npm install or upgrade steps and report installation failures without continuing blindly.

Risk: QHKIT token setup can expose credentials to the wrong tool or service.

Mitigation: Use the token only for the intended QHKIT CLI or environment variable and avoid echoing secrets in responses or logs.

Risk: Local product images or media paths may be uploaded during video generation.

Mitigation: Review the paths or URLs with the user before generation so only intended assets are uploaded.

Risk: Video generation can consume paid credits and submitted tasks may not be cancelable.

Mitigation: Run a matching estimate when supported, disclose expected credits and balance status, and get user approval before submitting a billable generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-video-ad-assets)
- [QHKIT npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with qhkit CLI commands and JSON parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include install or upgrade commands, token configuration guidance, credit estimates, submitted task IDs, polling instructions, and completed video URLs.]

## Skill Version(s):

0.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
