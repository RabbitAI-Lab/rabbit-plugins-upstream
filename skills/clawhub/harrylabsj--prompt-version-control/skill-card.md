## Description:

Git-like version control for AI prompts: track changes, A/B test variants, measure metrics, rollback with confidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[harrylabsj](https://clawhub.ai/user/harrylabsj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI teams use this skill to manage prompt changes with version history, semantic diffs, A/B testing, rollback, and iteration reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI mutates local repository files and unsafe input handling can write outside the prompt folder.

Mitigation: Run it only in trusted repositories with trusted prompt names, and review generated file paths before execution.

Risk: Crafted prompt names may trigger local code execution through unsafe helper invocation.

Mitigation: Do not execute it with untrusted prompt names until prompt-name validation is enforced and helper paths are passed safely.

Risk: Future remote sync can upload prompt contents to the configured git remote.

Mitigation: Use synthetic or anonymized test cases and confirm remote permissions and destination before syncing proprietary prompt content.

Risk: Secrets exposed in the environment may be available while the CLI is running.

Mitigation: Avoid running it with sensitive environment variables present unless the repository, prompt names, and execution path are trusted.

## Reference(s):

- [Default prompt repository configuration](references/config.yaml)
- [Prompt Version Control input schema](schemas/input.schema.json)
- [Prompt Version Control output schema](schemas/output.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON/YAML schema-backed files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces prompt repository files, version logs, diffs, rollback summaries, A/B comparison tables, and iteration reports.]

## Skill Version(s):

1.0.0 (source: frontmatter, skill.json, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
