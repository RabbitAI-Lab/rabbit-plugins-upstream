## Description:

A Codex Canvas is a live React app that the user can open beside the chat for standalone analytical artifacts, visual layouts, charts, tables, interactive explorations, repeatable tools, and `.canvas.tsx` authoring or debugging.

This skill is ready for commercial/non-commercial use.

## Publisher:

[eohmig](https://clawhub.ai/user/eohmig)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill to decide when a standalone Canvas is appropriate and to create a single `.canvas.tsx` React artifact using Cursor's canvas SDK. It is intended for analytical outputs, structured findings, charts, tables, and interactive tools that are clearer beside the chat than in plain Markdown.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Canvas files may store source analysis data inline in local `.canvas.tsx` artifacts.

Mitigation: Avoid using the skill for sensitive data that should not be stored in local artifact files; review generated canvases before sharing or retaining them.

Risk: The skill directs agents to write local Canvas files in Cursor's managed canvas directory.

Mitigation: Review proposed canvas content and destination before relying on generated artifacts in a workspace.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/eohmig/skills/canvas)
- [Publisher profile](https://clawhub.ai/user/eohmig)

## Skill Output:

**Output Type(s):** [code, markdown, guidance]

**Output Format:** [A single `.canvas.tsx` React file plus concise Markdown chat links when a canvas is created.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Canvas source data is embedded inline; the artifact instructions prohibit fetch calls, network calls, extra helper files, relative imports, npm packages, and Node built-ins.]

## Skill Version(s):

1.0.0 (source: server release metadata, released 2026-09-19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
