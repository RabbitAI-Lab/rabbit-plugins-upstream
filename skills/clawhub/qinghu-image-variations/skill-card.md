## Description:

Creates multiple ecommerce product-image variants from one source image, including different backgrounds, layouts, and marketing styles for ad creative testing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and ecommerce operators use this skill to generate batches of product-image variants for ad campaigns, marketplace listings, and A/B creative testing. The agent helps choose Qinghu AI image modes, estimate credits, run qhkit commands, and return generated image URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs the agent to install or upgrade an unpinned global qhkit npm package.

Mitigation: Approve installation explicitly and prefer a pinned, reviewed qhkit version before running the skill.

Risk: The skill can upload selected product images to Qinghu AI for generation.

Mitigation: Use only images approved for third-party processing and review outputs before publishing or using them in ads.

Risk: The skill needs a Qinghu API token and may persist it in CLI configuration.

Mitigation: Provide the token through a temporary protected secret when possible instead of a persistent config file.

Risk: Image generation can consume Qinghu credits.

Mitigation: Run qhkit image estimate for large batches and confirm available balance before generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-image-variations)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Markdown]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON command outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated image URLs and credit usage reported by qhkit.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
