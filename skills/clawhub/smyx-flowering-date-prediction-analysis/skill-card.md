## Description:

Predicts flowering dates for ornamental and cut-flower plants from bud imagery or video, optionally using temperature and light accumulation data to estimate full bloom in the next 3-7 days.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External growers, botanical garden operators, flower tourism teams, and agricultural developers use this skill to estimate bloom timing from greenhouse or drone-captured flower-bud media and optional environmental readings. It can also query previously generated analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends uploaded media or media URLs to the publisher's backend for analysis and report retrieval.

Mitigation: Use only media that is appropriate to share with the publisher's service, and review the configured endpoints before deployment.

Risk: The skill automatically manages identity and stores tokens or profile data locally.

Mitigation: Review local identity and token storage behavior before installation, especially on shared systems.

Risk: Configuration includes development or private-LAN backend endpoints alongside production endpoints.

Mitigation: Replace development or private-LAN configuration with approved production endpoints before operational use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-flowering-date-prediction-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown and JSON-style structured analysis text, including report links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local media paths, media URLs, report-list queries, and optional output-file writing.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
