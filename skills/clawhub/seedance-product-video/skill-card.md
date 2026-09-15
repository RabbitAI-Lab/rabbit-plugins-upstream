## Description:

Generates clean catalog-style e-commerce product videos from a product photo or text description using Ofox video API guidance, including brief questions, literal-accuracy prompting, a cost estimate, and approved generation and download steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn product photos or product descriptions into catalog-style e-commerce listing footage with a short creative brief, prompt guidance, cost estimate, and approved Ofox generation workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts and images are sent to Ofox, and approved generation jobs may spend Ofox credits.

Mitigation: Use only with an approved OFOX_API_KEY, avoid sensitive product material unless permitted, and require explicit cost approval before submitting jobs.

Risk: The skill depends on an external ofox-video-core helper that may be resolved from several local install locations.

Mitigation: Install only the needed ofox-video-core dependency from a trusted pinned source and verify the resolved ofox-video.sh path before running jobs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ofoxai/skills/seedance-product-video)
- [Skill homepage](https://github.com/ofoxai/skills/tree/main/skills/seedance-product-video)
- [Ofox API console](https://app.ofox.ai)
- [Ofox models catalog](https://api.ofox.ai/v1/models/catalog)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with prompt text, brief recap, cost estimate, and shell-command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit and poll Ofox video API jobs through the required ofox-video-core dependency after explicit approval; reports downloaded video path and actual cost.]

## Skill Version(s):

1.15.1 (source: server release metadata, SKILL.md frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
