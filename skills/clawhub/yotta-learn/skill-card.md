## Description:

元习 yotta-learn helps agents capture mistakes, corrections, and insights as reusable learning entries across sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users record and review lessons from failures, corrections, and better practices, then optionally promote useful lessons into agent guidance or new skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent learning entries could retain sensitive content or later be promoted or synced.

Mitigation: Redact credentials and private information before recording; review entries before promoting or explicitly syncing them.

Risk: Optional hooks can add review reminders to each prompt event.

Mitigation: Enable hooks only when those reminders are wanted.

Risk: Installing an unpinned release could run a version that was not reviewed.

Mitigation: Install a trusted, pinned version rather than the latest npx release.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yottameta/skills/yotta-learn)
- [Project homepage](https://github.com/YottaMeta/yotta-learn)
- [Learning entry examples](references/examples.md)
- [Hook setup guide](references/hooks-setup.md)
- [Usage walkthroughs](references/walkthroughs.md)
- [Frequently asked questions](references/faq.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Code, Configuration]

**Output Format:** [Markdown learning entries and agent guidance; optional skill scaffolds and configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Entries persist across sessions; promotion and syncing require explicit action.]

## Skill Version(s):

0.2.2 (source: ClawHub release, skill frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
