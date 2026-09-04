## Description:

Control Hantek DSO2D15 / DSO2000-series oscilloscopes over USB SCPI, including connection checks, channel/generator setup, waveform capture, probe compensation guidance, and remote-control lock handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jessehornbuckle](https://clawhub.ai/user/jessehornbuckle)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and electronics technicians use this skill to guide USB SCPI control of supported Hantek oscilloscopes, including setup checks, instrument configuration, waveform capture, troubleshooting, and safe bench reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to send commands to real USB test equipment.

Mitigation: Confirm the VISA resource and query *IDN? before sending setting changes.

Risk: Oscilloscope probing of powered circuits can create shorts through grounded probe leads.

Mitigation: Warn before safety-sensitive probing, confirm ground/reference points, and use current-limited or fused power and proper dummy loads where practical.

Risk: Private or underdocumented waveform and run-state commands may behave differently across firmware versions.

Mitigation: Test read-only behavior first, use generous timeouts, save raw bytes before decoding, and record model, firmware, scale, probe factor, timebase, sample rate, and enabled channels.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jessehornbuckle/skills/hantek-scope-control)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code, shell command, and SCPI command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include PyVISA examples, setup checklists, waveform capture notes, troubleshooting steps, and safety cautions.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
