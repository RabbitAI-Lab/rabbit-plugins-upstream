## Description:

Fully automated multi-round code iteration with configurable N-dimension parallel review, onboarding/personalization, and a cross-assistant installer/update system with mandatory SHA256 checksum verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use Iterate to run structured, multi-round code review and remediation across correctness, security, performance, architecture, testing, and related dimensions. It is suited for pre-release hardening, refactoring passes, and repeated quality checks where the agent may propose or apply code edits after the configured review and approval steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: High-autonomy review and fixing can modify repository files and run configured validation commands.

Mitigation: Use the skill only on repositories where automated edits and validation commands are acceptable; review validation.commands before execution and use review-only or dry-run mode for audits.

Risk: Automatic merge or push behavior could publish changes before the user has reviewed them.

Mitigation: Keep auto_merge and push_per_round disabled unless automatic publication is explicitly intended.

Risk: Installer or update flows can download release assets and install local tooling.

Mitigation: Prefer the checksum-verified installer and avoid the related harness curl | bash example unless the script source and execution environment have been reviewed.

Risk: Passing tokens on shared systems can expose credentials through shell history or process listings.

Mitigation: Use GITHUB_TOKEN instead of a --token argument on shared systems.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jingzhao-l/skills/iterate-skill)
- [GitHub repository](https://github.com/jingzhao-l/iterate-skill)
- [GitHub releases](https://github.com/jingzhao-l/iterate-skill/releases)
- [npm installer package](https://www.npmjs.com/package/iterate-skill-installer)
- [ModelScope listing](https://www.modelscope.cn/skills/jingzhao0/iterate-skill)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and summaries, code or configuration edits, and shell commands when validation or installation steps are needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can operate in review-only mode, or in iterative edit mode with configured validation commands and opt-in merge or push behavior.]

## Skill Version(s):

2.3.19 (source: frontmatter, pyproject.toml, npm package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
