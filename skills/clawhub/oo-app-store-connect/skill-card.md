## Description:

Operates App Store Connect through an OOMOL-connected account for reading apps, versions, builds, users, TestFlight resources, testers, and customer reviews, and for approved state-changing actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate App Store Connect from an agent workflow, including app, build, TestFlight, user, tester, and review management through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: App Store Connect requests and responses can include sensitive account, app, tester, user, build, and review data processed through OOMOL.

Mitigation: Install only if OOMOL is trusted for this account, and use the least-privileged App Store Connect credential that supports the intended task.

Risk: Write and destructive actions can change or remove TestFlight groups, testers, builds, test notes, or review responses.

Mitigation: Require explicit user confirmation of the target, payload, and expected effect before running any change, deletion, or review-response action.

Risk: The review-response action publishes or replaces a public developer response but is not labeled as a write action in the artifact action list.

Mitigation: Treat every customer review response as a state-changing action and require explicit approval before execution.

Risk: First-time setup includes remote oo CLI installer commands that execute downloaded code.

Mitigation: Inspect or verify the installer before use, prefer a trusted installation path when available, and approve local software installation separately from connector actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-app-store-connect)
- [Publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [App Store Connect homepage](https://appstoreconnect.apple.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Directs the agent to inspect the live App Store Connect connector schema before running actions and to request confirmation before write or destructive operations.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
