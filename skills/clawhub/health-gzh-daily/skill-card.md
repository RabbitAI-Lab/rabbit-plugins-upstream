## Description:

This skill helps authors draft daily Chinese WeChat health articles over 2,000 Chinese characters, rotate title and opening patterns, check for duplicated angles and platform compliance issues, generate inline-styled HTML, and update a local article library.

This skill is ready for commercial/non-commercial use.

## Publisher:

[meimei-shoulu](https://clawhub.ai/user/meimei-shoulu)

### License/Terms of Use:

MIT-0

## Use Case:

External content creators and operators of Chinese health or wellness WeChat accounts use this skill to produce daily long-form article drafts, run angle and compliance checks, prepare inline-styled HTML, and archive the finished article locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Health articles may contain inaccurate medical guidance, implied treatment promises, or platform compliance issues.

Mitigation: Review health claims and compliance wording before publishing; remove treatment guarantees, extreme advertising claims, fabricated medical credentials, and direct personal-contact redirects.

Risk: The local archive workflow reads article files and writes or updates an HTML article library.

Mitigation: Provide only article directories and files the agent is allowed to read and update, and keep backups of the article library before running the archive command.

Risk: Repeated templates can produce similar articles or repeated health angles over time.

Mitigation: Use the skill's angle-first workflow and recent-article checks to rotate title patterns, openings, symptoms, causes, and recommendations before archiving or publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/meimei-shoulu/skills/health-gzh-daily)

## Skill Output:

**Output Type(s):** [Markdown, HTML, Shell commands, Guidance, Files]

**Output Format:** [Markdown article drafts, inline-styled HTML, shell command snippets, and local HTML library updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The archive script reads a local Markdown article and writes or updates a local HTML article library.]

## Skill Version(s):

1.2.0 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
