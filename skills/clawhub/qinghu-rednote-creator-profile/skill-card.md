## Description:

Retrieves Xiaohongshu creator profile information, including follower counts, likes, saves, and biography, from a profile link using Qinghu AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and marketers use this skill to look up Xiaohongshu creator profiles and assess potential influencers using profile metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or update Node and qhkit on the user's machine without enough user-directed control.

Mitigation: Review before installing; prefer a preinstalled, pinned qhkit version and obtain user approval before changing local tooling.

Risk: Configuring a Qinghu API token may leave credentials stored locally.

Mitigation: Prefer a session-scoped token over persistent local credential setup, and obtain the user's consent before configuring credentials.

Risk: Profile lookups incur Qinghu credit charges that may vary with the result size.

Mitigation: Estimate credits and disclose expected costs before obtaining consent for paid calls; report actual credits used.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-rednote-creator-profile)
- [Qinghu qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise Markdown profile summaries; spreadsheet files for larger result sets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports Qinghu credit usage for paid lookups; may provide a file for larger results]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
