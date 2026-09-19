## Description:

VMware Debug helps agents troubleshoot VMware, vSphere, ESXi, and NSX incidents by correlating supplied events, ranking root-cause hypotheses, suggesting next checks, and recording investigation evidence in a local case ledger.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to diagnose active VMware or vSphere problems, correlate logs and events from companion skills, and decide what data or remediation path to pursue next. It is intended for troubleshooting incidents, not for executing fixes against VMware systems.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Auth troubleshooting may lead an agent to inspect credential-bearing configuration or .env files.

Mitigation: Use narrowly scoped, masked authentication checks and avoid submitting raw secrets as evidence.

Risk: Case folders may retain sensitive host names, addresses, log lines, event text, and investigation notes.

Mitigation: Store case data in owner-only locations and periodically delete closed case folders when retention is no longer needed.

Risk: Runtime package resolution can introduce deployment uncertainty in controlled environments.

Mitigation: Prefer a verified local install over runtime package resolution where package integrity and repeatability matter.

Risk: Ranked hypotheses can be mistaken for confirmed root cause if an agent overstates the tool output.

Mitigation: Treat hypotheses as diagnostic leads, require corroborating evidence from independent sources, and route any fix to the appropriate gated remediation skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-debug)
- [Project homepage](https://github.com/vmware-skills/VMware-Debug)
- [Agent guardrails](references/agent-guardrails.md)
- [Capabilities](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Event envelope](references/event-envelope.md)
- [Routing](references/routing.md)
- [Setup guide](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON tool and CLI outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local case ledger files under the operator's configured VMware operations directory.]

## Skill Version(s):

1.13.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
