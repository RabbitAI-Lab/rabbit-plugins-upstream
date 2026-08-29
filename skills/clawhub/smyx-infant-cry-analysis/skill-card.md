## Description:

Detects baby cries via audio AI in real-time, analyzes causes, and identifies needs like hunger, tiredness, pain, discomfort, or irritability to assist new parents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers and parenting-support agents use this skill to submit infant cry audio or video files or URLs, receive structured cause and need analysis, and retrieve previous reports for reference.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Infant or family media and URLs may be sent to the Life Emergence service for analysis.

Mitigation: Install only where this external processing is acceptable and avoid uploading sensitive media without appropriate consent.

Risk: The skill may create or reuse a local workspace identity, create or reuse a local database, and store tokens locally.

Mitigation: Review local identity, database, and token handling before deployment, and restrict workspace access accordingly.

Risk: Report-listing requests may automatically query cloud report history.

Mitigation: Use history retrieval only in contexts where account-linked report history access is expected.

Risk: Cry analysis output may be over-relied on as medical advice.

Mitigation: Present results as parenting reference only and seek medical care for persistent crying, distress, or health concerns.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-cry-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Guidance]

**Output Format:** [Structured text, Markdown report tables, optional JSON detail, and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include analysis status, recognized needs, recommendations, report links, and cloud history results.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact SKILL.md frontmatter reports 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
