## Description:

Hacker News (news.ycombinator.com). Use this skill for ANY Hacker News request -- searching and reading data. Whenever a task involves Hacker News, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search and read public Hacker News content, including stories, items, comments, updates, and public user profiles, through OOMOL-connected Hacker News actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that could execute arbitrary code if followed.

Mitigation: Review installer source before execution and prefer a verified, pinned, or package-manager installation path for the OOMOL CLI.

Risk: Hacker News queries are routed through the OOMOL connector rather than directly to Hacker News APIs.

Mitigation: Confirm that routing public Hacker News requests through OOMOL is acceptable for the intended environment before use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-hackernews)
- [Hacker News](https://news.ycombinator.com)
- [OOMOL CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas and returns connector responses as JSON when actions are run.]

## Skill Version(s):

1.0.3 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
