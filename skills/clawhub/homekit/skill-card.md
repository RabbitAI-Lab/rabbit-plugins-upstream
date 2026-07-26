## Description: <br>
Control Apple HomeKit smart home devices, including listing, discovering, pairing, and controlling lights, switches, outlets, and thermostats. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[manifoldor](https://clawhub.ai/user/manifoldor) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and smart-home operators use this skill to manage HomeKit accessories programmatically from an agent-assisted shell workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can control real HomeKit accessories, including power, brightness, pairing, unpairing, and batch on/off actions. <br>
Mitigation: Review each proposed command before running it, especially unpairing and batch actions, and only execute commands against intended devices. <br>
Risk: The local pairing file can enable future control of paired HomeKit devices. <br>
Mitigation: Protect the local HomeKit pairing file and avoid sharing it or storing it in synced or public locations. <br>
Risk: Device control depends on the local network, paired devices, and the HomeKit Python library being installed. <br>
Mitigation: Confirm the machine is on the expected Wi-Fi network, dependencies are installed, and device aliases are correct before sending control commands. <br>


## Reference(s): <br>
- [HomeKit API Reference](references/api.md) <br>
- [Apple HomeKit Documentation](https://developer.apple.com/homekit/) <br>
- [homekit_python Library](https://github.com/jlusiardi/homekit_python) <br>
- [ClawHub Skill Page](https://clawhub.ai/manifoldor/skills/homekit) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and Python examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces user-run commands for local HomeKit discovery, pairing, status checks, and accessory control.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
