## Description:

Cz Cli - Commitizen - conventional commit helper that helps agents generate, validate, lint, scope, and summarize conventional commit messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xueyetianya](https://clawhub.ai/user/xueyetianya)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to draft conventional commit messages, inspect recent commit history, validate commit-message format, and produce changelog-style summaries from Git history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated copy-and-run git commands can be unsafe if commit text contains untrusted quotes or shell characters.

Mitigation: Review generated commands before execution and use the documented cz_cli.sh interface only with trusted commit text.

Risk: The package includes an extra local data-storage utility that can persist and export user-supplied data.

Mitigation: Avoid entering sensitive data, inspect local storage behavior before installation, and remove persisted data when it is no longer needed.

## Reference(s):

- [Commit Helper on ClawHub](https://clawhub.ai/xueyetianya/skills/commit-helper)
- [BytesAgain homepage](https://bytesagain.com)
- [Commitizen cz-cli reference](https://github.com/commitizen/cz-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Plain text and Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces command-line output and suggested git commit commands; changelog output depends on local Git history.]

## Skill Version(s):

2.0.0 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
