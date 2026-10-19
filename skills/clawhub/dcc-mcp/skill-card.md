## Description:

Operates named supported applications through DCC-MCP and helps discover tools and marketplace skills for application tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Creative professionals and developers use this skill to discover application tools, perform authorized work in supported software, and verify the resulting scene, document, or artifact.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Application control can change the wrong project or document.

Mitigation: Confirm the named application, target project, and operation before approving launches or UI control; verify the result afterward.

Risk: Setup and marketplace actions can install or replace local components.

Mitigation: Require consent before downloads or installs and use the documented verified release flow.

Risk: Gateway operations can expose project data to an unintended destination.

Mitigation: Use a local or explicitly approved gateway and send only the project data needed for the task.

Risk: Ambiguous Office or spreadsheet requests can trigger unintended application actions.

Mitigation: Clarify the application and intended operation before authorizing those actions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/loonghao/skills/dcc-mcp)
- [Skill homepage listed in metadata](https://github.com/dcc-mcp/dcc-mcp-agent-plugins/blob/main/plugins/dcc-mcp/skills/dcc-mcp/SKILL.md)
- [First-run environment guidance](artifact/references/FIRST_RUN.md)
- [Application UI workflows](artifact/references/UI_WORKFLOWS.md)
- [Gateway profiles](artifact/references/GATEWAY_PROFILES.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Code]

**Output Format:** [Markdown with commands and structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide changes to local application scenes, documents, and project files.]

## Skill Version(s):

0.19.113 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
