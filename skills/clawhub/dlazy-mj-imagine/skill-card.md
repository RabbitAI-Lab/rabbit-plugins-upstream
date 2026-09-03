## Description:

Generates Midjourney-style images through the dLazy CLI, supporting aspect ratio, bot type, and grid or U1-U4 output selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to request stylized image generation from dLazy's hosted service from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and explicitly supplied media files are sent to dLazy's hosted API and media storage.

Mitigation: Use the skill only with data appropriate for dLazy's service and avoid submitting confidential media unless approved.

Risk: The dLazy API key may be stored locally in the user's CLI configuration.

Mitigation: Keep local CLI configuration user-restricted, prefer per-invocation DLAZY_API_KEY where appropriate, and rotate or revoke keys from the dLazy dashboard if exposure is suspected.

Risk: The skill depends on a third-party CLI and hosted service.

Mitigation: Use the pinned npx @dlazy/cli@1.2.3 path if a persistent global binary is not desired, and review the dLazy CLI package before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-mj-imagine)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted image URLs, downloaded image files when --save is used, or asynchronous task identifiers when --no-wait is used.]

## Skill Version(s):

1.3.10 (source: server release metadata; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
