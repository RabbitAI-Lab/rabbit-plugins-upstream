## Description: <br>
Use when programming Unihiker K10 board with MicroPython, uploading code, flashing firmware, or accessing K10 MicroPython APIs (screen, sensors, RGB, audio, AI). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rockets-cn](https://clawhub.ai/user/rockets-cn) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to create, upload, debug, and flash MicroPython programs for the Unihiker K10 board, including display, sensor, RGB LED, audio, and AI API usage. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup script can run remote installer code, invoke sudo, and modify local developer tooling. <br>
Mitigation: Review scripts/setup.sh before use; prefer installing arduino-cli, mpremote, and ampy through trusted package managers or isolated environments, and avoid unattended or sudo execution unless host-level changes are acceptable. <br>


## Reference(s): <br>
- [MicroPython API Reference](references/micropython-api.md) <br>
- [DFRobot Gravity I2C ADS1115 16-bit ADC module](https://www.dfrobot.com.cn/goods-1734.html) <br>
- [DFRobot Unihiker Board Manager Package Index](https://downloadcd.dfrobot.com.cn/UNIHIKER/package_unihiker_index.json) <br>
- [Arduino CLI Installation](https://arduino.github.io/arduino-cli/latest/installation/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown guidance with Python and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose local shell commands and MicroPython code for connected K10 hardware.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
