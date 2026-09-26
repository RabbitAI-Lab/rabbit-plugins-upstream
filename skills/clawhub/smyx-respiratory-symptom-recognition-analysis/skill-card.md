## Description:

Analyzes respiratory videos or images for coughing, phlegm, and wheezing, and provides symptom counts and early health alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

People and caregivers use the skill to review respiratory symptoms in supplied media and retrieve past monitoring reports for follow-up. Its alerts are for monitoring, not medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Respiratory media and historical report queries are sent to lifeemergence.com services.

Mitigation: Avoid submitting real health media until you have reviewed the publisher's privacy, retention, and deletion commitments; use a separate workspace or account for sensitive testing.

Risk: The skill silently creates or reuses a local identity and stores access tokens in a workspace SQLite database.

Mitigation: Use an isolated workspace and account, and review the local identity and token handling before deployment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-respiratory-symptom-recognition-analysis)
- [Respiratory analysis API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Text or Markdown with structured JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Symptom counts, health alerts, suggestions, historical report links, and optional saved output.]

## Skill Version(s):

1.0.17 (source: server-resolved ClawHub release; artifact frontmatter lists 1.0.19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
