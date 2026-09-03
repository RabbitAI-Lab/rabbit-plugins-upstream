## Description:

Creates marketing, promotional, advertising, and brand videos from a product, brand, or brief for social media or campaign use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and marketing teams use this skill to turn product specs, manuals, catalogs, or ecommerce listings into conversion-focused shopping videos with multilingual voiceover and an optional virtual host.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses dLazy as an external SaaS, so prompts, selected files, and project context may be sent to dLazy services.

Mitigation: Use the skill only with content approved for dLazy processing, attach only necessary files, and clear or compact project context when it is no longer needed.

Risk: The dLazy CLI stores an API key locally and project sessions may persist across turns.

Mitigation: Prefer per-invocation DLAZY_API_KEY or npx when appropriate, review local config file permissions after login, and rotate, revoke, or log out credentials when access should end.

Risk: Security evidence reports that a local file-permission claim in the skill text was not enforced by inspected CLI code.

Mitigation: Do not rely solely on the CLI for credential file hardening; verify operating-system permissions on ~/.dlazy/config.json or avoid persistent local credential storage.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May stream agent responses from dLazy and may reference uploaded local files by URL when files are attached.]

## Skill Version(s):

1.0.8 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
