## Description:

Operates Speedtest Tracker through the OOMOL oo CLI to inspect service health, retrieve speedtest results, list servers, get aggregate statistics, and queue new speedtests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to interact with an OOMOL-connected Speedtest Tracker instance from an agent. It supports reading recent and historical speedtest data, checking instance health, inspecting servers, reviewing aggregate network statistics, and queueing a new speedtest when explicitly approved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary says the skill under-discloses the state-changing run_speedtest action.

Mitigation: Require explicit user approval before queueing a new speedtest and confirm the intended payload and effect.

Risk: The security guidance identifies the documented remote installer commands as unsafe unless independently verified.

Mitigation: Avoid curl|bash or irm|iex installer paths unless the installer source and integrity have been independently verified.

## Reference(s):

- [Speedtest Tracker homepage](https://speedtest-tracker.dev/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-speedtest-tracker)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON responses returned by the oo CLI; state-changing speedtest runs require explicit user confirmation.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
