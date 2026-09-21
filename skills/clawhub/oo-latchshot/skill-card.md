## Description:

Latchshot lets agents operate an OOMOL-connected Latchshot account to capture public web pages as artifacts and check usage details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run Latchshot connector actions through an authenticated OOMOL account, including rendering public web pages as PNG, JPEG, or PDF artifacts and checking plan usage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes direct remote-script execution to install the oo CLI.

Mitigation: Prefer a signed package or official install guide, inspect downloaded installers before running them, and avoid remote-script installation when a safer installation path is available.

Risk: The capture_page action changes Latchshot state by rendering and uploading a bounded artifact.

Mitigation: Fetch the live connector schema before building the payload and confirm the target URL, output format, and expected effect with the user before execution.

## Reference(s):

- [ClawHub Latchshot skill page](https://clawhub.ai/oomol/skills/oo-latchshot)
- [Latchshot homepage](https://latchshot.fly.dev)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads; connector responses are JSON and capture_page can produce PNG, JPEG, or PDF artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; write actions require user confirmation of payload and effect.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
