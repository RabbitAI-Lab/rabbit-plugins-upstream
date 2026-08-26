## Description:

Minimal demonstration skill for verifying a ClawHub publish flow. Prints a configurable greeting and the current date so the publish/ingest path can be exercised with a safe, side-effect-free artifact.

This skill is for demonstration purposes and not for production usage.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release maintainers use this skill to smoke-test a ClawHub publish pipeline, verify that a freshly published skill installs and renders correctly, and demonstrate a simple skill input/output contract.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may mistake the demo greeting skill for a broader automation or production workflow.

Mitigation: Use it only for publish-flow smoke testing or input/output contract demonstrations, and verify functionality before relying on it for any operational task.

Risk: The documented command depends on a POSIX shell environment with date available.

Mitigation: Run it in an environment that provides a POSIX shell and date, or adapt the invocation for the target platform.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/terrycarter1985/skills/demo-hello-skill)
- [Publisher profile](https://clawhub.ai/user/terrycarter1985)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [Plain text greeting documented with Markdown and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The documented command prints one stdout line containing the greeting recipient and an ISO-8601 date.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
