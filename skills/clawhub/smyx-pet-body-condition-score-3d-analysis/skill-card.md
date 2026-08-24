## Description:

Analyzes pet images or multi-angle videos through external health-analysis APIs to estimate a visual 3D Body Condition Score (BCS 1-9), classify body condition, and return structured reports without disease diagnosis or treatment advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External ClawHub users and developers use this skill to submit pet media or URLs for BCS analysis, retrieve structured analysis results, and query cloud-hosted historical reports for pet weight-management workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded pet media or media URLs may be sent to external services for analysis.

Mitigation: Use the skill only with explicit consent for media submission, documented retention expectations, and endpoint configuration scoped to approved production services.

Risk: The skill can silently create or reuse an internal account identity and store auth tokens locally.

Mitigation: Review identity handling before deployment, protect the workspace data directory, rotate tokens as needed, and disclose account creation or reuse behavior to users or administrators.

Risk: Cloud history reports can be fetched automatically from trigger phrases with limited user control.

Mitigation: Require a clear confirmation or policy gate before historical report retrieval and scope report access to the intended user identity.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-body-condition-score-3d-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [JSON or Markdown text with structured report content and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return BCS classifications, cloud history report records, and report export links.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
