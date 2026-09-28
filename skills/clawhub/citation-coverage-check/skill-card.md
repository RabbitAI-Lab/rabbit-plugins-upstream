## Description:

Checks the share of numeric or dated claims in a document that include source markers and lists claims missing them.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (code only); documentation and theory all rights reserved

## Use Case:

Developers and report authors use this skill to identify numeric or dated claims in drafts that lack nearby source markers before human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reading sensitive local documents can expose their contents to the agent.

Mitigation: Grant only the tools needed for local checks and select documents you are comfortable sharing with the agent.

Risk: Source-marker matching does not verify whether a citation supports a claim.

Mitigation: Review flagged claims and verify cited sources before relying on the report.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/citation-coverage-check)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Plain text or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports coverage, missing-source excerpts and pass/fail against a configurable threshold.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata; bundled SKILL.md says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
