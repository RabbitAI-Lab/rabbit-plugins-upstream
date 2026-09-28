## Description:

Guides developers through diagnosing failed GitHub, Gitee, and AtomGit pushes and choosing credential, network, or API-based remedies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

All rights reserved (documentation; MIT applies only to .py code files)

## Use Case:

Developers use this Chinese-language workflow to diagnose Git hosting authentication and connection failures, prepare safer push commands, and consider GitHub API fallback steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Overbroad or exposed Git hosting tokens may grant unintended repository access.

Mitigation: Use narrowly scoped tokens and avoid storing secrets in plaintext.

Risk: Pushes, API calls, or switching a private repository to public can change or disclose repository contents.

Mitigation: Explicitly approve each write or visibility change after reviewing its target and effects.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/github-api-push-workaround)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands and visibility changes require user review before execution.]

## Skill Version(s):

1.0.2 (source: ClawHub release; embedded version labels differ)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
