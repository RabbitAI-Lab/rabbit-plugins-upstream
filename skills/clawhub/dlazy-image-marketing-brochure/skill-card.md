## Description:

A workflow skill for marketing brochure design that guides requirements gathering, layout design, user confirmation, folded mock-ups, and lifestyle mock-ups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, design, and business users use this skill to plan brochure content, generate unfolded layouts for common fold types, confirm the layout, and then produce folded and lifestyle mock-ups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs or runs a third-party npm CLI and may store a persistent API key.

Mitigation: Prefer npx or a sandboxed local install, use a revocable API key, and rotate or revoke credentials when no longer needed.

Risk: Prompts and local media paths supplied for generation may be sent to dLazy services and media storage.

Mitigation: Avoid sensitive local files and confirm each command, file input, and upload target before generation.

Risk: Brochures for regulated industries can omit required disclaimers or contain misleading claims.

Mitigation: Review generated copy and layouts for brand, legal, and compliance requirements before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-marketing-brochure)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline bash commands and generated asset URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate remote image assets through the dLazy API after user confirmation.]

## Skill Version(s):

1.3.17 (source: server release metadata; artifact frontmatter reports 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
