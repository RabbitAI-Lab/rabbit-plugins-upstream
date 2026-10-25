## Description:

Analyzes child activity footage for contact with dangerous objects and returns safety alerts and reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, caregivers, and child-safety system operators use this skill to analyze home or classroom footage for dangerous object contact and review alerts or past reports. It supplements, rather than replaces, adult supervision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive child and home monitoring footage or video references are sent to external cloud services.

Mitigation: Obtain guardian consent, use trusted video URLs, and share only necessary footage.

Risk: Cloud report history is linked to a persistent identity that may be created without an explicit prompt, with a token retained locally.

Mitigation: Review account and token handling before use; protect local tokens and establish clear report retention and deletion controls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-child-dangerous-object-detection-analysis)
- [API documentation](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis report or Markdown report-history table; optional JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include alerts, event details, and links to reports.]

## Skill Version(s):

1.0.8 (source: server-resolved ClawHub release; bundled skill frontmatter says 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
