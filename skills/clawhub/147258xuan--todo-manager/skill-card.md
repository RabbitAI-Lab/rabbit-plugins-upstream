## Description:

Scan workspace files for TODO/FIXME/HACK comments, list them with context, and optionally sync to a local task file. Use when you need to track code TODOs or audit outstanding work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[147258xuan](https://clawhub.ai/user/147258xuan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to scan workspace source files for TODO, FIXME, HACK, and XXX comments, review findings with their locations and context, and summarize or filter outstanding work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan flags an unexplained health check and automatic saving of TODO findings; the scan was partial.

Mitigation: Clarify the health-check behavior, inspect the remaining unassessed components, and require an explicit choice before writing findings to a file.

## Reference(s):

- [ClawHub todo-manager release](https://clawhub.ai/147258xuan/skills/todo-manager)
- [Publisher profile: 147258xuan](https://clawhub.ai/user/147258xuan)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Plain-text reports and JSON findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include file path, line, column, tag, matched text, and context.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
