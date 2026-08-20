## Description:

Motion graphics, kinetic typography, animated text video, animated infographic, and explainer animation authored as Remotion code, then polished and exported for code-driven animated graphics rather than AI-generated footage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creative technologists, and content teams use this skill to start or continue dLazy motion-graphics projects that generate Remotion-based animated text, infographic, explainer, and branded video work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and files attached with --files are sent to dLazy infrastructure.

Mitigation: Do not submit secrets, credentials, regulated data, or confidential files unless that external sharing has been approved.

Risk: The dLazy CLI stores an API key in local user configuration.

Mitigation: Use the documented login or auth flow, restrict access to the local config file, and rotate or revoke the key from the dLazy dashboard when needed.

Risk: The skill depends on a hosted SaaS CLI and network endpoints for normal operation.

Mitigation: Install and use it only in environments where communication with api.dlazy.com and files.dlazy.com is approved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-motion-graphics)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and CLI guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference dLazy project ids and uploaded file URLs when continuing or attaching project context.]

## Skill Version(s):

1.3.8 (source: ClawHub release evidence; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
