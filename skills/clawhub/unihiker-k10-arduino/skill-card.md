## Description: <br>
Use when programming Unihiker K10 board with Arduino/C++, uploading code, flashing firmware, or accessing K10 Arduino APIs (screen, sensors, RGB, audio, AI, TTS, ASR). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rockets-cn](https://clawhub.ai/user/rockets-cn) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, educators, and makers use this skill to set up Arduino tooling for the Unihiker K10, compile and upload sketches, troubleshoot board connectivity, and look up K10 screen, sensor, audio, AI, TTS, ASR, GPIO, and OTA APIs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup workflow can run remote installer code and make privileged system changes. <br>
Mitigation: Review setup scripts before running them, prefer a trusted package manager or pinned release for arduino-cli, avoid sudo fallback unless a system-wide install is intended, and use an isolated Python environment for mpremote and ampy. <br>
Risk: Camera, face recognition, motion detection, QR scanning, microphone recording, and continuous ASR examples can process sensitive personal or environmental data. <br>
Mitigation: Before deploying beyond personal experiments, add clear notice and consent, visible active indicators, and deletion and retention controls. <br>
Risk: K10 AI, voice, TTS, face-recognition, and OTA workflows can depend on firmware variants and factory model-data offsets. <br>
Mitigation: Confirm the installed firmware variant before using TTS and preserve factory model-data offsets when generating, compiling, uploading, or troubleshooting sketches that use AI, voice, face recognition, or OTA partitions. <br>


## Reference(s): <br>
- [Arduino API Reference](references/arduino-api.md) <br>
- [Arduino Examples](references/arduino-examples.md) <br>
- [Arduino CLI Releases](https://github.com/arduino/arduino-cli/releases) <br>
- [DFRobot UNIHIKER K10 Board Manager Index](https://downloadcd.dfrobot.com.cn/UNIHIKER/package_unihiker_index.json) <br>
- [Espressif ESP32 Arduino Core Index](https://dl.espressif.com/dl/package_esp32_index.json) <br>
- [ESP32 Arduino Core China Mirror](https://jihulab.com/esp-mirror/espressif/arduino-esp32/-/raw/gh-pages/package_esp32_index_cn.json) <br>
- [UNIHIKER K10 Arduino PIO Example](https://www.unihiker.com.cn/wiki/k10/Arduino_PIO_Example) <br>
- [UNIHIKER K10 Arduino PIO API List](https://www.unihiker.com.cn/wiki/k10/Arduino_PIO_API_List) <br>
- [DFRobot Gravity I2C ADS1115 Module](https://www.dfrobot.com.cn/goods-1734.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Arduino/C++ snippets, shell commands, PowerShell commands, and configuration instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce local setup, compile, upload, OTA, and troubleshooting commands for Arduino CLI and Unihiker K10 workflows.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
