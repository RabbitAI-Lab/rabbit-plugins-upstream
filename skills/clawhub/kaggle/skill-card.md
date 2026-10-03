## Description:

Helps coding agents research Kaggle competitions and work with Kaggle datasets, models, notebooks, discussions, benchmarks, and badges.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shepsci](https://clawhub.ai/user/shepsci)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use it to investigate Kaggle competitions, retrieve data and writeups, and manage submissions, notebooks, datasets, and models with user approval for account changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Direct badge automation can change a Kaggle account without the main command's dry-run, confirmation, or read-only safeguards.

Mitigation: Prefer the top-level skill commands, review a dry run before approving writes, and avoid running the badge orchestrator directly for mutating phases unless its exact account actions have been reviewed.

Risk: Account-changing operations can use Kaggle credentials and consume submission slots or notebook quota.

Mitigation: Grant account access only when needed; keep KAGGLE_SKILL_READ_ONLY=1 for read-only use and confirm expected account effects and costs before writes.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/shepsci/skills/kaggle)
- [Project homepage listed in skill metadata (not verified import provenance)](https://github.com/shepsci/kaggle-skill)
- [Kaggle MCP](https://www.kaggle.com/mcp)
- [Skill CLI reference](modules/references/cli-reference.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown and text with commands or code when appropriate]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some operations require Kaggle credentials; account-changing actions require explicit review and confirmation.]

## Skill Version(s):

3.0.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
