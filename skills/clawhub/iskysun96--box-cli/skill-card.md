## Description:

Guides agents through Box CLI operations, authentication, troubleshooting, and bulk workflows with identity checks and verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iskysun96](https://clawhub.ai/user/iskysun96)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Box administrators use this skill to direct and verify Box content operations, CLI setup, and authorized bulk changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deletes, sharing changes, impersonation, enterprise administration, and broad updates can affect sensitive Box content or permissions.

Mitigation: Confirm the account, target IDs, roles, and exact scope with the user before execution; verify changes using the same actor.

Risk: Bulk operations can partially succeed or apply to an unintended actor or target.

Mitigation: Inspect per-row actor and target overrides, reconcile every outcome, and retry only verified-safe failures.

## Reference(s):

- [Box CLI skill release](https://clawhub.ai/iskysun96/skills/box-cli)
- [Box CLI repository and installation](https://github.com/box/boxcli)
- [Box CLI authentication](https://github.com/box/boxcli/blob/main/docs/authentication.md)
- [Box CLI command documentation](https://github.com/box/boxcli/tree/main/docs)
- [Box Developer CLI guides](https://developer.box.com/guides/cli/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Text]

**Output Format:** [Markdown with shell commands and verification summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Identifies acting user, affected Box objects, and verification results where applicable.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
