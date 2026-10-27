## Description:

Drafts Chinese multi-source research briefs with source-linked findings, retrieval dates, explicit evidence gaps, and conclusions left for human review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and researchers can use this skill to organize multiple Chinese-language sources into a brief whose findings link back to dated sources and whose evidence gaps are stated explicitly. It does not provide investment recommendations or final judgments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Enabling online research may send CUE_API_KEY to a connection destination that has not been verified.

Mitigation: Use the offline workflow without an API key until the destination is independently verified and restricted to approved HTTPS origins.

Risk: The brief checker can miss evidence gaps, so a passing result does not establish that claims or conclusions are adequately supported.

Mitigation: Review cited sources, retrieval dates, missing evidence, and conclusions manually, even after the checker passes.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huhoo/skills/cue-cn-research-brief)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown brief with four sections, source anchors, URLs, and retrieval dates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes explicitly named evidence gaps; conclusions and judgment calls remain for human review.]

## Skill Version(s):

0.1.0 (source: SKILL.md frontmatter, CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
