## Description:

Requires OFOX_API_KEY; generates realistic-human, dialogue-driven short-drama video clips from a script or scene description using the Ofox video API and Seedance 2.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn a short dialogue beat into a generated video clip after a brief, cost estimate, and approval step. It is intended for fictional short-drama scenes with people talking to each other, not product shots, anime scenes, talking-head clips, or stitching multiple finished videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Missing-dependency guidance can lead to broad, unpinned installation of external skill packages into multiple agents.

Mitigation: Review the install path first and prefer a narrowly scoped, pinned installation of only ofox-video-core.

Risk: The skill requires an Ofox API key and sends prompts to Ofox to generate and download media.

Mitigation: Use an appropriate OFOX_API_KEY, review prompts before submission, and only proceed after the skill presents a cost estimate and receives approval.

Risk: Portrait or real-person inputs can create likeness-rights concerns.

Mitigation: Confirm the user has rights to the likeness before providing portrait inputs or enabling real-person handling.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ofoxai/skills/seedance-short-drama)
- [Source homepage](https://github.com/ofoxai/skills/tree/main/skills/seedance-short-drama)
- [Ofox API key management](https://app.ofox.ai)
- [Ofox model catalog](https://api.ofox.ai/v1/models/catalog)
- [Ofox video core approval gate](../ofox-video-core/references/approval-gate.md)
- [Ofox video core prompt structure](../ofox-video-core/references/prompt-structure.md)
- [Ofox video core API parameters](../ofox-video-core/references/api-params.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with structured prompt text, approval tables, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit, poll, download, and report generated video jobs through the dependent Ofox video core skill after user approval.]

## Skill Version(s):

1.13.4 (source: release evidence, frontmatter, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
