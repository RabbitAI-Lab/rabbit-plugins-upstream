## Description:

元信 yotta-verify is a pre-install verifier for Agent skills and npm packages that performs deterministic local static scans for prompt injection, malicious patterns, SKILL.md integrity, and permissions, then returns a verdict, report, and audited badge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill before installing, evaluating, or publishing skills and npm packages to scan local files, generate install verdicts and reports, create audited badges, and enforce CI gates. It supports human review but does not replace the installer's final decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence marks the release suspicious because installer and scanner scoping and reliability issues remain.

Mitigation: Install only from a pinned, trusted release and review the skill carefully before enabling it.

Risk: The scanner should not be the only safety gate for untrusted skills or archives while known symlink, tarball-limit, and target-controlled exemption issues remain.

Mitigation: Use it as one review signal alongside manual inspection and any deeper security review required by the environment.

Risk: Global installation enables the skill across agents and may expand where its hook runs.

Mitigation: Choose one explicit destination such as --agent or --dir, and avoid global install unless that scope is intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-verify)
- [Prompt injection detection patterns](references/injection-patterns.md)
- [SKILL VERIFY REPORT template](references/verify-report-template.md)
- [Audited badge reference](references/badges.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration]

**Output Format:** [CLI verdict text, Markdown or JSON reports, badge SVG output, and install-gate exit codes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local offline static analysis; scanned code is not executed, installed, uploaded, or modified.]

## Skill Version(s):

0.3.1 (source: frontmatter, package.json, skill-manifest.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
