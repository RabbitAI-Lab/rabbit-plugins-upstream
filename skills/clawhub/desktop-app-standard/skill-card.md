## Description:

Build, maintain, or audit Tauri and Electron desktop apps, including dependencies, packaging, updates, CI, and .NET SDK or target-framework checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rockbenben](https://clawhub.ai/user/rockbenben)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to create, maintain, upgrade, and audit Tauri or Electron desktop apps and their CI and release pipelines. It provides project-specific checks, migration guidance, reusable templates, and .NET SDK or target-framework audits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is incomplete and flags audit-coverage weaknesses and releases made public before verification.

Mitigation: Check the platform-coverage and release-publication findings against the target project, and verify the release path before adopting the guidance.

Risk: Installer-language requirements and shell capabilities are flagged for review.

Mitigation: Inspect the relevant scripts and installer configuration, and confirm those requirements fit the project's platforms before running or adopting them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/rockbenben/skills/desktop-app-standard)
- [Project homepage](https://github.com/rockbenben/aishort-skills/tree/main/skills/desktop-app-standard)
- [Tauri updater documentation](https://v2.tauri.app/plugin/updater/)
- [Tauri GitHub pipeline documentation](https://v2.tauri.app/distribute/pipelines/github)
- [Electron security documentation](https://www.electronjs.org/docs/latest/tutorial/security)
- [GitHub Actions security hardening](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Shell commands, Code, Configuration, JSON]

**Output Format:** [Markdown findings and plans, shell commands, code and configuration examples or templates, and JSON audit reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-specific; scope follows the user's request and can be read-only or implementation-focused.]

## Skill Version(s):

0.9.15 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
