## Description:

Invoked ONLY by the user with /dont-edit when they want read-only mode activated.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tobiaswestholm](https://clawhub.ai/user/tobiaswestholm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users invoke this skill when they want the agent to inspect a workspace and provide advice without making file changes until explicitly approved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is an instruction layer and may not technically prevent every file-changing action.

Mitigation: Review the agent's proposed changes before granting approval, and only approve file modifications you intend to allow.

Risk: Read-only mode can delay legitimate edits if it remains active during implementation work.

Mitigation: Use the skill only when advisory review is desired, then explicitly approve or switch modes before requesting edits.

## Reference(s):

- [Source repository](https://github.com/TobiasWestholm/dont-edit)
- [ClawHub skill page](https://clawhub.ai/tobiaswestholm/skills/dont-edit)

## Skill Output:

**Output Type(s):** [guidance, text, markdown]

**Output Format:** [Markdown guidance and proposed changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only advisory responses; file changes require explicit user approval.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
