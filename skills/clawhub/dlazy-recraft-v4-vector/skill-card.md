## Description:

Text-to-vector model that outputs SVG results for logos, icons, and scalable design assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to invoke dLazy's Recraft V4 Vector generation workflow for logo, icon, and scalable design asset creation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the global npm CLI adds a persistent executable to the user's environment.

Mitigation: Review the linked dLazy CLI source or npm package before installing, and use the pinned npx invocation when a non-persistent install is preferred.

Risk: Prompts and selected local file paths are sent to the hosted dLazy service during generation.

Mitigation: Avoid submitting sensitive prompts or files unless the user has approved sending that data to dLazy.

Risk: Workflows that require true SVG/vector output may be affected if the returned asset type differs from expectations.

Mitigation: Verify the generated asset's MIME type and file format before using it in downstream vector-only workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-vector)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON, files]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return hosted generated asset URLs, asynchronous task identifiers, or saved local result files depending on CLI flags.]

## Skill Version(s):

1.3.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
