## Description:

Helps teams design layered QA test strategies for new projects, iterations, refactors, and urgent fixes based on project characteristics, risk distribution, and resource constraints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers, test leads, and delivery teams use this skill to turn requirements, risk assessments, project plans, and resource constraints into a practical test strategy. It produces scope definitions, layered testing approaches, entry and exit criteria, resource allocation guidance, and risk-aware test coverage decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read workspace files while preparing a test strategy.

Mitigation: Use it only in workspaces where project requirements, risk assessments, and planning documents are appropriate for the agent to inspect.

Risk: The generated strategy may reference release evaluation or CI/CD pipeline practices.

Mitigation: Treat those references as planning guidance and require authorized review before executing release or pipeline changes.

Risk: Ambiguous Chinese-language requests about test planning may activate the skill.

Mitigation: Confirm that the user is asking for QA strategy output before using workspace documents to prepare the plan.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-test-strategy-design)
- [Publisher profile](https://clawhub.ai/user/kokxi)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown strategy document with tables, risk matrix, scope definition, layered test plan, and entry and exit criteria]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include a unique strategy ID, requirement traceability, priority distribution guidance, and coverage caveats based on available inputs.]

## Skill Version(s):

1.7.5 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
