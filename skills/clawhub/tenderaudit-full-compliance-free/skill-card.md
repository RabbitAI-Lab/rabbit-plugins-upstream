## Description:

Provides a free local pre-check for Chinese tender documents by validating bidder line-item arithmetic and scanning for unreplaced template placeholders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement and tendering teams use this skill to run a zero-cost local pre-submission check on bidding materials. It identifies arithmetic mismatches in bidder line items and leftover template placeholders, but does not make legal, scoring, or award determinations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The free local audit appears purpose-aligned, but the skill also points users toward mutable external payment tooling and a paid skill purchase flow.

Mitigation: Use the free audit only with local JSON inputs unless you separately trust the payment tooling, verify the package source and version, and explicitly want the paid product installed.

Risk: Audit output may be mistaken for a legal, scoring, or award determination.

Mitigation: Treat results as a mechanical pre-check and have qualified reviewers or the responsible evaluation body make final determinations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/tenderaudit-full-compliance-free)
- [Sample input JSON](artifact/templates/sample.json)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Human-readable text or JSON report, with command-line usage guidance in Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs local deterministic checks and reports insufficient input instead of fabricating conclusions.]

## Skill Version(s):

1.1.7 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
