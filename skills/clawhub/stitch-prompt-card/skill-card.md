## Description:

Turns a public TikTok stitch target and an operator's written replies into a planned set of quote-reply stills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and social media teams use this skill to plan quote-reply cards from a public TikTok video or pasted comments and their own reply lines, then generate approved still images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shared Beatra device token grants broad media, task, artifact, and wallet-spend authority.

Mitigation: Review account and device revocation controls before connecting; approve each paid lookup and image request separately.

Risk: The package silently replaces its own files through automatic updates by default.

Mitigation: Disable automatic updates with the documented `update --auto off` command if you prefer to review new versions before installing them.

## Reference(s):

- [Stitch Prompt Card product page](https://beatra.ai/skills/stitch-prompt-card)
- [Stitch prompt workflow](references/workflow.md)
- [Comment lookup](references/comment-lookup.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Image artifacts]

**Output Format:** [Markdown cover plan and generated still images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans up to six quote-reply cards and reports task status and actual credits charged for approved work.]

## Skill Version(s):

0.1.8 (source: server-resolved release and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
