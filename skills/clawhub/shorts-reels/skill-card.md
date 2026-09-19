## Description:

Generates priced batches of vertical 9:16 short-form video drafts, helps compare a contact sheet, and guides promotion of a selected take for Shorts, Reels, or TikTok workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and agent operators use this skill to generate several low-cost vertical video draft options, compare them visually, and decide whether to re-render a chosen clip for final use. It is intended for short-form social raw material where iteration and selection matter more than producing a single finished clip immediately.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary reports overbroad fallback install guidance with unpinned global installer commands that can affect all agent skills.

Mitigation: Install only the specific Ofox core and scenario skills needed, and prefer pinned or reviewed installer versions.

Risk: Paid generation can incur charges or create outputs in an unintended directory if the batch is run without review.

Mitigation: Confirm the dry-run cost table, output directory, and API key handling before starting paid jobs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ofoxai/skills/shorts-reels)
- [Skill homepage](https://github.com/ofoxai/skills/tree/main/skills/shorts-reels)
- [Ofox API keys](https://app.ofox.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash commands, approval prompts, cost summaries, and generated artifact paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local video files and contact-sheet paths produced by Ofox jobs; requires OFOX_API_KEY for paid generation.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
