## Description:

Generates cinematic product or brand ad video clips from a product description or photo using the Ofox video API, including a short creative brief, timestamped prompt, cost estimate, generation workflow, download, and final cost report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn product descriptions or product photos into commercial-style brand videos. It helps choose or confirm the product-photo route, brand tone, camera movement, aspect ratio, and cost before generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts and images are sent to Ofox for video generation.

Mitigation: Install and use only if sharing those inputs with Ofox is acceptable for the user's product and organization.

Risk: The skill depends on an external ofox-video-core helper and the security evidence flags this release for review.

Mitigation: Verify the helper skill from a trusted source before execution and avoid broad unpinned global installs.

Risk: Video generation can incur paid API costs.

Mitigation: Require the dry-run cost table and an explicit user confirmation before submitting a paid generation job.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ofoxai/skills/seedance-ad-creative)
- [Skill homepage](https://github.com/ofoxai/skills/tree/main/skills/seedance-ad-creative)
- [Ofox API key portal](https://app.ofox.ai)
- [Ofox models catalog](https://api.ofox.ai/v1/models/catalog)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with creative brief recap, timestamped video prompt, cost table, and shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires OFOX_API_KEY, curl, jq, and the ofox-video-core helper skill.]

## Skill Version(s):

1.12.1 (source: frontmatter, changelog, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
