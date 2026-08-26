## Description:

Extends an agent with Gemini Web for second opinions, current web lookup, multimodal understanding, Deep Research, artifact generation, and explicit account workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luckycat133](https://clawhub.ai/user/luckycat133)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to route Gemini Web tasks through the narrowest appropriate capability lane, including assistance, web research, file or image understanding, media generation, and explicitly requested account workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated Gemini Web use may involve account cookies and may send selected prompts, local files, URLs, or reference media to Gemini.

Mitigation: Use the narrowest server profile for the requested task, require explicit user approval for browser cookie export, and avoid logging, sharing, or retaining cookie values.

Risk: Explicit account workflows can read or change Gemini history, scheduled actions, notebooks, Gems, or related account data.

Mitigation: Run account workflows only for explicit user requests, start with read-only identification, and require positive read-back before claiming a mutation or deletion succeeded.

Risk: Deep Research, video, music, and generated artifacts can remain queued, time out, or be partially available.

Mitigation: Preserve operation and upstream identifiers, resume rather than duplicate long operations, and verify artifact state, path, type, and size before treating output as complete.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/luckycat133/skills/gemini-web-mcp)
- [Gemini Web MCP Homepage](https://github.com/Luckycat133/gemini-web-mcp)
- [Task Workflows](references/workflows.md)
- [Artifact Acceptance and Handoff](references/artifacts.md)
- [Long Operations](references/operations.md)
- [Recovery Playbook](references/recovery.md)
- [Gemini Web Tool Surface Reference](references/tool_surface.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with structured tool and artifact handling details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or reference Gemini Web artifacts and operation handles when the selected workflow creates media, files, or long-running research.]

## Skill Version(s):

0.2.1 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
