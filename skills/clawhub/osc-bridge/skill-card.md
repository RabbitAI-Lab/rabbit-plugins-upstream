## Description:

osc-bridge helps agents control music hardware and software through OSC, MIDI, and SysEx by selecting device drivers, reading route surfaces, starting the bridge, and troubleshooting silent failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[roomi-fields](https://clawhub.ai/user/roomi-fields)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, musicians, and automation builders use this skill to guide an agent through controlling hardware synthesizers, DAWs, and live-coding environments with osc-bridge. It is used to find device routes, configure local bridge processes, choose MIDI ports, send OSC messages, and diagnose silent UDP or device-control failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can send OSC, MIDI, and SysEx commands that change the state of music hardware or software.

Mitigation: Install only for intentional device-control workflows, verify MIDI output ports before sending, and treat raw SysEx as capable of changing device state.

Risk: Network-exposed bridge bindings can allow unintended OSC access beyond the local workstation.

Mitigation: Keep the bridge bound to localhost unless network access is deliberately required.

Risk: Fire-and-forget UDP behavior can report sent messages even when the bridge, host setup, reply port, or address is wrong.

Mitigation: Confirm the device catalogue is indexed, run a separate bridge process, use the documented OSC client and listener checks, and verify exact routes and argument types.

## Reference(s):

- [Devices: finding drivers and how addresses map to the wire](artifact/references/devices.md)
- [DAW and live-coding targets](artifact/references/software-targets.md)
- [When nothing happens](artifact/references/troubleshooting.md)
- [osc-bridge device browser](https://roomi-fields.github.io/osc-bridge/)
- [vcv-osc plugin](https://github.com/roomi-fields/vcv-osc)
- [ClawHub skill page](https://clawhub.ai/roomi-fields/skills/osc-bridge)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with JSON, shell, Ruby, SuperCollider, and TOML snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include device-specific OSC addresses, MIDI port choices, local bridge commands, and troubleshooting checks.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
