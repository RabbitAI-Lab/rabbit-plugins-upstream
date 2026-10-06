## Description:

Chooses a notification cadence and deduplication key, then groups operational updates into a scheduled digest with delivery timing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations teams use this skill to choose a digest schedule and deduplication rule, then consolidate updates into a locally saved digest for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Operational updates included in downstream runs may be saved in a local Markdown digest.

Mitigation: Use a dedicated output directory and avoid sensitive updates unless local storage is acceptable.

## Reference(s):

- [Operations Digest Desk release](https://clawhub.ai/wxt-ai/skills/operations-digest-desk)
- [Operations Digest Desk README](README.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown]

**Output Format:** [Text cadence guidance, JSON digest summary and local Markdown digest]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The downstream operation writes a local digest only when given an output directory; it does not send notifications.]

## Skill Version(s):

3.0.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
