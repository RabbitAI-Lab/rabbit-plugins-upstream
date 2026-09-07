## Description:

Turns product photos or listings into conversion-focused ecommerce ad videos for stores, TikTok Shop, and cross-border selling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, and developers use this skill to generate product ad videos from product images, documents, catalogs, or marketplace listings through the dLazy CLI and hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the third-party dLazy CLI and hosted service.

Mitigation: Review the linked CLI source or npm package before installing, and prefer npx or an isolated environment if you do not want a global CLI.

Risk: The dLazy API key is a credential stored or supplied to the CLI.

Mitigation: Treat the key like a secret and rotate or revoke it from the dLazy dashboard if needed.

Risk: Attached product files may be uploaded to dLazy storage for processing.

Mitigation: Only attach product files you are comfortable uploading to dLazy.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-video)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown or terminal text with dLazy CLI commands and hosted service responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require a dLazy API key and may upload attached product files to dLazy storage.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter lists 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
