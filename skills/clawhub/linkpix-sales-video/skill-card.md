## Description:

This skill guides agents through generating ecommerce sales videos from product images, selling points, and optional reference videos with LinkPix/qhkit, including setup, model selection, quoting, polling, and delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn product images, selling points, and optional reference videos into short ecommerce sales videos for platforms such as TikTok and Douyin. It helps the agent choose qhkit video commands, estimate credits, poll generation status, and deliver generated video URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change the development environment by installing executable code from npm.

Mitigation: Review the skill before installing and prefer a pinned, isolated qhkit installation instead of global installs or @latest upgrades.

Risk: Token setup may expose credentials if API tokens are pasted into command-line arguments or shell history.

Mitigation: Use a secure secret mechanism or environment variable for qhkit credentials and avoid placing tokens directly in command invocations.

Risk: Local product images or videos may be uploaded to LinkPix during generation.

Mitigation: Confirm that uploaded media is approved for external processing and does not contain sensitive or restricted content.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/linkpix-sales-video)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command output summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit task IDs, credit estimates, status results, and generated video URLs.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
