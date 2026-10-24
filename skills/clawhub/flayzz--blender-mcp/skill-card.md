## Description:

Advanced bridge to Blender via MCP that allows querying scenes, creating objects, applying materials, and running custom BPY code in real time.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flayzz](https://clawhub.ai/user/flayzz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and 3D artists use this skill to connect an agent to a running Blender instance for scene inspection, object and material changes, asset import, and BPY automation with real-time feedback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bridge can execute custom BPY code and affect local Blender files, renders, downloads, and saves.

Mitigation: Use it only in a constrained Blender environment, keep sensitive files and credentials out of reach, and require explicit user approval for execute_code, downloads, saves, and renders.

Risk: The bridge starts the blender-mcp package at runtime through uvx, which can introduce supply-chain and version drift risk.

Mitigation: Pin and review the blender-mcp version before routine use, and prefer an allowlisted or sandboxed tool configuration.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/flayzz/skills/blender-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured tool-call guidance with inline code or shell snippets when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct an agent to call Blender MCP tools, execute BPY code, download scene assets, save Blender files, or render outputs.]

## Skill Version(s):

1.0.0 (source: server release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
