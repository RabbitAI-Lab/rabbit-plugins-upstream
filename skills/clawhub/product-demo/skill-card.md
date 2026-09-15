## Description:

Requires an OFOX_API_KEY and two real screenshots of one interface in different states, then guides an agent to create a short Ofox video that animates the transition between those states.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, product teams, and documentation authors use this skill to turn before-and-after screenshots of a real software interface into a short demo clip. It is suited to bounded UI state changes where recording the real app is unavailable or impractical.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Missing-dependency recovery may encourage broad unpinned global skill installation.

Mitigation: Install only the required ofox-video-core dependency from a trusted, pinned source and avoid wildcard global installs.

Risk: Screenshots may include secrets, customer data, live tokens, faces, or other private information that would be uploaded to Ofox and appear in the generated video.

Mitigation: Remove private or sensitive content from both screenshots before generating a job.

Risk: A paid video job could be approved before the user has checked cost and input attachment details.

Mitigation: Review the dry-run cost table and payload details before approving paid generation.

Risk: The skill delegates API handling and safety behavior to a separate core skill.

Mitigation: Inspect the core skill before use and keep it installed from a trusted, pinned source.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ofoxai/skills/product-demo)
- [Product-demo homepage](https://github.com/ofoxai/skills/tree/main/skills/product-demo)
- [Ofox API key portal](https://app.ofox.ai)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash commands, prompts, brief recaps, and cost approval tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides Ofox video generation from two UI screenshots; the delegated core skill reports the downloaded video path.]

## Skill Version(s):

1.0.1 (source: frontmatter, release evidence, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
