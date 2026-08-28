## Description:

Turn rough video ideas into structured English or Chinese prompt packs, reference-aware sequences, continuity rules, and focused debugging loops.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gpt-img-2](https://clawhub.ai/user/gpt-img-2)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, developers, and media teams use this skill to convert rough video concepts into structured prompts, reference-aware shot plans, continuity constraints, avoid lists, and focused revision guidance for text-to-video, image-to-video, reference-to-video, and video-to-video workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional MCP installation runs a GitHub-hosted npx package and changes MCP configuration.

Mitigation: Use the skill manually when supply-chain controls are strict, or review and pin the optional MCP source before enabling it.

Risk: The skill can produce prompts that imply unsupported provider settings or model behavior if exact interface details are assumed.

Mitigation: Confirm exact model settings, input support, prices, and availability in the current product interface before relying on them.

Risk: Prompt outputs may still contain creative ambiguity that leads to unwanted video artifacts or continuity drift.

Mitigation: Revise one axis at a time and keep reference roles, continuity constraints, and avoid lists explicit.

## Reference(s):

- [SeeVido AI Video Generator](https://seevido.org/ai-video-generator)
- [SeeVido Models](https://seevido.org/models)
- [Seedance Model Page](https://seevido.org/models/seedance)
- [Kling Model Page](https://seevido.org/models/kling)
- [Wan Model Page](https://seevido.org/models/wan)
- [SeeVido Prompt Library](https://seevido.org/seedance-2-0-prompts)
- [SeeVido Video-to-Prompt Tool](https://seevido.org/video-to-seedance-prompt)
- [Raw Skill](https://seevido.org/skills/seevido-video-prompt-architect/SKILL.md)
- [ClawHub Listing](https://clawhub.ai/gpt-img-2/skills/seevido-video-prompt-architect)
- [Optional MCP Source](https://github.com/gpt-img-2/seevido-prompt-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with optional inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include prompt packs, reference roles, continuity constraints, avoid lists, numbered shot plans, revision moves, and optional MCP setup commands.]

## Skill Version(s):

1.0.0 (source: release evidence and openclaw metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
