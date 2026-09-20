## Description:

A workflow skill for planning marketing brochure layouts, generating approved unfolded designs, and producing folded and lifestyle mock-ups through dLazy image generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and marketing or design teams use this skill to plan brochure content, confirm fold layouts, and produce image-generation prompts, dLazy CLI commands, and generated brochure mock-up URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files can be sent to dLazy SaaS endpoints, and generated results are hosted by dLazy.

Mitigation: Avoid submitting sensitive or restricted content unless approved for dLazy processing, and disclose the external SaaS flow before generation.

Risk: The dLazy API key may be stored in the user's local CLI configuration.

Mitigation: Use the npx or environment-variable option when persistent global CLI configuration is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Image generation may spend credits before the requested brochure direction is aligned.

Mitigation: Require explicit prompt, layout, and mock-up approval gates before running generation commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-marketing-brochure)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with CLI commands and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires stepwise user confirmation before generation and layout approval before mock-up production.]

## Skill Version(s):

1.3.19 (source: server release evidence; artifact frontmatter reports 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
