## Description:

VMware Debug helps agents troubleshoot VMware, vSphere, ESXi, and NSX incidents by correlating supplied events, ranking root-cause hypotheses, and suggesting the next checks without applying fixes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and support engineers use this skill to investigate VMware incident symptoms, correlate logs and events gathered by companion tools, and decide what evidence or remediation path to pursue next.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary flags a mismatch between read-only positioning and documented persistent local case or audit writes.

Mitigation: Review before installing, set OPS_HOME to a controlled location when available, and define retention and deletion procedures for local VMware incident evidence.

Risk: The skill can store VMware incident evidence locally under case and audit paths.

Mitigation: Treat local case and audit data as sensitive operational evidence and limit access to users approved to handle the affected VMware environment.

Risk: The skill ranks hypotheses and recommends next checks, which can be mistaken for confirmed root cause.

Mitigation: Require users to distinguish observed evidence from interpretation and route any fix through the companion remediation skills' approval and audit gates.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-debug)
- [Project homepage](https://github.com/vmware-skills/VMware-Debug)
- [agent-guardrails.md](references/agent-guardrails.md)
- [capabilities.md](references/capabilities.md)
- [cli-reference.md](references/cli-reference.md)
- [event-envelope.md](references/event-envelope.md)
- [routing.md](references/routing.md)
- [setup-guide.md](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON tool outputs and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ranked hypotheses, timelines, next-check suggestions, local case ledger paths, and remediation routing recommendations.]

## Skill Version(s):

1.11.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
