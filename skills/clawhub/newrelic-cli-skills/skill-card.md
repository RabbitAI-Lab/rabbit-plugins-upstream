## Description: <br>
Monitor, query, and manage New Relic observability data via the newrelic CLI, including NRQL queries, APM performance triage, deployment markers, alert policy and condition management, notification channel setup, infrastructure monitoring, and agent diagnostics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vince-winkintel](https://clawhub.ai/user/vince-winkintel) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, SREs, and observability engineers use this skill to inspect New Relic telemetry, triage application and infrastructure issues, record deployment markers, and manage selected alerting resources through the New Relic CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Alert policy, alert condition, notification channel, deployment marker, and alert condition deletion commands can change New Relic account state. <br>
Mitigation: Review write and delete commands before execution and use a least-privileged New Relic key scoped only to intended accounts. <br>
Risk: New Relic CLI profile setup can store credentials and change the default profile on the machine. <br>
Mitigation: Use a dedicated profile for agent workflows, protect stored credentials, and verify the active profile before running commands. <br>
Risk: Queries and scripts can expose sensitive observability data from the configured New Relic account. <br>
Mitigation: Install and run the skill only for accounts the agent is intended to inspect or manage. <br>
Risk: Untrusted values embedded in NRQL can alter query behavior. <br>
Mitigation: Validate user-provided query inputs and preserve the artifact scripts' escaping behavior when adapting commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/vince-winkintel/skills/newrelic-cli-skills) <br>
- [NRQL Patterns Reference](references/nrql-patterns.md) <br>
- [Performance Triage Guide](references/performance-triage.md) <br>
- [New Relic CLI releases](https://github.com/newrelic/newrelic-cli/releases) <br>
- [New Relic data exploration](https://one.newrelic.com/data-exploration) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash and NRQL code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the newrelic CLI plus NEW_RELIC_API_KEY and NEW_RELIC_ACCOUNT_ID; outputs may include New Relic account observability data returned by CLI commands.] <br>

## Skill Version(s): <br>
1.0.5 (source: SKILL.md frontmatter, VERSION, and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
