## Description:

AI-powered fruit ripeness grading for tomatoes and strawberries from images or videos, returning visual maturity grades, structured analysis results, harvest guidance, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External growers, greenhouse operators, smart grow-box users, home gardeners, cooperatives, and agents supporting them use this skill to analyze tomato or strawberry media for ripeness grading, harvest timing, and account-linked report history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fruit images, videos, or media URLs are sent to the LifeEmergence cloud service for analysis.

Mitigation: Use the skill only with media approved for that service and review retention, privacy, and account controls before submitting private or sensitive media.

Risk: The skill can create or reuse a local account identity and store service tokens in the workspace data database.

Mitigation: Run it in an appropriate workspace, protect or clear stored local identity data according to policy, and review account controls before installation.

Risk: History queries fetch account-linked report records automatically.

Mitigation: Confirm the active account context before listing historical reports and avoid using shared workspaces for private report histories.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fruit-ripeness-grading-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Interface Documentation](references/api_doc.md)
- [SMYX Analysis API Interface Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown or JSON-like structured text with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save report output to a file when requested.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter says 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
