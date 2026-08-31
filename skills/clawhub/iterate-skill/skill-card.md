## Description:

Fully automated multi-round code iteration with configurable N-dimension parallel review, onboarding/personalization, and a cross-assistant installer/update system with mandatory SHA256 checksum verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use Iterate to run multi-round AI-assisted code review, fix atomic issues, request approval for larger changes, validate results, and produce review summaries before release or refactoring work is complete.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release was flagged for review because some instructions conflict around read-only mode and automatic Git merge/push behavior.

Mitigation: Keep auto_merge and push_per_round disabled unless explicitly intended, review diffs before merging, and confirm whether review-only or dry-run mode should prevent all file changes.

Risk: Installer and update flows can run local commands, install a CLI, and fetch release artifacts.

Mitigation: Prefer the checksum-verifying installer, avoid curl-to-shell install paths, and pass GitHub tokens through environment variables rather than command-line flags.

Risk: The skill can ask an AI agent to edit repositories and run configured validation commands.

Mitigation: Install only in repositories where this behavior is acceptable, review configuration before use, and require human approval for larger architectural changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jingzhao-l/skills/iterate-skill)
- [Agent Skills](https://agentskills.io/)
- [iterate-skill-installer npm package](https://www.npmjs.com/package/iterate-skill-installer)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and text with inline shell commands, code edits, configuration updates, and review summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May edit repository files, run configured validation commands, create git branches or worktrees, and install a local CLI depending on user choices and configuration.]

## Skill Version(s):

2.10.0 (source: frontmatter, pyproject.toml, npm package, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
