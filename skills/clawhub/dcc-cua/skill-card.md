## Description:

Routes authorized application UI tasks through DCC-CUA, with exact target binding and verified outcomes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can direct an agent to control a specified application window, including DCC hosts, browsers, and desktop apps, using scoped authorization and verified UI actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: UI control can observe or act on sensitive application or account content.

Mitigation: Review prompts, bind only the intended window, and keep sensitive browser and account actions human-controlled.

Risk: Component installation or repair may change the local UI-control runtime.

Mitigation: Authorize installation or repair only when expected and required for the task.

## Reference(s):

- [DCC-CUA on ClawHub](https://clawhub.ai/loonghao/skills/dcc-cua)
- [DCC-CUA skill homepage](https://github.com/dcc-mcp/dcc-mcp-agent-plugins/blob/main/plugins/dcc-mcp/skills/dcc-cua/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the bound target and verified outcome or a concrete blocker.]

## Skill Version(s):

0.19.113 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
