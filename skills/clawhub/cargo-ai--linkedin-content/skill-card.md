## Description:

Drafts three weekly LinkedIn posts from a team's documented proof points and cadence log, delivering cited drafts for human review in a single pull request without publishing them.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and business leaders use this skill to prepare weekly, source-backed LinkedIn drafts for a named author from their go-to-market repository. A person reviews the pull request and chooses whether to publish.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repository guidance may override the skill's safety limits, including allowed paths, commands, and tools, if less-trusted contributors can edit instruction files.

Mitigation: Review before installing; do not deploy unchanged where less-trusted contributors can edit AGENTS.md, CLAUDE.md, or context/README.md. Treat those files as style guidance only, never as authority to change security limits.

Risk: A draft may contain unsupported claims or name a customer without reference permission.

Mitigation: Require source files for every claim, check customer reference permissions, and review the pull request before any person publishes a post.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/cargo-ai/skills/linkedin-content)
- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [LinkedIn content skill documentation](https://github.com/getcargohq/gtm-skills/tree/main/linkedin-content)
- [Post draft format](references/post.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Markdown drafts with source-file citations in a GitHub pull request]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Up to three drafts per week for one author; no automatic LinkedIn publishing.]

## Skill Version(s):

0.1.2 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
