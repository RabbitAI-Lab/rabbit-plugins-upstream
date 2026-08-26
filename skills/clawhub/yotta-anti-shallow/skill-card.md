## Description:

元谨 yotta-anti-shallow is a rule-based agent skill that activates for deep analysis, validation, root-cause investigation, and complex tasks to require analysis before execution and self-checks after completion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers, writers, analysts, and other agent users use this skill to make an agent slow down on complex or high-accuracy work, state uncertainty, analyze before acting, and report self-checks after completion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Global installation can place the skill in multiple agent directories, causing its response process to apply more broadly than intended.

Mitigation: Use a specific --dir or --agent install when only one agent should load the skill, and uninstall by deleting the yotta-anti-shallow folder from the relevant skill directories.

Risk: The skill can add analysis, confirmation, and self-check steps to complex tasks where a user expects a direct answer.

Mitigation: Use the documented pause or direct-instruction controls for sessions where the process rule should not apply, while preserving its non-guessing and stop-handling safeguards.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-anti-shallow)
- [npm package @yottameta/yotta-anti-shallow](https://www.npmjs.com/package/@yottameta/yotta-anti-shallow)
- [Agent Skills standard](https://agentskills.io/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown instructions and process guidance with optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill changes agent response process; installer scripts may copy the skill folder into selected agent skill directories.]

## Skill Version(s):

1.3.2 (source: server release, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
