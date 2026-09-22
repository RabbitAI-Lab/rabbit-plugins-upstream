## Description:

Generates game asset and game development guidance with CellCog-focused prompts for character-consistent art, sprites, tilesets, and game concepts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, independent game creators, and teams use this skill to draft game art prompts, sprite and tileset specifications, character concepts, and related game development outputs. It is intended for asset-generation workflows where the user can review and refine the generated content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security summary rates the skill as suspicious because it asks for broad write and command-execution capability for a game-asset helper.

Mitigation: Review the skill before installation, run it only in a sandboxed or approval-controlled agent environment, and restrict command execution and file writes to the current project.

Risk: The security guidance warns against giving the skill sensitive project files or secrets.

Mitigation: Avoid sharing credentials, private assets, or confidential files unless the runtime provides clear approval controls and the user has confirmed the need.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/game-asset-generation-cellcog)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-like structured responses with optional code or shell snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read and write project files or propose command execution when the agent runtime permits those actions.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
