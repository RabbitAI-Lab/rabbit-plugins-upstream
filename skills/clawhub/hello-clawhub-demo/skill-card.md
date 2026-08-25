## Description:

A minimal demo skill that greets the user and prints the current UTC timestamp to verify the ClawHub publish and install pipeline end to end.

This skill is for demonstration purposes and not for production usage.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release maintainers use this skill to demonstrate and smoke-test ClawHub skill publishing, installation, and registry round-trip validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the agent to run a shell command, even though the command is limited to printing a greeting and timestamp.

Mitigation: Review the command before execution and run it only in an environment where printing the current UTC timestamp is acceptable.

Risk: The skill is intended for publish and install smoke testing, not production automation.

Mitigation: Use it to verify ClawHub publishing or installation flows, and choose a task-specific skill for operational workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/terrycarter1985/skills/hello-clawhub-demo)

## Skill Output:

**Output Type(s):** [Shell commands, Text, Guidance]

**Output Format:** [Markdown with a bash command and plain text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prints a greeting with an ISO-8601 UTC timestamp; no external dependencies or API keys.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
