## Description:

Print the current UTC time and ISO date in a deterministic, copy-friendly format.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agents use this skill when logs, notes, manifests, or filenames need a stable UTC timestamp or date prefix.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The script may not run directly if executable permissions are not preserved by packaging.

Mitigation: Run it with sh scripts/echo_now.sh or adjust executable permissions before use.

Risk: The output depends on the host system clock.

Mitigation: Use hosts with synchronized time when the timestamp is used for logs, manifests, or release records.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/terrycarter1985/skills/echo-now)
- [ClawHub publisher profile](https://clawhub.ai/user/terrycarter1985)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [Plain text timestamp lines and Markdown usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs two newline-delimited key-value strings: utc=<YYYY-MM-DDTHH:MM:SSZ> and date=<YYYY-MM-DD>.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
