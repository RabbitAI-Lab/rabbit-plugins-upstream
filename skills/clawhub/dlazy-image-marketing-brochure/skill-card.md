## Description:

A workflow skill for marketing brochure design that guides requirements gathering, fold-type planning, layout-first generation, user confirmation, and final folded and lifestyle mock-up delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, designers, marketers, and agents use this skill to plan and generate brochure layouts and mock-ups for company, product, event, investment, enrollment, and portfolio promotion workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill requires trusting the dLazy CLI and cloud API with prompts and selected media files.

Mitigation: Install only after reviewing the dLazy CLI source or package, confirm prompts and media before command execution, and avoid sending sensitive content unless that use is approved.

Risk: Persistent local API keys may remain available to future CLI invocations.

Mitigation: Prefer the DLAZY_API_KEY environment variable for per-session use when persistence is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Generated brochure content can be incorrect, misleading, or unsuitable for regulated industries.

Mitigation: Review each layout and mock-up before use, and add required compliance disclaimers for regulated industries.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-marketing-brochure)
- [dLazy CLI source and homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Image URLs]

**Output Format:** [Markdown guidance with inline shell commands and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses dLazy CLI commands to request brochure layout and mock-up generation; prompts and selected media may be sent to dLazy services.]

## Skill Version(s):

1.3.9 (source: server release metadata; artifact frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
