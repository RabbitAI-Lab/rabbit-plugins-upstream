## Description:

Helps an agent generate cinematic LinkPix product advertising videos by preparing precise prompts, qhkit video commands, cost estimates, task polling, and delivery guidance for brand films and TVC-style product videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content operators use this skill to create high-end product advertising videos and brand films through LinkPix/qhkit, including prompt refinement, reference-image handling, estimates, status checks, and final video delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and may upgrade mutable third-party qhkit tooling.

Mitigation: Use an isolated or project-local pinned CLI install and avoid automatic @latest upgrades unless the release is reviewed.

Risk: The workflow requires a production LinkPix/qhkit API token.

Mitigation: Provide the token through a secure secret mechanism or QHKIT_TOKEN rather than pasting it into shared commands.

Risk: The workflow uploads user media to a third-party video service.

Mitigation: Confirm before uploading proprietary, unreleased, personal, or otherwise sensitive media.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-ad-film)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with qhkit shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit video generation parameters, estimate commands, polling instructions, task IDs, video URLs, and credit usage summaries.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
