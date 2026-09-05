## Description:

Analyzes pet water fountain area videos or video URLs through a remote service to estimate drinking events, session duration, daily intake, historical changes, and health-reference alerts for drops or spikes in water consumption.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze pet water-fountain videos or URLs, retrieve structured drinking-intake reports, and query cloud-stored historical analysis records. Results are health references based on estimated intake behavior, not veterinary diagnosis or treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends pet water-fountain videos, URLs, and identity-linked history requests to a remote service.

Mitigation: Install and run only where users accept remote media processing and identity-linked cloud report retrieval for this publisher service.

Risk: The skill silently creates or reuses an internal user identity and persists account tokens locally.

Mitigation: Review local credential storage expectations before deployment and avoid use in environments that prohibit persistent local account tokens.

Risk: The security verdict is suspicious because user control over identity-linked remote processing is limited.

Mitigation: Require explicit deployment review before installation and communicate the remote processing and local persistence behavior to operators.

## Reference(s):

- [Pet Water Fountain Intake Analysis API documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, API calls, shell commands, configuration]

**Output Format:** [Markdown text with structured JSON analysis content and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write the rendered analysis result to a user-specified output file.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
