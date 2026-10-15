## Description:

Helps agents generate videos from text prompts, reference media, or first and last frames using Tongyi Wanxiang 2.7 through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request video generation from text, reference images or videos, and first and last frames through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and provided media may be sent to dLazy's hosted service.

Mitigation: Only submit content you are authorized to share with the service.

Risk: Generation may consume dLazy credits.

Mitigation: Check expected cost with the CLI's dry-run option before submitting.

Risk: Authentication may save an API key locally.

Mitigation: Protect the local key and rotate or revoke it in the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-wan2-7)
- [dLazy CLI source listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can return hosted result URLs or save generated media locally.]

## Skill Version(s):

1.3.28 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
