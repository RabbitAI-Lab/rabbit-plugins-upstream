## Description:

Analyzes videos to evaluate human eating behaviors, habits, and dietary patterns, identifies tendencies toward unhealthy eating, and provides structured analysis reports with nutritional improvement recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze meal videos or video URLs for eating speed, dining habits, dietary structure, risk behaviors, and nutrition recommendations. It can also query cloud-hosted diet analysis report history associated with the current workspace identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Meal videos or URLs are processed by a remote cloud service.

Mitigation: Use non-sensitive inputs unless the publisher's data handling, retention, and account practices are acceptable for the intended use.

Risk: The skill silently creates or reuses identity state and stores account tokens in the local workspace.

Mitigation: Run the skill in a dedicated workspace and review local account state before sharing or reusing that workspace.

Risk: Historical report queries are performed automatically through cloud APIs.

Mitigation: Review cloud report access expectations before enabling history queries, especially in shared or multi-user environments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-diet-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON or Markdown-style structured analysis reports, with optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include health scores, eating behavior observations, risk warnings, suggestions, and links to exported cloud reports.]

## Skill Version(s):

1.0.10 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
