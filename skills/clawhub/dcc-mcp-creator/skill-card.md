## Description:

Infrastructure skill that guides developers and agents through creating or modernizing DCC-MCP adapters and standalone internal MCP services for DCC hosts and custom studio systems.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create or modernize DCC-MCP adapters and standalone internal MCP services, including server composition, host-thread dispatch, gateway integration, packaging, testing, and release validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide code edits and shell commands for adapter development, which may affect local projects if followed without review.

Mitigation: Review proposed edits and commands before applying them, run changes in a normal development environment, and keep production credentials out of the session.

Risk: Install and debug commands, including npx-based tools, can introduce supply-chain or credential exposure risk.

Mitigation: Pin package versions, verify provenance or hashes when available, and run debug tools in an isolated environment without production credentials.

## Reference(s):

- [DCC-MCP Creator Skill Source](https://github.com/dcc-mcp/dcc-mcp-agent-plugins/blob/main/plugins/dcc-mcp/skills/dcc-mcp-creator/SKILL.md)
- [DCC-MCP Creator on ClawHub](https://clawhub.ai/loonghao/skills/dcc-mcp-creator)
- [Adapter And Service Workflow](references/ADAPTER_WORKFLOW.md)
- [Internal Standalone Service Workflow](references/INTERNAL_SERVICE_WORKFLOW.md)
- [Host Pattern Matrix](references/HOST_PATTERN_MATRIX.md)
- [Core Escalation Checklist](references/CORE_ESCALATION_CHECKLIST.md)
- [Testing And Release](references/TESTING_AND_RELEASE.md)
- [DCC-MCP Skill](https://clawhub.ai/loonghao/skills/dcc-mcp)
- [DCC-MCP Skills Creator](https://clawhub.ai/loonghao/skills/dcc-mcp-skills-creator)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code blocks, shell commands, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose file edits and command sequences for adapter development; users should review generated changes before applying them.]

## Skill Version(s):

0.19.100 (source: server release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
