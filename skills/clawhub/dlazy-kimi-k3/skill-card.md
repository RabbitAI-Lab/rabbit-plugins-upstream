## Description:

Connects agents to Moonshot AI’s Kimi K3 model for text, image, and video understanding, supporting complex analysis, coding, and long-form writing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can ask Kimi K3 to analyze text or supplied images and videos, write content, and generate code. Requests require a dLazy API key and may consume service credits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy’s hosted services for processing.

Mitigation: Send only prompts and media you are comfortable sharing with dLazy, and review the service terms before use.

Risk: The CLI saves an API key locally, and requests may consume service credits.

Mitigation: Protect the local CLI configuration or use per-invocation authentication; rotate or revoke keys when needed, and use the CLI dry run to inspect estimated cost.

Risk: The external executable package and its credential-storage protections were not independently verified.

Mitigation: Review the pinned @dlazy/cli 1.2.3 package and its repository before installing or using it with credentials.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-kimi-k3)
- [dLazy service](https://dlazy.com)
- [@dlazy/cli package](https://www.npmjs.com/package/@dlazy/cli)
- [Repository link listed in skill metadata](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, JSON]

**Output Format:** [JSON response envelope containing generated result content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return asynchronously when requested; generated results can include text or other model-produced content.]

## Skill Version(s):

1.2.32 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
