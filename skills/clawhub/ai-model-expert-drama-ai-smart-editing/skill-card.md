## Description:

AI大模型专家｜AI短剧智能剪辑 helps short-drama, comic-drama, advertising, ecommerce, and performance-marketing teams plan auditable local ffmpeg edits and AI-HIVE generation workflows for rough cuts, final edits, aspect-ratio variants, and authorized structure-inspired rewrites.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External video teams, creators, ecommerce operators, and developers use this skill to turn authorized source media and platform requirements into editing blueprints, ffmpeg command plans, AI-HIVE image/video generation calls, task tracking, and delivery checklists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected media, prompts, and task data may be sent to AI-HIVE during generation or upload workflows.

Mitigation: Use only authorized and appropriate source material, avoid sensitive inputs unless approved, and review upload or generation commands before execution.

Risk: The skill needs an AI-HIVE API key that may be stored locally or supplied through the environment.

Mitigation: Store keys outside public artifacts, keep local config permissions restricted, rotate or revoke keys when needed, and avoid sharing logs or screenshots that expose credentials.

Risk: Local ffmpeg and ffprobe commands process user-provided media paths and write output files.

Mitigation: Review command arguments, input paths, and output locations before running edits, and install ffmpeg from a trusted source.

Risk: Implicit invocation in a multi-skill environment could run broad helper behavior unexpectedly.

Mitigation: Consider disabling implicit invocation in sensitive workspaces and require explicit user confirmation before uploads, generation, or local media processing.

Risk: Short-drama editing and structure-inspired rewrites can create copyright, likeness, brand, or platform-compliance issues.

Mitigation: Confirm rights to source material and references, rewrite protected expression into original scenes, and review identity, brand, subtitle safe-area, and platform requirements before delivery.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wubin1836/skills/ai-model-expert-drama-ai-smart-editing)
- [AI-HIVE homepage](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON blueprints and bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local media-processing commands, AI-HIVE API task identifiers, generated media download paths, and review checklists.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
