## Description:

Control Eight Sleep pods (status, temperature, alarms, schedules).

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent prepare eightctl commands and setup guidance for checking and controlling Eight Sleep pod status, temperature, alarms, schedules, audio, and base angle.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs a mutable third-party CLI that handles account credentials and device control.

Mitigation: Review the upstream eightctl project before installation and prefer a pinned version when one is available.

Risk: Commands can change temperature, alarms, schedules, audio playback, or base angle.

Mitigation: Confirm any command that changes device state before running it.

Risk: The underlying API is described as unofficial and rate-limited.

Mitigation: Avoid repeated logins and unnecessary repeated requests.

## Reference(s):

- [eightctl homepage](https://eightctl.sh)
- [ClawHub skill page](https://clawhub.ai/azizbrownint/skills/eightctl)
- [eightctl Go install module](https://pkg.go.dev/github.com/steipete/eightctl/cmd/eightctl)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include commands that control an Eight Sleep device; credential setup is required.]

## Skill Version(s):

1.0.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
