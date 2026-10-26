## Description:

Turns documents, topics, or briefs into narrated explainer videos with an outline, storyboard, voiceover, and validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn documents, topics, or briefs into narrated explainer, courseware, or training videos through a project-based workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files are sent to dLazy; local file attachments are uploaded to its media storage.

Mitigation: Only send documents you are comfortable sharing with dLazy, and review attachments before submitting them.

Risk: Login saves an organization API key in the local CLI configuration, and hosted generation may incur costs.

Mitigation: Prefer device-code login, protect the local configuration, check generation costs, and rotate or revoke the key when access is no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-explainer-video)
- [dLazy homepage](https://dlazy.com)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [CLI repository (listed in skill metadata; not server-verified provenance)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands, Files]

**Output Format:** [Text guidance and generated explainer-video project/media outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped sessions; attached local files are uploaded to the provider's media storage before use.]

## Skill Version(s):

1.0.30 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
