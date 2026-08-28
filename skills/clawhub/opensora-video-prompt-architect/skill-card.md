## Description:

Turn rough video ideas into structured OpenSora prompt packs, reference-aware motion instructions, shot plans, and focused debugging loops.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gpt-img-2](https://clawhub.ai/user/gpt-img-2)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, product teams, and developers use this skill to turn rough text, image, or video concepts into concise OpenSora-style prompts, shot plans, reference constraints, and revision guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional MCP setup runs a referenced GitHub package through npx.

Mitigation: Use the text-only workflow by default, and add the MCP server only after reviewing the package source and accepting the local execution risk.

Risk: Users may mistake OpenSora2.com guidance for official Open-Sora project documentation.

Mitigation: Present the site and skill as an independent OpenSora 2 resource, and avoid claims about official model behavior unless verified in the product interface.

Risk: Prompt or shot-plan guidance can still produce misleading or low-quality video instructions if user constraints are underspecified.

Mitigation: Ask only for missing details that materially affect the result, keep each shot to one visible action, and revise one variable at a time when debugging.

## Reference(s):

- [Prompt guide](https://opensora2.com/blog/opensora-2-prompt-guide)
- [Free prompt examples](https://opensora2.com/free-ai-video-prompts)
- [Generator workspace](https://opensora2.com/generator)
- [Text-to-video workflow](https://opensora2.com/text-to-video)
- [Image-to-video workflow](https://opensora2.com/image-to-video)
- [Video-to-video workflow](https://opensora2.com/video-to-video)
- [Raw skill](https://opensora2.com/skills/opensora-video-prompt-architect/SKILL.md)
- [MCP source](https://github.com/gpt-img-2/opensora2-prompt-mcp)
- [ClawHub listing](https://clawhub.ai/gpt-img-2/skills/opensora-video-prompt-architect)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with concise prompt sections, numbered shot plans, avoid lists, and optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces text-only planning artifacts by default; optional MCP helpers are read-only and do not generate video or spend credits.]

## Skill Version(s):

1.0.0 (source: server release evidence and OpenClaw metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
