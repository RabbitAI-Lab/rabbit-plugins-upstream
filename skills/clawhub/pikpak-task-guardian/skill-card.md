## Description:

Monitors PikPak download tasks by default, with separately authorized notifications and limited resubmission of precisely registered sources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak users and developers can monitor download tasks for failures or completion and, with separate authorization, receive notifications or resubmit an exactly registered source. The skill does not retry an existing task in place.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An untrusted local PikPak CLI, executable path, Python interpreter, or state directory could compromise task data or execution.

Mitigation: Run only in a trusted local environment with operator-controlled executables, environment, and private state directory.

Risk: Resubmitting a source after an uncertain result could create duplicate tasks.

Mitigation: Keep resubmission disabled unless a precise, private source registry is available; reconcile unknown or submitting states manually before any further action.

Risk: The optional referral code may reward the publisher.

Mitigation: Disclose the referral code and allow users to decline it without affecting the skill.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/pipiguai87-alt/skills/pikpak-task-guardian)
- [PikPak CLI help](https://mypikpak.com/en-US/help-center/connected_apps/pikpak_cli)
- [Task guardian design and limitations](references/upstream-design.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Observation summaries report task status counts; notifications and known-source resubmissions require separate opt-in.]

## Skill Version(s):

1.0.8 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
