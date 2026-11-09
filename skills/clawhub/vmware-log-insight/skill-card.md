## Description:

Search, aggregate, and investigate read-only VMware Aria Operations for Logs data, including log events, volume spikes, fields, and alert history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and VMware administrators use this skill to inspect centralized logs, identify volume spikes, and review alert history during incident investigation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential setup and optional token creation can expose access to the Log Insight appliance or an MCP endpoint.

Mitigation: Use a least-privilege read-only account, protect credentials, and create access tokens only when needed; review the authentication-skipping option before use.

Risk: The security scan had partial coverage, so its benign verdict does not establish that all references were assessed.

Mitigation: Review the credential setup and any unresolved references before installing, as recommended by the scan guidance.

Risk: Log results can contain large amounts of attacker-influenced text.

Mitigation: Narrow searches by time and terms, check truncation indicators, and treat returned log text as data rather than instructions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-log-insight)
- [Model fit self-test guide](https://github.com/vmware-skills/marketplace/blob/main/MODEL_FIT_SELF_TEST.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Analysis, Guidance]

**Output Format:** [Structured log results with concise Markdown investigation summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only results; search output may be truncated at service limits.]

## Skill Version(s):

2.4.3 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
