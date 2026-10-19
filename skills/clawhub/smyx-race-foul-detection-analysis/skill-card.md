## Description:

Analyzes pet race videos for false starts and lane crossings, returning structured results and report links to assist referees.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Race referees and event organizers use this skill to review start and finish video for suspected false starts or lane crossings and consult past analysis reports; final decisions remain with the referee.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Race videos or video URLs are sent to lifeemergence API services for analysis.

Mitigation: Obtain approval before submitting footage or URLs and check the service's data-handling terms.

Risk: The skill silently creates or reuses an identity, registers or logs in, and stores authentication tokens in a local workspace database.

Mitigation: Review this behavior before installation and restrict access to the workspace and its stored tokens.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-race-foul-detection-analysis)
- [API documentation](references/api_doc.md)
- [Skill usage demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis results or a Markdown report-history table with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can also be saved to a local file.]

## Skill Version(s):

1.0.12 (source: server-resolved ClawHub release; artifact SKILL.md lists 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
