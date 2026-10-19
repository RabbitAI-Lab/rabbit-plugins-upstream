## Description:

Guides a single authorized PikPak magnet or link through task creation, status checks, one-file download, and manually reviewed cloud cleanup suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak users and developers can download one authorized magnet or link with a local receipt, then review suggested cloud cleanup commands after verifying the downloaded file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An untrusted local CLI or environment could affect account operations and downloads.

Mitigation: Run only in a trusted environment and verify PIKPAK_BIN and PATH before execution.

Risk: The local state file contains account and download details that should not be shared.

Mitigation: Keep each state file private and authorize the account, resource, and destination explicitly.

Risk: Cloud cleanup commands could target the wrong object or remove wanted content if run without review.

Mitigation: Verify the downloaded content and current cloud object, then review any printed cleanup command before running it manually.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/pipiguai87-alt/skills/pikpak-magnet-pipeline)
- [Upstream design notes](references/upstream-design.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON]

**Output Format:** [Step-by-step guidance and CLI output, including a local JSON receipt and printed cleanup suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Processes one resource and one file per state file; cloud deletion requires separate manual action.]

## Skill Version(s):

1.0.8 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
