## Description:

Guides operators through read-only discovery of AWS-hosted AI agent and workload assets, writing canonical inventory JSON for optional local scanning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inventory AWS agent and MCP-related assets with an approved read-only role. They can optionally scan or export the resulting inventory after choosing the scope and destination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad AWS permissions could expose more cloud metadata than needed.

Mitigation: Use an operator-approved, least-privilege read-only role or profile and limit the account, region, and services.

Risk: Generated inventory may contain sensitive cloud metadata that could be shared or retained unintentionally.

Mitigation: Choose the output path deliberately, review the inventory before sharing, and approve scans, exports, or handoffs only after confirming the destination and retained evidence.

## Reference(s):

- [agent-bom project (skill metadata)](https://github.com/msaad00/agent-bom)
- [agent-bom on PyPI (skill metadata)](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files]

**Output Format:** [Markdown instructions and shell commands; optional canonical inventory JSON file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Inventory is written to an operator-selected path; scanning and export are optional.]

## Skill Version(s):

0.107.0 (source: ClawHub release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
