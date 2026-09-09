## Description:

Marketing Brochure guides an agent through requirements gathering, brochure layout generation, approval, and mock-up delivery using a layout-first workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, marketers, and agent users can use this skill to plan and generate marketing brochure layouts, folded mock-ups, and lifestyle mock-ups with an explicit approval gate before final rendering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install or invoke the dLazy CLI and submit prompts or selected media to dLazy-hosted services.

Mitigation: Use npx or a sandbox where practical, verify the reviewed @dlazy/cli@1.2.3 package before use, and use a revocable dLazy API key.

Risk: Generated shell commands could perform unintended actions if accepted without review.

Mitigation: Review each command before execution and keep the skill's required confirmation gates in place.

Risk: Brochure mock-ups can drift from the intended layout if generated without a confirmed source layout.

Mitigation: Require explicit approval of the layout before producing folded or lifestyle mock-ups, and use the approved layout as the reference for downstream images.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-marketing-brochure)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands]

**Output Format:** [Markdown guidance with inline shell commands and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user confirmation before image generation and before moving from layout design to mock-up production.]

## Skill Version(s):

1.3.15 (source: server release metadata; artifact frontmatter reports 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
