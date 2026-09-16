## Description:

Creates a short Ofox video demo by animating between two real screenshots of the same user interface state, after checking order, visible differences, pricing, and capture constraints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, technical writers, and product teams use this skill to turn before/after UI captures into short demo clips for docs, changelogs, or product communication when recording the live app is not practical.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback installation and script-discovery guidance can create supply-chain and persistent agent-scope risk.

Mitigation: Install only a pinned, reviewed ofox-video-core version and verify the exact core script path before allowing it to handle OFOX_API_KEY or screenshots.

Risk: Screenshots and OFOX_API_KEY can expose private data during paid video generation.

Mitigation: Remove private data from screenshots before generation and provide the API key only to the reviewed command path that submits the job.

Risk: A wrong screenshot pair, reversed order, or unapproved resubmission can spend money on an unusable clip.

Mitigation: Confirm both captures, their order, the printed frame payload, and the documented cost approval before any paid job.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ofoxai/skills/product-demo)
- [Project homepage from metadata](https://github.com/ofoxai/skills/tree/main/skills/product-demo)
- [Ofox app and API key dashboard](https://app.ofox.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and Ofox video job parameters.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires OFOX_API_KEY and two matching UI screenshots; normal flow includes a dry-run cost table before paid generation.]

## Skill Version(s):

1.1.0 (source: frontmatter, changelog, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
