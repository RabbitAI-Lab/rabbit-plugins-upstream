## Description:

Helps PikPak users create, inspect, and manage share links and audit expired or unused shares.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak users create individual or batch share links, review access and expiration details, and identify old shares for possible removal. The audit produces recommendations without deleting shares.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A share link may expose unintended files or remain accessible longer than intended.

Mitigation: Confirm the account and target files before sharing; use passwords and expiration limits for public shares.

Risk: Removing a share invalidates its existing link.

Mitigation: Review suggested pikpak share rm commands and confirm the intended share before executing them.

## Reference(s):

- [PikPak Share Manager release](https://clawhub.ai/pipiguai87-alt/skills/pikpak-share-manager)
- [PikPak CLI](https://mypikpak.com/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON]

**Output Format:** [Share-management guidance and a text audit report, with optional JSON report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The audit does not create or delete shares; it suggests removal commands for user review.]

## Skill Version(s):

1.0.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
