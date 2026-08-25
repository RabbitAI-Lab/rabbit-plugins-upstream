## Description:

Create source-grounded weekly HRBP decision briefs for accountable human review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mwclaw](https://clawhub.ai/user/mwclaw)

### License/Terms of Use:

MIT-0

## Use Case:

HR business partners and authorized reviewers use this skill to turn approved weekly HR source packets into source-labeled decision briefs for accountable human review. It is intended for draft preparation and verification handoff, not for making or executing employment decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HR briefs may include unsupported claims, hidden missing facts, or conflated legal, policy, and operating-practice statements.

Mitigation: Use only approved source packets, cite source labels for material claims, preserve conflicts and missing facts, and perform independent source comparison before human disposition.

Risk: The local checker can be mistaken for factual, policy, legal, or decision approval.

Mitigation: Treat checker output as structural completeness only and keep the brief marked DRAFT - HUMAN REVIEW REQUIRED until authorized human review is complete.

Risk: Inputs may contain unnecessary sensitive personal data for HR-related drafting.

Mitigation: Stop and request a minimized or de-identified packet when unnecessary personal data, credentials, medical details, government identifiers, home addresses, or unrelated sensitive information are present.

## Reference(s):

- [Evaluation Cases](references/evals.md)
- [Weekly Decision Brief Template](templates/weekly-decision-brief.md)
- [Synthetic Brief Example](examples/synthetic-brief.md)
- [ClawHub Skill Page](https://clawhub.ai/mwclaw/skills/hrbp-weekly-decision-brief)
- [Publisher Profile](https://clawhub.ai/user/mwclaw)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands]

**Output Format:** [Markdown brief with source references and an optional local structural-check command]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Drafts must remain marked for human review; the checker verifies structural completeness only.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
