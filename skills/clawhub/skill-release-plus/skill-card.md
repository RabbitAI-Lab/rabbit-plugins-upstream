## Description:

skill-release-plus helps agents package, optionally sign, and publish skills to ClawHub, skillhub.cn, GitHub Releases, or custom hook targets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[songhonglei](https://clawhub.ai/user/songhonglei)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release engineers use this skill to publish agent skills across multiple registries from one workflow, including dry runs and deterministic package-only builds for governance review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Verified packaging and publishing flaws could expose files the user did not intend to release.

Mitigation: Review the exact skill directory before publishing and prefer package-only or dry-run flows before any network publish.

Risk: Publishing untrusted skill trees, especially those containing symlinks, may release unexpected content.

Mitigation: Avoid untrusted skill trees and use the deterministic package-only flow, which rejects symlinks according to the artifact documentation.

Risk: User-hook targets execute external scripts and can publish to arbitrary destinations.

Mitigation: Use user-hook scripts only when they are fully trusted and review their behavior before running them with release metadata or package paths.

Risk: Long-lived publishing tokens stored in configuration files increase credential exposure if the environment is compromised.

Mitigation: Use short-lived or scoped tokens and avoid storing long-lived publishing tokens in the global .env file.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/songhonglei/skills/skill-release-plus)
- [ClawHub CLI package](https://www.npmjs.com/package/clawhub)
- [skillhub.cn](https://skillhub.cn)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and release configuration details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or invoke release packages, manifests, and per-target publishing results through the bundled scripts.]

## Skill Version(s):

1.1.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
