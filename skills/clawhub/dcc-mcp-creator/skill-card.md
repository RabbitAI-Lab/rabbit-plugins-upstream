## Description:

Guides developers and agents through creating or modernizing DCC-MCP adapters and standalone internal MCP services for DCC tools and custom studio systems.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to plan, scaffold, modernize, test, and release DCC-MCP adapters or private standalone MCP services. It helps choose host integration patterns, core escalation boundaries, dispatcher behavior, packaging, and validation steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Adapter or service guidance may propose commands that affect a local DCC runtime, package installation, or development environment.

Mitigation: Review commands before running them and validate changes in a clean test environment before release.

Risk: Internal MCP services exposed beyond loopback can introduce network, authentication, and secret-management risk.

Mitigation: Keep services on loopback until an operator owns TLS, authentication, firewall policy, secret storage, and audit controls.

Risk: Using unpinned inspection tooling can introduce unexpected package changes during validation.

Mitigation: Pin the MCP Inspector package version when reproducible validation is required.

## Reference(s):

- [DCC-MCP Creator Skill Page](https://clawhub.ai/loonghao/skills/dcc-mcp-creator)
- [Declared Homepage](https://github.com/dcc-mcp/dcc-mcp-agent-plugins/blob/main/plugins/dcc-mcp/skills/dcc-mcp-creator/SKILL.md)
- [DCC-MCP Skill](https://clawhub.ai/loonghao/skills/dcc-mcp)
- [DCC-MCP Skills Creator](https://clawhub.ai/loonghao/skills/dcc-mcp-skills-creator)
- [Adapter And Service Workflow](references/ADAPTER_WORKFLOW.md)
- [Internal Standalone Service Workflow](references/INTERNAL_SERVICE_WORKFLOW.md)
- [Host Pattern Matrix](references/HOST_PATTERN_MATRIX.md)
- [Core Escalation Checklist](references/CORE_ESCALATION_CHECKLIST.md)
- [Testing And Release](references/TESTING_AND_RELEASE.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include adapter skeletons, configuration snippets, validation commands, and operational checklists.]

## Skill Version(s):

0.19.98 (source: server release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
