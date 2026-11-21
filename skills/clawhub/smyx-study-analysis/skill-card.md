## Description:

Analyzes videos of children's and students' learning behavior to identify study habits and provide structured reports with family education suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and educators can use the skill to review study videos, receive observations about learning behaviors, and get suggestions for supporting study habits at home. Its reports are for educational reference and do not replace professional assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags possible exposure of sensitive student videos or reports, remote credentials, and user identity when the skill communicates with its cloud service.

Mitigation: Review account registration and credential handling, confirm where videos are sent, and avoid sensitive student media until those data flows are understood.

Risk: The security review asks whether an export-only choice could still allow video analysis, and notes that coverage is incomplete because a local reference could not be resolved.

Mitigation: Verify export-only behavior before relying on it to prevent analysis, and resolve the missing reference or obtain complete scan coverage.

## Reference(s):

- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-study-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Markdown]

**Output Format:** [Structured analysis report as text or JSON; Markdown tables for report listings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include behavior observations, risk indicators, family education suggestions, and report links.]

## Skill Version(s):

1.0.22 (source: server-resolved release metadata; packaged SKILL.md declares 1.0.26)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
