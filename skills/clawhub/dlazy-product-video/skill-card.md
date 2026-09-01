## Description:

Turns product photos, ecommerce listings, specifications, manuals, or catalogs into product demo, showcase, or advertising videos with multilingual voiceover and an optional virtual host.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask the dLazy hosted agent to create ecommerce product videos for demos, ads, showcases, and cross-border selling workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files are sent to dLazy services.

Mitigation: Share only content appropriate for the dLazy service and review files before attaching them.

Risk: The dLazy CLI may store an API key and project or session metadata under ~/.dlazy.

Mitigation: Use npx for on-demand execution when avoiding a global install, and rotate or revoke the API key from dLazy when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-product-video)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source reference](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and CLI guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill invokes the pinned dLazy CLI template and may stream agent responses while project sessions preserve context.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
