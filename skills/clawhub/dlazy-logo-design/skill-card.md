## Description:

Helps create, refine, and evaluate brand logos, including a transparent-background logo and previews across common brand contexts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, brand teams, and other users can create, upgrade, or evaluate logos and preview them in multiple brand contexts through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files are sent to the third-party dLazy service.

Mitigation: Share only prompts and files intended for that service.

Risk: Login stores a dLazy API key in local CLI configuration.

Mitigation: Protect the local account and revoke or rotate the key if compromised.

Risk: Clearing a project session discards its saved conversation context.

Mitigation: Use the clear option only when a fresh session is intended.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-logo-design)
- [dLazy CLI source (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text with logo results and multi-context previews]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Logo artwork and multi-context previews are delivered through the dLazy service.]

## Skill Version(s):

1.3.29 (source: ClawHub release; artifact frontmatter: 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
