## Description:

Generates clean catalog-style product videos from a real product photo, or a text description for generic products, using the Ofox Seedance 2.5 video API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent developers use this skill to turn product photos or simple product descriptions into plain-background listing and catalog videos, with a brief, prompt, cost estimate, generation command, download, and cost report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images, prompts, and generation metadata may be sent to Ofox and paid jobs may incur charges.

Mitigation: Review the prompt, selected assets, and displayed cost estimate before approving generation; use only images and product data that may be shared with Ofox.

Risk: The release security summary flags an unpinned external skills repo installation path.

Mitigation: Prefer a pinned, reviewed copy of the required core skill instead of allowing an agent to run an unpinned install fallback automatically.

Risk: The security guidance notes confusing out-of-scope people or dialogue material in a product-only skill.

Mitigation: Use this skill only for inanimate product showcase clips and route people, voices, dialogue, or presenter-led commerce videos to a more appropriate reviewed skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ofoxai/skills/seedance-product-video)
- [Clawdis homepage](https://github.com/ofoxai/skills/tree/main/skills/seedance-product-video)
- [Ofox API dashboard](https://app.ofox.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with prompt text, cost table, shell command snippets, and video job report fields.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires OFOX_API_KEY, curl, and jq; generation can send selected product assets and prompts to Ofox and may incur approved API charges.]

## Skill Version(s):

1.13.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
