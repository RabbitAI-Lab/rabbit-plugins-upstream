## Description:

Turns PowerPoint, Word, Excel, PDF, and other documents into narrated explainer, training, or report videos through a project-based workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, educators, and business teams use this skill to turn supplied documents into narrated explainer, courseware, report, or training videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached documents are sent to an external dLazy service.

Mitigation: Only submit documents you are authorized to share with dLazy.

Risk: The CLI saves a dLazy API key locally.

Mitigation: Protect the local key and rotate or revoke it in the dLazy dashboard when access should end.

Risk: A global CLI installation persists on the user's system.

Mitigation: Use the pinned npx command when a persistent global binary is not desired.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-file-to-video)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI homepage (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Video links, Guidance]

**Output Format:** [Streaming text responses with links to generated video assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports project-based follow-up conversations.]

## Skill Version(s):

1.3.23 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
