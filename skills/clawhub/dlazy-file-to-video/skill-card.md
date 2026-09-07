## Description:

Converts PPT, Word, Excel, PDF, and other documents into explainer, report, courseware, or training videos through the dLazy file-to-video workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use this skill to start or continue dLazy file-to-video projects that turn documents into explainer, report, courseware, or training videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party npm CLI and a dLazy API key.

Mitigation: Review the dLazy CLI source or package before installing in sensitive environments, prefer the pinned npx invocation when practical, avoid administrator privileges, and rotate or revoke API keys when needed.

Risk: Files attached to a session are uploaded to dLazy's hosted service.

Mitigation: Only upload documents that are appropriate for processing by dLazy and follow organizational data-handling rules.

Risk: Workflow execution can fail when authentication, account balance, or hosted service availability is insufficient.

Mitigation: Confirm the API key, credits, and service access before relying on the skill for time-sensitive work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-file-to-video)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and streamed CLI responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and may upload user-selected files to dLazy's hosted service for processing.]

## Skill Version(s):

1.3.12 (source: release evidence, released 2026-09-07; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
