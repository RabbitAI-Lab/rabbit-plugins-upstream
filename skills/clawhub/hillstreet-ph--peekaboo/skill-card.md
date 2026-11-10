## Description:

Capture and automate macOS UI with the Peekaboo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hillstreet-ph](https://clawhub.ai/user/hillstreet-ph)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and macOS users can use the skill to inspect an application interface, carry out authorized actions on the intended target, and verify the result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial because a referenced local path could not be resolved.

Mitigation: Review the unresolved reference and decide whether the incomplete scan evidence is sufficient before installing.

Risk: Foreground keyboard and cursor actions can affect the wrong window or UI target if observations are stale.

Mitigation: Inspect the intended app and window immediately before acting, use current target details, and verify the UI after each action.

## Reference(s):

- [Peekaboo homepage](https://peekaboo.boo)
- [ClawHub skill release](https://clawhub.ai/hillstreet-ph/skills/peekaboo)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with inline shell commands, configuration examples, and tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands and examples should follow the installed Peekaboo version and the user's current macOS UI state.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
