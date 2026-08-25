## Description:

Miao Vision creates local-first article infographics, HTML/PDF reports, static dashboards, browser decks, recurring report updates, and report or deck spec validation artifacts from user-provided URLs, Markdown, text, or local structured data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[miaoshou.dev](https://clawhub.ai/user/miaoshou.dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and business users use this skill to turn local data, article content, or existing Miao Vision specs into grounded visual reports, browser decks, infographics, and validation outputs. The skill is intended for explicit Miao Vision requests where local execution and artifact generation are acceptable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or use a local Miao Vision CLI binary when no compatible CLI is already present.

Mitigation: Approve installation only when the prompt points to the expected Miao Vision release, rely on the checksum-verifying installer, and remove ~/.miao-vision if the shared CLI should be deleted.

Risk: The skill executes local shell commands and reads user-provided files or article URLs to create artifacts.

Mitigation: Use the skill only for explicit Miao Vision requests, limit inputs to intended source files or URLs, and review generated artifacts before sharing.

## Reference(s):

- [Article Infographic Workflow](artifact/references/article.md)
- [Data Report Workflow](artifact/references/report.md)
- [Browser Deck Workflow](artifact/references/deck.md)
- [Outcome Brief Plan-First Workflow](artifact/references/outcome-brief.md)
- [Miao Vision ClawHub Skill Page](https://clawhub.ai/miaoshou.dev/skills/miao-vision-skill)

## Skill Output:

**Output Type(s):** [Files, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and generated local HTML, PDF, PNG, YAML, or JSON artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Artifacts are created locally in a per-task Miao Vision delivery directory unless the user names another output location.]

## Skill Version(s):

0.6.0 (source: release evidence and cli-compatibility.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
