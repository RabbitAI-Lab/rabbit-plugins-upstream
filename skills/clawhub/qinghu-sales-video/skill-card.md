## Description:

Uploads product media through qhkit to generate short ecommerce sales videos with AI scripts, voiceover, subtitles, and transitions for platforms such as TikTok and Douyin.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, marketers, and their agents use this skill to turn product images, selling points, and optional reference videos into short sales or product showcase videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images or videos selected for generation are uploaded to Qinghu's third-party service.

Mitigation: Review and approve the exact media files before upload, and avoid using sensitive, confidential, or unlicensed assets.

Risk: The skill may install or upgrade the qhkit CLI globally, which can change behavior between runs.

Mitigation: Use a pinned, isolated qhkit installation and require approval before installing or upgrading the CLI.

Risk: The workflow requires a qhkit account token.

Mitigation: Store the token in approved secret storage or environment variables, and avoid pasting it into transcripts or shell commands that may be logged.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-sales-video)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit task IDs, credit estimates, polling status, and completed video URLs.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
