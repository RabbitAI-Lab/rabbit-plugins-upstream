## Description:

Yotta-learn helps agents record errors, corrections, feature requests, and reusable insights as project-local `.learnings/` entries for later review and skill improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to preserve useful lessons from command failures, user corrections, better practices, missing capability requests, and outdated knowledge. It supports local review, promotion into agent guidance files, and extraction of high-value learning entries into new skill skeletons.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Global installation and optional hook templates can make the skill available across many agent environments or run a review command automatically on every prompt.

Mitigation: Install only into the intended agent, avoid `-g` or `--global` unless broad availability is desired, and review hook templates before merging them into agent settings.

Risk: Learning entries could capture secrets, private source content, or sensitive operational details if the user or agent records them directly.

Mitigation: Record summaries or redacted snippets, and do not log tokens, keys, environment variable values, credentials, or full private source files.

Risk: The optional `--remember` path depends on a `yotta-memory` executable found in PATH.

Mitigation: Use `--remember` only when the `yotta-memory` executable is trusted; otherwise rely on local `.learnings/` records.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yottameta/skills/yotta-learn)
- [npm Package](https://www.npmjs.com/package/@yottameta/yotta-learn)
- [Recording examples and field guide](references/examples.md)
- [Hook setup guide](references/hooks-setup.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown files, CLI text output, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes project-local `.learnings/` Markdown entries and can optionally generate agent guidance updates or skill skeleton previews.]

## Skill Version(s):

0.1.2 (source: ClawHub release evidence, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
