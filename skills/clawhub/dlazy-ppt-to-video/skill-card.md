## Description:

Converts PPT, PowerPoint, Keynote, and related presentation documents into explainer, pitch, courseware, or training videos by using the dLazy hosted file-to-video workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use this skill when they have presentation or document files and want dLazy to produce a narrated video workflow for explainers, pitches, courseware, reports, or training material.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local documents may be sent to dLazy's hosted API and media storage.

Mitigation: Use the skill only for documents approved for dLazy processing, and avoid confidential decks or regulated data unless the organization's data-handling review approves the service.

Risk: The dLazy API key can be saved in the local CLI configuration.

Mitigation: Prefer DLAZY_API_KEY for per-invocation use when persistence is not needed, protect the config file, and rotate or revoke organization keys when access changes.

Risk: The security verdict is suspicious because the skill combines hosted uploads, local credential storage, and an overconfident permissions claim.

Mitigation: Review the dLazy CLI, install the pinned package version, and confirm expected network behavior before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ppt-to-video)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI homepage from metadata](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and terminal-oriented text with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference generated project ids, uploaded file URLs, authentication state, and hosted dLazy task results.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
