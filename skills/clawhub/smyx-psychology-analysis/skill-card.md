## Description:

Analyzes human mental health and psychological behavior, supports identifying common psychological problem tendencies through video analysis, and provides structured mental health analysis reports and improvement suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze submitted videos or video URLs for psychological behavior signals, mental health tendencies, and structured improvement suggestions. It can also retrieve cloud-hosted historical mental health analysis reports for the resolved user identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive videos, video URLs, identity metadata, and historical report requests may be sent to an external service and associated with a persistent account.

Mitigation: Require explicit consent for each analysis or history lookup, avoid analyzing third-party or highly private videos without permission, and verify the service endpoint plus data retention and deletion terms before use.

Risk: Cloud history lookup can expose prior mental health analysis reports linked to the resolved user identity.

Mitigation: Confirm the user's intent before history retrieval and return only the report history needed for the current request.

Risk: Mental health analysis output could be mistaken for professional diagnosis or treatment advice.

Mitigation: Present results as informational mental health reference only and direct users with psychological distress to qualified professionals.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-psychology-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown or JSON structured report with analysis details, suggestions, history results, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud report history and external report export links returned by the configured service.]

## Skill Version(s):

1.0.17 (source: server release metadata; artifact frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
