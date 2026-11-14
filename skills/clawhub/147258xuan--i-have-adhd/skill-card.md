## Description:

Shape output for a reader with ADHD: lead with the next action, number multi-step work, respect a hard length budget, stop when the reader signals closure, never restate an unverified conclusion. Invoke with /i-have-adhd; on until "stop adhd mode".

This skill is ready for commercial/non-commercial use.

## Publisher:

[147258xuan](https://clawhub.ai/user/147258xuan)

### License/Terms of Use:

MIT-0

## Use Case:

People who want ADHD-aware response formatting can invoke this skill to make answers easier to scan and act on. It prioritizes a clear next action, short bounded steps, and concise responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is benign but medium-confidence because two local Markdown references could not be resolved.

Mitigation: Review the skill and check those references before enabling it.

Risk: The skill's output-style rules persist for the session until the reader gives a stated stop command.

Mitigation: Enable it when session-wide formatting changes are intended; use its documented stop command to end the mode.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Plain text or concise Markdown, often with numbered steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Applies a short response budget, caps displayed lists at five items, and favors a clear next action.]

## Skill Version(s):

0.1.0 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
