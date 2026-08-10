## Description:

Predicts full-bloom timing for ornamental and cut-flower plants from greenhouse or drone imagery, optional temperature and light data, and cloud analysis services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External growers, greenhouse operators, botanical-garden staff, and developers use this skill to analyze flower-bud images or video and receive flowering-date predictions, confidence information, structured reports, and history queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Greenhouse images, video URLs, and report-history requests are sent to LifeEmergence cloud services.

Mitigation: Use only where cloud processing is acceptable, avoid sensitive facility footage, and review endpoint scope and data-retention terms before deployment.

Risk: The skill creates or reuses local identity state and stores returned tokens in a workspace database.

Mitigation: Run in an isolated workspace and review identity, token storage, and cleanup behavior before installing in shared or production environments.

Risk: Security evidence reports token-bearing cloud requests with weak user-facing control.

Mitigation: Limit use to trusted operators and require installation review until the publisher documents token handling and user controls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-flowering-date-prediction-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files]

**Output Format:** [Markdown or JSON-like structured analysis text, optionally saved to a file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links and cloud history-query results.]

## Skill Version(s):

1.0.6 (source: server release evidence; artifact frontmatter says 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
