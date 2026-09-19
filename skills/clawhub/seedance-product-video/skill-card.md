## Description:

Generates clean catalog-style e-commerce product videos from product photos or product descriptions using the Ofox video API with Seedance 2.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and marketplace operators use this skill to turn product photos or product descriptions into plain-background listing videos, including a creative brief, prompt, cost estimate, generation call, download, and cost report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill executes a separately installed ofox-video-core script that can access OFOX_API_KEY and local product files.

Mitigation: Install only a pinned, verified core skill and provide only the API key and product files intended for the paid generation job.

Risk: Product photos and prompts are sent to the Ofox API and generation can incur paid jobs.

Mitigation: Use the creative brief, cost estimate, and approval gate to confirm product photo, aspect ratio, background, motion, and price before generation.

Risk: People, dialogue, or unauthorized likeness references fall outside this product-only skill's intended boundary.

Mitigation: Route people or dialogue requests to a more appropriate skill and use real-person references only when the user has the required rights.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ofoxai/skills/seedance-product-video)
- [Publisher profile: ofoxai](https://clawhub.ai/user/ofoxai)
- [Source homepage](https://github.com/ofoxai/skills/tree/main/skills/seedance-product-video)
- [Ofox app and API keys](https://app.ofox.ai)
- [Ofox models catalog API](https://api.ofox.ai/v1/models/catalog)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown brief, prompt, cost table, shell command output, and downloaded video file path]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires OFOX_API_KEY, curl, jq, and a separately installed ofox-video-core skill.]

## Skill Version(s):

1.16.1 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
