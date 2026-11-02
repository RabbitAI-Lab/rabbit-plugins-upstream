## Description:

Analyzes crib camera images or videos to estimate infant blanket coverage and identify kicking or blanket-slip events, returning alerts and reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and infant-care teams can use crib camera footage to review blanket coverage and kicking events and receive monitoring reports. Treat alerts as a supplementary cue; the skill documentation says it does not replace adult supervision or provide medical advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shared accounts can expose private infant-monitoring reports.

Mitigation: Wait for sender-isolation fixes, use a dedicated service credential, and confirm the provider's processing, retention, and account-deletion terms before submitting footage.

Risk: Export-only mode may still submit footage for analysis.

Mitigation: Wait for export-only fixes before submitting private footage and confirm the provider's handling terms.

Risk: Continuous monitoring and automatic alerts are unverified.

Mitigation: Treat alerts as supplementary and do not rely on continuous monitoring until it is verified; the skill documentation says it does not replace adult supervision.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-blanket-kick-detection-analysis)
- [API interface documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [JSON, Markdown, Guidance]

**Output Format:** [Structured JSON analysis reports and Markdown report lists, with alerts and report links when available.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include estimated blanket coverage, coverage state, detected events, and alert summaries.]

## Skill Version(s):

1.0.13 (source: release evidence and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
