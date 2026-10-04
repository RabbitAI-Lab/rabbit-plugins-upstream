## Description:

Routes authorized application UI tasks through DCC-CUA, with exact target binding and verification of the final state.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to control an explicitly authorized DCC application, browser, or other desktop UI through DCC-CUA when direct application tools cannot complete the task.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: UI actions can click, type, and change application state beyond what the user intended.

Mitigation: Grant access only for intended tasks and windows; bind the exact process and window, use a scoped task grant, and verify the resulting state.

Risk: A stale observation or changed window could direct input to the wrong target.

Mitigation: Require a fresh observation before state-dependent actions and stop if the target binding or verification fails.

## Reference(s):

- [ClawHub DCC-CUA release](https://clawhub.ai/loonghao/skills/dcc-cua)
- [DCC-CUA skill homepage (release metadata)](https://github.com/dcc-mcp/dcc-mcp-agent-plugins/blob/main/plugins/dcc-mcp/skills/dcc-cua/SKILL.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown with command examples and status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports exact target binding and verified outcome or a concrete blocker.]

## Skill Version(s):

0.19.107 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
