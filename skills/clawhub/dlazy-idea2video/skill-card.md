## Description:

Turns a user's idea into a staged video-production plan covering story, characters, scene and shot planning, keyframes, generated shot videos, and final concatenation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to gather video requirements, generate a reviewable idea-to-video plan, expand it into canvas workflow nodes, and apply the plan to a canvas for model-backed video generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses the dLazy CLI with a stored or environment-provided API key and may send prompts or referenced media to dLazy services.

Mitigation: Install only when that data flow is acceptable, use a dedicated revocable API key, review prompts and media before execution, and rotate or revoke keys when needed.

Risk: The skill mixes a reviewable canvas-planning workflow with direct authenticated terminal execution.

Mitigation: Keep direct CLI generation explicitly opt-in, review the generated plan before execution, and scope command execution to the requested video-generation task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-idea2video)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with inline shell commands and structured canvas planning guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user confirmation before plan expansion and before direct generation commands]

## Skill Version(s):

1.3.11 (source: server release metadata; artifact frontmatter reports 1.3.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
