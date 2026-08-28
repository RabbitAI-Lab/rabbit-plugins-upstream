## Description:

Fully automated multi-round code iteration with configurable N-dimension parallel review, onboarding/personalization, and a cross-assistant installer/update system with mandatory SHA256 checksum verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use Iterate to run repeated, multi-dimension code reviews, apply small fixes, coordinate approved larger changes, and validate projects before release. It is suited for repository quality improvement, security hardening, refactoring wrap-up, and read-only review reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill has high-autonomy code and git automation that can edit files, run validation commands, and create commits.

Mitigation: Install only when this level of autonomy is acceptable, review generated branches before merging, and keep automated merge or push settings disabled unless explicitly intended.

Risk: PATH-level CLI installation changes the local environment.

Mitigation: Use the documented no-CLI installation mode when a PATH-level command should not be installed.

Risk: Token handling and curl-to-bash installation can expose credentials or execute unreviewed code.

Mitigation: Prefer GITHUB_TOKEN over command-line token flags and inspect installation scripts before using curl-to-bash flows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jingzhao-l/skills/iterate-skill)
- [GitHub repository](https://github.com/jingzhao-l/iterate-skill)
- [Release notes](RELEASE.md)
- [README](README.md)
- [Configuration schema](config/config.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, code edits, shell commands, configuration files, and review summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can edit files, run configured validation commands, create git commits, and generate review or iteration reports depending on mode.]

## Skill Version(s):

2.9.1 (source: frontmatter, pyproject.toml, package.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
