## Description: <br>
Control a Sphero Mini robot ball over Bluetooth Low Energy with Python, including movement, LED color changes, sensor access, shape drawing, and prebuilt play scripts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[joneschi](https://clawhub.ai/user/joneschi) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and robotics hobbyists use this skill to discover and control a Sphero Mini device from an agent workflow, generate Python examples, run bundled scripts, and troubleshoot Bluetooth LE setup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Troubleshooting guidance includes privileged Linux commands that can alter Bluetooth services or Python process capabilities system-wide. <br>
Mitigation: Review privileged commands before use, prefer non-privileged bleak setup where possible, and avoid granting persistent capabilities to the global python3 binary unless there is a verified rollback plan. <br>
Risk: The skill controls a physical robot ball that can move unexpectedly during examples or play scripts. <br>
Mitigation: Run movement scripts in a clear, supervised area, start at low speeds, and stop or disconnect the device before handling it. <br>


## Reference(s): <br>
- [Sphero Mini Control Skill](https://clawhub.ai/joneschi/skills/sphero-mini) <br>
- [API Reference](references/api.md) <br>
- [Examples](references/examples.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python snippets and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs assume a local Python 3 environment with bleak, Bluetooth access, and a Sphero Mini device.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
