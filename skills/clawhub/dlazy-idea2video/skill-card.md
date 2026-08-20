## Description:

Turns a user's idea into a staged video-production workflow that gathers requirements, creates a reviewable plan, expands it into canvas shapes, and can invoke dLazy CLI/cloud services to generate media.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and developers use this skill to turn an idea into a reviewable video production plan, then expand it into canvas nodes for story, characters, keyframes, shot videos, and final concatenation. It is intended for users comfortable with dLazy cloud generation and CLI execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill mixes canvas-review planning with direct terminal generation, which can make it unclear when commands will run.

Mitigation: Confirm whether the user wants canvas-only planning or direct CLI generation before invoking commands, and require explicit confirmation before generation.

Risk: Using the dLazy CLI can send prompts and selected media files to dLazy services.

Mitigation: Use the skill only when cloud processing by dLazy is acceptable, and avoid submitting sensitive prompts or media.

Risk: The workflow may install or run a third-party CLI and store a local API key.

Mitigation: Review the pinned CLI package before use, prefer scoped credentials, and rotate or revoke the dLazy API key when access is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-idea2video)
- [dLazy CLI metadata link](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with structured plan summaries, canvas-shape instructions, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require dLazy CLI authentication and sends prompts or selected media to dLazy services when direct generation is used.]

## Skill Version(s):

1.3.12 (source: server release evidence; artifact frontmatter reports 1.3.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
