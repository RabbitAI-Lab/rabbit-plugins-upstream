## Description:

Generates or updates tutorials from VHS tapes and Playwright specs with dual-tone markdown and GIF recording.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and documentation maintainers use this skill to refresh user-facing tutorials by validating tape files and manifests, recording terminal and browser demos, and generating project docs, book pages, README demo sections, and GIF assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run project-supplied shell commands from tape files and manifest requires entries.

Mitigation: Install and use it only for trusted repositories, review all .tape files and manifest requires entries before execution, and avoid --skip-validation.

Risk: The skill can rebuild binaries, run recording tools, and edit documentation outputs.

Mitigation: Approve any cargo install, make build, npm, go, VHS, or Playwright commands before they run, and prefer a disposable container or clean workspace for recording demos.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-tutorial-updates)
- [Configured homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum)

## Skill Output:

**Output Type(s):** [markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash code blocks, tutorial file paths, and demo asset references.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update README.md, docs/tutorials/, book/src/tutorials/, book/src/SUMMARY.md, and GIF asset paths.]

## Skill Version(s):

1.9.19 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
