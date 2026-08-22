## Description:

Converts rambling or disorganized user ideas into clear, structured, actionable prompts for coding, content, planning, or general tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[blackcorvu](https://clawhub.ai/user/blackcorvu)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to turn fragmented brainstorming into a structured prompt before asking an agent or person to execute the work. It is especially useful when the original request mixes multiple goals, has missing constraints, or needs a task-specific prompt template.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation phrases may trigger during general brainstorming or loosely organized requests.

Mitigation: Tighten trigger phrases or scope activation when deploying in environments that need narrower behavior.

Risk: The artifact is written primarily in Chinese and may default to Chinese-facing structure or wording.

Mitigation: Adapt the skill language and examples for the deployment audience before installation when a different language is required.

Risk: A generated prompt may carry forward incorrect assumptions from an ambiguous user idea.

Mitigation: Review the structured prompt and answer any clarifying questions before using it to drive follow-on work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/blackcorvu/skills/idea-to-prompt)
- [README.md](README.md)
- [SKILL.md](SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown structured prompt or 1-3 targeted clarifying questions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include assumptions and category-specific sections; does not execute follow-on tasks unless explicitly requested.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
