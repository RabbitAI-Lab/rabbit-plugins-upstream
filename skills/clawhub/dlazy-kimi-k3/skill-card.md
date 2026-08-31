## Description:

Moonshot AI thinking model with text, image, and video understanding, suited to complex analysis, coding, and writing that needs long reasoning chains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, employees, and external users can use this skill to call the dLazy Kimi K3 model for long-form reasoning, multimodal analysis, coding assistance, and writing tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to dLazy's hosted API and media storage.

Mitigation: Send only content that is appropriate for the dLazy service and avoid passing sensitive local media unless approved for that environment.

Risk: The dLazy API key may be persisted in the local CLI configuration.

Mitigation: Protect the local user account, rotate or revoke keys when needed, and prefer environment-variable authentication or npx use on shared machines.

Risk: The skill depends on a pinned third-party CLI package to execute requests.

Mitigation: Use the pinned package version declared by the artifact and review the package or source before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kimi-k3)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, JSON, Guidance]

**Output Format:** [JSON response envelope containing generated outputs or asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports prompt input plus optional image and video references; local media paths passed to the CLI may be uploaded to dLazy-hosted storage.]

## Skill Version(s):

1.2.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
