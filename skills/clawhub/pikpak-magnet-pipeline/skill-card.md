## Description:

Guides a single magnet or link through PikPak task creation, status checks, local download, and a manual cleanup preview.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese-speaking users and developers can manage an authorized single-file PikPak transfer through a local CLI, retain a download receipt, and review a cleanup command before deciding whether to run it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the local PikPak CLI can create cloud tasks and download files to disk.

Mitigation: Use only with authorization for the current account and resource, a trusted CLI and environment, and a user-approved download destination.

Risk: State files contain transfer and account-binding information that should not be shared.

Mitigation: Keep state files private and run the workflow from a trusted environment.

Risk: The printed cleanup command may delete cloud content if run manually; a local hash does not prove the download matches the source.

Mitigation: Verify the local content and current cloud account and object before choosing whether to run the printed command.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/pipiguai87-alt/skills/pikpak-magnet-pipeline)
- [Upstream design and limitations](references/upstream-design.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files]

**Output Format:** [JSON status and download receipts, with plain-text cleanup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Single-file local download; cleanup is printed for manual review, not executed.]

## Skill Version(s):

1.0.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
