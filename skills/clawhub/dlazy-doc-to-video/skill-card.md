## Description:

Creates explainer, report, courseware, or training-video workflows from document inputs by routing prompts and attached files through the dLazy hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to start or continue dLazy document-to-video projects from documents such as Word, Markdown, PDF, PPT, and spreadsheet files. It is suited for explainer videos, report broadcasts, courseware, and training content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files may be sent to dLazy hosted services.

Mitigation: Use this skill only with documents that are allowed under the user's organization policy and dLazy service terms.

Risk: Authentication stores a dLazy API key in local CLI configuration unless a per-run environment variable is used.

Mitigation: Prefer npx for on-demand execution when avoiding a persistent global install, and rotate or revoke API keys when access requirements change.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-doc-to-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and service-generated responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload attached local files to dLazy media storage and stream responses from the hosted dLazy service.]

## Skill Version(s):

1.0.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
