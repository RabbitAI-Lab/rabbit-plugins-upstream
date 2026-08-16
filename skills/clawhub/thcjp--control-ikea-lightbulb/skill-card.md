## Description:

Controls IKEA and TP-Link Kasa smart bulbs for on/off state, brightness, and color adjustments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use this skill to ask an agent to control supported IKEA or TP-Link Kasa smart bulbs and return execution status or troubleshooting guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence marks the skill suspicious because it requests broad read, write, and command-execution authority for a smart-home control task.

Mitigation: Install only in an agent environment where file and command tools are constrained or manually approved, and prefer a version scoped to explicit bulb-control operations.

Risk: Smart-home control may expose credentials or enable unauthorized remote access if credentials and network access are not handled carefully.

Mitigation: Use environment-based credential handling, avoid committing secrets, restrict network access to trusted devices, and review credential handling before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/control-ikea-lightbulb)
- [Publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON status examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May request broad file and command execution authority in the agent environment.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter reports 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
