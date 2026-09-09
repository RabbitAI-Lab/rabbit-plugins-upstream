## Description:

Trace Home Assistant incidents by correlating automations, logbook attribution, entity history, and device registry records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nextaltair](https://clawhub.ai/user/nextaltair)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and Home Assistant users use this skill to investigate unexpected device state changes by tracing automations, logbook attribution, entity history, and registry metadata. It helps report the strongest supported causal path, alternatives, missing decisive evidence, and the smallest safe measurement that would distinguish them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The investigation may expose sensitive Home Assistant data such as tokens, MAC addresses, registry identifiers, unrelated configuration, or broader history than the incident requires.

Mitigation: Limit inspection to the incident window and relevant entities, and redact credentials, identifiers, unrelated configuration, and unnecessary history from reports.

Risk: An incident report could overstate causality when evidence is indirect, speculative, truncated, or based on proxy telemetry.

Mitigation: Label evidence levels clearly, preserve gaps and polling delays, name missing decisive evidence, and verify static configuration, logbook attribution, and narrow history before reporting a causal path.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nextaltair/skills/home-assistant-causal-incident-analysis)
- [Publisher profile](https://clawhub.ai/user/nextaltair)

## Skill Output:

**Output Type(s):** [analysis, markdown, guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces an evidence-ranked incident report with causal path, alternatives, missing evidence, and recommended next measurement.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
