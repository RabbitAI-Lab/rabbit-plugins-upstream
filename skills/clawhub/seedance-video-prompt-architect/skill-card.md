## Description:

Turn rough creative briefs into structured Seedance video prompt packs, reference-aware motion plans, focused variants, and debugging loops.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gpt-img-2](https://clawhub.ai/user/gpt-img-2)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and developers use this skill to turn rough Seedance video ideas into structured prompt packs, reference-aware motion plans, variants, and debugging steps. It supports text-to-video, image-to-video, video-to-video, first-last-frame transitions, and multi-shot storyboard planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional C Dance Prompt MCP runs a referenced GitHub/npx package outside the core text-only workflow.

Mitigation: Use the skill without the MCP unless public prompt lookup is needed, and add the MCP only after reviewing and accepting that package.

Risk: The skill produces prompt guidance and does not generate final video output or spend generation credits.

Mitigation: Treat outputs as prompt drafts for review, then use a separate trusted video generation capability when final video creation is required.

## Reference(s):

- [C Dance Seedance Prompt Architect Docs](https://cdance.ai/docs/seedance-video-prompt-architect)
- [C Dance Seedance 2.0 Prompt Gallery](https://cdance.ai/prompts/seedance-2-0)
- [Seedance 2.0 Prompt Examples](https://cdance.ai/blog/best-seedance-2-0-prompt-examples)
- [Seedance Prompt Debugging Guide](https://cdance.ai/blog/common-seedance-2-0-prompt-mistakes)
- [Optional C Dance Prompt MCP](https://github.com/gpt-img-2/cdance-prompt-mcp)
- [ClawHub Skill Listing](https://clawhub.ai/gpt-img-2/skills/seedance-video-prompt-architect)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown prompt packs with occasional inline shell commands for optional MCP setup]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes primary prompts, focused variants, avoid lists, revision moves, and reference-aware motion guidance.]

## Skill Version(s):

1.1.0 (source: OpenClaw metadata and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
