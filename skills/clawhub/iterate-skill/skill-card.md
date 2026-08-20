## Description:

Fully automated multi-round code iteration with configurable N-dimension parallel review, onboarding and personalization support, and a cross-assistant installer/update system with mandatory SHA256 checksum verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use Iterate to run multi-round code review, automated fixes, validation, onboarding, and review-only audits across software projects. It is intended for code-quality, security-hardening, refactoring, and pre-release review workflows where human review remains important for high-impact changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: High-impact git automation can merge or push code when explicitly enabled.

Mitigation: Keep auto_merge and push_per_round disabled unless those actions are intended, and manually review iteration branches before merging or pushing.

Risk: Remote installer paths can execute downloaded code during setup.

Mitigation: Avoid the README's curl-to-bash harness install path; prefer checksum-verified installation paths or manually review installer contents before running them.

Risk: Command-line tokens can be exposed through shell history or process inspection.

Mitigation: Use the GITHUB_TOKEN environment variable instead of passing tokens on the command line.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jingzhao-l/skills/iterate-skill)
- [Publisher Profile](https://clawhub.ai/user/jingzhao-l)
- [Artifact README](artifact/README.md)
- [Security Notes](artifact/README.md#security)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code edits, shell commands, configuration files, and review summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May modify files and run configured validation commands when not in review-only mode; review-only mode emits reports without file changes.]

## Skill Version(s):

2.4.1 (source: server release, SKILL.md frontmatter, pyproject.toml, package.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
