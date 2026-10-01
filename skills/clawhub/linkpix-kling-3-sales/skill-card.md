## Description:

Guides agents to use Qinghu qhkit/LinkPix to configure, estimate, submit, poll, and deliver Kling 3.0 ecommerce product videos from product media and selling points.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, short-video teams, brand content teams, and their agents use this skill to turn product images and selling points into paid Qinghu/qhkit video-generation jobs, then poll and deliver the resulting product video links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads selected product media to the Qinghu/qhkit service.

Mitigation: Use only media approved for that external service and avoid submitting confidential or restricted product assets unless the organization permits it.

Risk: Generate commands can consume paid credits and cannot be cancelled after submission.

Mitigation: Confirm model, input files, duration, orientation, and estimated credits with the user before running any generate command.

Risk: The workflow depends on npm-installed qhkit tooling and an API token.

Mitigation: Install from trusted package sources, prefer pinned versions in controlled environments, and handle Qinghu/qhkit tokens as credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-kling-3-sales)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)
- [Qinghu API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit task IDs, estimated or actual credit usage, status results, and generated video URLs.]

## Skill Version(s):

0.1.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
