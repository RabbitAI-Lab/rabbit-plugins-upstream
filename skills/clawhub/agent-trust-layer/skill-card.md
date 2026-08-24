## Description:

Agent Trust Layer is a rule-based discriminator that checks AI inputs and outputs for truthfulness, safety, honesty, manipulation, contradictions, confidence issues, and related quality signals without an LLM dependency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yun520-1](https://clawhub.ai/user/yun520-1)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent builders use this skill to add rule-based checks that classify AI inputs, drafts, or outputs as pass, verify, rewrite, or block before content reaches users or downstream tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags under-disclosed local MCP service behavior.

Mitigation: Bind the MCP service to localhost, set the MCP token explicitly, and review local configuration before enabling integrations.

Risk: The security evidence flags local state retention through data, audit, feedback, or memory files.

Mitigation: Review generated local state files after use and disable memory with HEARTFLOW_MEMORY=off when retention is not needed.

Risk: The security evidence flags optional process-management behavior through the daemon.

Mitigation: Avoid the daemon unless a persistent background process is required and monitor the process lifecycle when enabled.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yun520-1/skills/agent-trust-layer)
- [Skill definition](artifact/SKILL.md)
- [README](artifact/README.md)
- [Security advisory](artifact/SECURITY.md)
- [Evaluation report](artifact/docs/eval-report-2026-08-17.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline JavaScript and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include gate actions, findings, and setup instructions for local use.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata; artifact source declares 6.6.1 in SKILL.md and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
