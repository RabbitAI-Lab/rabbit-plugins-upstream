## Description:

Moonshot AI thinking model with text, image, and video understanding, suited to complex analysis, coding, and writing that needs long reasoning chains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and writing-oriented agents use this skill to call the dLazy Kimi K3 hosted model for complex reasoning, code assistance, and long-form generation with optional image or video context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to dLazy's hosted service.

Mitigation: Use the skill only when the user accepts hosted processing by dLazy, and avoid sending sensitive files that should not leave the local environment.

Risk: The dLazy API key may be saved in the local CLI configuration.

Mitigation: Use DLAZY_API_KEY per invocation when persistent local key storage is not desired, and rotate or revoke exposed keys from the dLazy dashboard.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kimi-k3)
- [dLazy CLI source reference](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [JSON response containing generated model output; async mode can return a task identifier.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include hosted output URLs from files.dlazy.com when the hosted service returns generated assets.]

## Skill Version(s):

1.2.6 (source: server release evidence; artifact frontmatter says 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
