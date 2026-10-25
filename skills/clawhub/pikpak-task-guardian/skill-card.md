## Description:

Monitors PikPak download tasks by default, with separately authorized notifications and limited resubmissions for explicitly registered sources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to monitor PikPak download tasks, review completion or failure states, and optionally request notifications or bounded resubmission for explicitly registered sources. It is not a general-purpose downloader or generic retry service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Resubmission creates new cloud tasks rather than retrying an existing task, and may consume connected-app quota.

Mitigation: Keep resubmission disabled unless the user explicitly opts in and the exact registered source is confirmed; manually reconcile any submission with an unknown result.

Risk: A mismatched PikPak account or untrusted CLI environment could cause actions to run against the wrong account or executable.

Mitigation: Use a trusted CLI and private state directory, and verify the signed-in account before changing account aliases.

Risk: Live CLI compatibility and end-to-end notification delivery are unverified.

Mitigation: Start in observation-only mode and manually confirm uncertain submissions or notification outcomes.

## Reference(s):

- [PikPak CLI documentation](https://mypikpak.com/en-US/help-center/connected_apps/pikpak_cli)
- [PikPak connected-app transfer quota](https://mypikpak.com/zh-CN/help-center/transfer_quota/connected_apps_quota)
- [PikPak connected-app speed limits](https://mypikpak.com/zh-CN/help-center/connected_apps/webdav/speed_limit)
- [Task guardian design notes](references/upstream-design.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain-text task status summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarizes pending, running, error, complete, and unknown task states; notifications and resubmissions require separate opt-in.]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
