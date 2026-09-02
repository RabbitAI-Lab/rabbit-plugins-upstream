## Description:

Analyzes children's learning behavior from video or URL inputs and returns structured reports on focus, posture, study habits, risk indicators, and family education suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, educators, and agents supporting family education use this skill to submit a child's study video or video URL for learning-behavior analysis. It can also retrieve the user's historical learning analysis reports from the configured cloud API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may upload children's study videos or URL references to a remote service.

Mitigation: Install only after confirming consent to process minors' media and verifying the service endpoint, TLS use, retention policy, and deletion behavior.

Risk: Reports may be associated with an internal or locally generated identity and historical reports can be retrieved from the cloud API.

Mitigation: Review identity handling, access controls, and local workspace storage before use in shared or regulated environments.

Risk: Security evidence reports a mismatch between privacy claims and observed endpoint, upload, identity-linking, and token-storage behavior.

Mitigation: Treat the release as requiring careful review before installation and use the publisher service only where its data-handling terms are acceptable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-study-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON analysis reports, optional saved text output, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include structured learning-behavior results, historical report lists, risk warnings, suggestions, and report export URLs.]

## Skill Version(s):

1.0.15 (source: ClawHub server release evidence; artifact frontmatter states 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
