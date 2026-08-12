## Description:

GitHub订阅 helps agents fetch GitHub Trending repository lists, optionally filtered by programming language, and format the results for developer workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation teams use this skill to retrieve GitHub Trending repositories, apply an optional language filter, and produce shareable feed-style summaries for chat, console, or workflow updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags broad read/write/exec-capable instructions and unrelated automation, private repository, and command-execution claims for a skill presented as a GitHub Trending feed.

Mitigation: Review before installing, restrict use to public GitHub Trending retrieval, and avoid private repository access or command execution unless a reviewed version clearly requires and constrains it.

Risk: The artifact documents generic API key setup even though the server security guidance recommends a narrower public GitHub Trending retrieval posture.

Mitigation: Do not provide secrets unless they are required by a reviewed implementation, and prefer a release with a concrete script path and minimal permissions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/github-trending-feed)
- [SkillHub skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with JSON result examples and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include language-filtered repository entries with repository names, descriptions, star counts, languages, and URLs when available.]

## Skill Version(s):

1.0.1 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
