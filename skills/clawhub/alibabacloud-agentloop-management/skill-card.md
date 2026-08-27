## Description:

This skill routes Alibaba Cloud AgentLoop requests for observability onboarding, Dataset management, Pipeline creation, evaluation workflows, and experience recall.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to plan and execute Alibaba Cloud AgentLoop workflows, including application observability onboarding, Datasets, Pipelines, evaluations, and recall of prior experience.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make persistent Alibaba Cloud resource changes and may trigger costly evaluation or pipeline runs.

Mitigation: Use the documented dry-run and confirmation protocols, confirm every resource parameter, and operate with a narrowly scoped RAM role.

Risk: Some workflows can retrieve sensitive cluster access files or service credentials.

Mitigation: Grant kubeconfig and delete permissions only when required, keep secrets in environment variables, and redact credential values from chat, logs, and generated reports.

Risk: Updater or installer guidance may execute remote setup scripts or change local CLI plugins.

Mitigation: Review downloaded scripts and prefer organization-approved installation or built-in update paths before execution.

Risk: Evaluation, embedding, agentic, LLM, or recall workflows may send task text, dataset fields, or query text to external services.

Mitigation: Keep recall disabled unless outbound sharing is approved, minimize or redact dataset fields, and avoid printing real conversation bodies during previews.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sdk-team/skills/alibabacloud-agentloop-management)
- [AgentLoop skill router](SKILL.md)
- [Application onboarding](references/onboarding.md)
- [Dataset management](references/dataset/dataset.md)
- [Pipeline workflows](references/pipeline/pipeline.md)
- [Evaluation workflows](references/evaluation/evaluation.md)
- [Experience recall](references/experience/experience.md)
- [RAM policies](references/ram-policies.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with shell command, JSON, and code snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes dry-run, confirmation, verification, and credential-redaction guidance; bundled helper scripts may emit JSON.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
