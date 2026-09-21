## Description:

Speedtest Tracker enables agents to operate a user's OOMOL-connected Speedtest Tracker instance for reading results, inspecting stats and servers, checking health, and queuing new speed tests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and users with an OOMOL-connected Speedtest Tracker account use this skill to inspect network performance data and initiate speed tests through documented connector actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback installer commands fetch and execute remote scripts without verification.

Mitigation: Do not allow an agent to run the installer commands automatically; install the oo CLI manually from a trusted source and verify the installer where possible.

Risk: The run_speedtest action queues a new speed test and changes Speedtest Tracker state.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [Speedtest Tracker homepage](https://speedtest-tracker.dev/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-speedtest-tracker)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke oo CLI connector actions; write actions require user confirmation before execution.]

## Skill Version(s):

1.0.1 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
