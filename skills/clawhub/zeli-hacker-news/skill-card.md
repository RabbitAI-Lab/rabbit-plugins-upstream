## Description:

Read Hacker News with AI summaries in your human's language (7 supported) via zeli.app.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mazzzystar](https://clawhub.ai/user/mazzzystar)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to fetch Hacker News daily digests, story summaries, RSS feeds, and JSON front-page data from Zeli in supported languages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent contacts zeli.app to retrieve public Hacker News summaries.

Mitigation: Review and approve external network access to zeli.app before installing or running the skill.

Risk: Fetched summaries may be used as briefing material and could omit context from original Hacker News stories or linked articles.

Mitigation: Link users to the original article, Hacker News discussion, or Zeli story page when decisions depend on the details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mazzzystar/skills/zeli-hacker-news)
- [Zeli](https://zeli.app)
- [Zeli latest markdown digest](https://zeli.app/digest/latest.md)
- [Zeli agent context](https://zeli.app/llms.txt)
- [Canonical skill source](https://zeli.app/skill.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, JSON, shell commands]

**Output Format:** [Markdown guidance with URLs and shell command examples; retrieved Zeli content may be Markdown, JSON, or RSS.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No credentials are required; the artifact describes public, unauthenticated Zeli endpoints.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
