## Description:

A local-first Instagram content system for hooks, captions, content structure, and draft storage that optimizes stop-rate and retention without API connection, auto-posting, or automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticio](https://clawhub.ai/user/agenticio)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and social media operators use this skill to improve Instagram hooks, captions, carousel structure, CTAs, and account-level content strategy while keeping publishing under manual control.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved captions may persist sensitive draft content in the local OpenClaw workspace memory directory.

Mitigation: Use chat-only rewrites when persistence is not needed, and review or remove locally saved drafts according to workspace retention practices.

Risk: Aggressive auto-routing could invoke the skill for broad Instagram-related prompts when the user only wants general discussion.

Mitigation: Narrow triggers or require explicit save and optimization requests in environments that route skills automatically.

Risk: Content recommendations could become spam-like, over-promotional, or misaligned with the user's account voice.

Mitigation: Use the skill's friction check and manual review before publishing any generated caption, CTA, or strategy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/agenticio/skills/instagram)
- [README](artifact/README.md)
- [Examples](artifact/examples.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown responses with structured sections and optional shell command usage for local draft persistence]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save finalized captions locally only when persistence is requested.]

## Skill Version(s):

2.1.1 (source: frontmatter, skill.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
