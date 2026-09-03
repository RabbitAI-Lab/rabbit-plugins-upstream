## Description:

A professional pipeline for building everything from a core mark to a complete brand visual system, ensuring creative quality, execution consistency, and shippable delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, designers, marketers, and developers use this skill to plan logo and brand-system work, generate core mark concepts, and iteratively create derivative brand assets through dLazy CLI workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and referenced media may be sent to dLazy-hosted API and storage services.

Mitigation: Use the skill only when cloud processing is acceptable, and avoid sending sensitive prompts or media unless approved.

Risk: The dLazy API key can be persisted in a local CLI configuration file.

Mitigation: Use the DLAZY_API_KEY environment variable for one-off use when local key persistence is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Using the npm CLI introduces normal package supply-chain considerations.

Mitigation: Prefer npx for one-off use and review the package or source repository when supply-chain risk matters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-logo-branding-system)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses phased confirmations and one generation command at a time.]

## Skill Version(s):

1.2.9 (source: server release metadata; artifact frontmatter reports 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
