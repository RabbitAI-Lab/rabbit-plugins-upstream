## Description:

Guides OpenClaw agents in turning YouTube videos or local audio into time-ordered, evidence-grounded listening-experience prompts and music-structure analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sellemain](https://clawhub.ai/user/sellemain)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to analyze music from YouTube or local files and write grounded, time-ordered listening descriptions or identify structural moments in a music video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow requires a separately installed CLI from an external package source.

Mitigation: Verify the package and source before installation when supply-chain provenance matters.

Risk: Analyzing YouTube media can download content and create local analysis files.

Mitigation: Process only media you are authorized to use and review stored analysis files.

Risk: Passing assembled prompts to another model may disclose included lyrics, context, or frames.

Mitigation: Review the assembled prompt before sharing it with an external model.

## Reference(s):

- [Galdr metric reference](references/metrics.md)
- [Galdr on ClawHub](https://clawhub.ai/sellemain/skills/galdr)
- [Galdr CLI on PyPI](https://pypi.org/project/galdr/)

## Skill Output:

**Output Type(s):** [Markdown, Analysis, Shell commands, Guidance]

**Output Format:** [Markdown prose and command examples; may guide creation of local analysis JSON and assembled prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Audio-derived metrics are interpretation cues, not measured listener responses.]

## Skill Version(s):

0.7.2 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
