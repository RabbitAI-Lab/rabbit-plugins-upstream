## Description:

Provides a Chinese-language helper for fetching GitHub Trending repositories, optionally filtering by language, and returning repository data for agent-formatted updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to request GitHub Trending repository lists, apply optional language filters, and format results for chat, console, or workflow notifications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documentation asks for broad execution/write authority without a concrete implementation or clear permission boundaries.

Mitigation: Install with least privilege and do not grant broad exec/write access unless the publisher supplies exact commands, implementation details, and bounded permissions.

Risk: The skill may produce incorrect or misleading GitHub Trending output because the implementation path and command examples are inconsistent.

Mitigation: Run in a sandbox first and verify returned repository data against public GitHub sources before using the output in automated workflows.

Risk: Granting API keys or private repository permissions could expose sensitive account or repository data.

Mitigation: Use public, unauthenticated access where possible and avoid providing API keys, tokens, or private repository access unless a reviewed implementation demonstrates a specific need.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/github-trending-feed)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with JSON examples and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include repository names, descriptions, languages, star counts, URLs, and language-filtered results when available.]

## Skill Version(s):

1.0.2 (source: evidence release metadata; artifact frontmatter lists 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
