## Description:

Analyzes smart feeder or IPC camera media to detect cats and dogs, recognize pet identity, enroll pets in a recognition database, and list historical analysis reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to route pet feeder or IPC camera images, videos, or media URLs through a cloud analysis service and return pet detection, identity recognition, enrollment, recommendations, and historical report results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review states that the skill sends pet images, videos, media URLs, identity data, and analysis requests to cloud or development endpoints.

Mitigation: Use only media whose upload and retention expectations are acceptable, and review the configured endpoint before running the skill.

Risk: The security review states that the skill can silently create or reuse a remote account and store access tokens in the workspace.

Mitigation: Run it in a controlled workspace, review local token storage, and remove credentials when the skill is no longer needed.

Risk: The security review verdict is suspicious because requests are bound to local or derived identity and use under-scoped cloud or development endpoints.

Mitigation: Install only after confirming the publisher, account behavior, endpoint configuration, and data handling are acceptable for the deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-detection-feeder-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands]

**Output Format:** [Markdown status text with structured JSON sections and optional saved result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include report links and historical report tables returned by the provider service.]

## Skill Version(s):

1.0.10 (source: ClawHub server release metadata; artifact frontmatter reports 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
