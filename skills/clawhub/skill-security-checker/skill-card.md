## Description:

Skill Security Checker scans ClawHub, SkillHub, and WorkBuddy skill directories for security, dependency, permission, supply-chain, sandbox, and compliance issues and can produce text, JSON, HTML, or SARIF reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers use this skill to audit skill directories before release, assess third-party skills, and generate CI-friendly reports with remediation guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may contact GitHub by default for update checks, which can be undesirable in offline or sensitive environments.

Mitigation: Run with --skip-update when network access should be avoided.

Risk: The optional syscall monitor uses root or administrator telemetry paths, and the server security summary says this high-privilege behavior needs review before installation.

Mitigation: Avoid --syscall-monitor unless the operator has reviewed and accepted the privilege requirements, telemetry behavior, and implementation limits.

Risk: Dynamic scanning executes target skill code in a sandbox when enabled.

Mitigation: Use --dynamic only with Docker or Windows Sandbox available, keep default network isolation, and allow only trusted domains with --allow-domain.

Risk: The scanner reads skill directories and can write cache or report files.

Mitigation: Run it only against intended directories and direct outputs to approved locations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/skill-security-checker)
- [scan-patterns.md](artifact/references/scan-patterns.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands plus text, JSON, HTML, and SARIF report outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may be printed to the terminal or written to caller-selected output files; optional features can read local caches, write report/cache files, and perform a GitHub update check unless skipped.]

## Skill Version(s):

3.3.0 (source: SKILL.md frontmatter and evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
