## Description:

Self-Learning Skill Publisher helps publish local skills to the ClawHub marketplace, apply quality checks, handle known publishing errors, and record publish outcomes for future retries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill publishers use this skill to publish one or more local ClawHub skills, check required skill metadata, resolve common publishing failures, and produce a publish summary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install the ClawHub CLI globally.

Mitigation: Require explicit user confirmation before any package installation and run in an environment where global tool changes are acceptable.

Risk: The skill can patch installed ClawHub CLI JavaScript files.

Mitigation: Review the exact patch before applying it and keep a clean way to reinstall or restore the CLI.

Risk: The skill can write persistent local learning and publish history files.

Mitigation: Store only non-sensitive publish diagnostics and periodically review or delete the learning files.

Risk: The skill can batch publish skills and bump versions automatically.

Mitigation: Require manual confirmation before batch publishing, release version changes, or marketplace submissions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/auto-publisher-self-learning)
- [Publisher profile](https://clawhub.ai/user/qq435912743)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose package installation, local learning-file writes, CLI patching, version bumps, retries, and ClawHub publish actions.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
