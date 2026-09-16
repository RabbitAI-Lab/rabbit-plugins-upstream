## Description:

iaiops-fab helps agents support semiconductor and display fab equipment diagnostics across SECS/GEM, OPC-UA, and related industrial protocols with read-first workflows and MOC-gated writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and fab automation engineers use this skill to inspect fab equipment status, alarms, variables, data quality, downtime causes, OEE, asset inventory, and readiness across SECS/GEM, OPC-UA, and related industrial systems. It is intended for read-first diagnosis, with production writes gated through management-of-change controls when write tools are exposed by the runtime.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags the runtime installation path as unverifiable and unpinned for high-impact industrial systems.

Mitigation: Require a pinned, provenance-verified package version with hashes or a lockfile before use.

Risk: Fab-connected environments can expose production equipment and process-control paths.

Mitigation: Run under a least-privilege account and isolate the skill from production write paths until MOC controls are independently verified.

Risk: Operator misunderstanding of approval flow could lead to unsafe production changes when write-capable tools are available.

Mitigation: Confirm operators understand the instructions, require named approval, keep dry-run behavior enabled by default, and verify undo information before any write.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-fab)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Analysis]

**Output Format:** [Markdown guidance with inline shell commands, tool names, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-first operational guidance; production writes require MOC approval and dry-run controls when exposed by underlying tools.]

## Skill Version(s):

0.28.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
