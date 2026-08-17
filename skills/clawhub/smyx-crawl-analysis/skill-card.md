## Description:

Analyzes reptile or arachnid videos or URLs through server-side APIs to identify skin, scale, and body-condition indicators, screen for possible disease risks, and return a Pet Safety Guardian health report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit reptile or arachnid media for server-side visual health analysis, receive structured findings, and retrieve report links or historical cloud reports. Results are health references and are not a substitute for professional veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted media, URLs, and identity data are sent to external lifeemergence.com services.

Mitigation: Use only media and URLs approved for external processing, and avoid private/internal URLs or sensitive videos unless the publisher documents account handling, retention, and authorization controls.

Risk: The skill may create or reuse a local identity and store returned access tokens locally.

Mitigation: Review local workspace data and token storage behavior before installation, and run the skill in an isolated workspace when handling sensitive user contexts.

Risk: The skill can retrieve historical cloud reports associated with the resolved identity.

Mitigation: Confirm that the identity and report-history access model matches the intended user or tenant before allowing historical report queries.

Risk: Health analysis output may be incorrect or incomplete.

Mitigation: Present results as informational health references and direct users to professional veterinary diagnosis for medical decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-crawl-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown or JSON health report text with optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured health findings, warnings, care suggestions, historical report lists, and exported report URLs.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter states 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
