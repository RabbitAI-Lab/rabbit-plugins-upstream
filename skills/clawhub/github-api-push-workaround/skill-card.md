## Description:

Guides developers through diagnosing Git push failures and choosing credential, network, or API-based remedies for GitHub, Gitee, and AtomGit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

All rights reserved

## Use Case:

Developers and engineers use this Chinese-language guide to troubleshoot Git push authentication and connection failures, or plan a remote-repository publishing workaround.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A push or API fallback may update the wrong repository, branch, or ref.

Mitigation: Confirm the repository, remote provider, and branch or ref before allowing the agent to act.

Risk: Changing repository visibility may publish private content.

Mitigation: Require explicit confirmation before any private-to-public visibility change.

Risk: Git credentials may be exposed in chat or command examples.

Mitigation: Keep tokens in a vault or environment variable; never paste long-lived credentials into chat.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/github-api-push-workaround)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance only; the package has no standalone code files.]

## Skill Version(s):

1.0.3 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
