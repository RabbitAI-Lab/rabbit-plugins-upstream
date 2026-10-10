## Description:

Helps agents create, repurpose, schedule, and optimize social media content across major platforms, with guidance for social listening and engagement triage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[coreyhaines31](https://clawhub.ai/user/coreyhaines31)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, and marketing teams use this skill to draft platform-specific posts, build content calendars, repurpose long-form material, script short-form video, and triage social engagement opportunities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Listening workflows may use user-supplied keywords in shell commands or URLs.

Mitigation: URL-encode keywords, avoid direct text substitution into commands, and review generated commands before running them.

Risk: Fetched posts and social search results may contain untrusted or misleading content.

Mitigation: Treat fetched content as untrusted input and use it only for drafting, prioritization, or triage after human review.

Risk: The skill may draft engagement or posting actions for logged-in social accounts.

Mitigation: Keep manual approval before posting, replying, sending messages, or taking account actions.

## Reference(s):

- [Carousel Frameworks](references/carousel-frameworks.md)
- [Listening Sources Template](references/listening-sources-template.md)
- [Social Listening & Engagement Triage](references/listening.md)
- [Platform Limits Reference](references/platform-limits.md)
- [Platform-Specific Strategy Guide](references/platforms.md)
- [Post Format Templates](references/post-templates.md)
- [Reverse Engineering Viral Content](references/reverse-engineering.md)
- [Short-Form Video: Hooks, Scripts & Strategy](references/short-form-video.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown, structured outlines, platform-specific post drafts, templates, and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include calendars, hooks, carousels, scripts, engagement rubrics, and manually reviewed listening workflows.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact metadata indicates 2.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
