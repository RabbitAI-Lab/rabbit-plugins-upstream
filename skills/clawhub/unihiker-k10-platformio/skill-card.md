## Description: <br>
Use when programming a UNIHIKER K10 board with PlatformIO CLI, creating or converting Arduino/C++ K10 projects to PlatformIO, building, uploading, monitoring serial output, diagnosing K10 PlatformIO setup or ASR microphone/wake-word failures, or preparing/installing offline PlatformIO support for workshops, including macOS archives and Windows self-extracting USB installers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rockets-cn](https://clawhub.ai/user/rockets-cn) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, educators, and workshop facilitators use this skill to create, convert, build, upload, monitor, and troubleshoot UNIHIKER K10 PlatformIO Arduino/C++ projects, including offline class setup and ASR/TTS diagnostics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bundled installer, build, upload, and monitor commands can modify local PlatformIO environments or connected K10 projects. <br>
Mitigation: Run them only from trusted workshop media and only against K10 project directories and boards the user expects to modify. <br>
Risk: Quarantine-removal guidance can reduce macOS protections for unverified downloaded files. <br>
Mitigation: Use quarantine removal only for trusted prepared installers or copied folders, and avoid applying it broadly to unknown downloads. <br>
Risk: Generated offline-bundle metadata can expose local paths, platform details, or preparation-machine information when shared. <br>
Mitigation: Review generated metadata and remove or redact it before distributing bundles outside the intended workshop context. <br>


## Reference(s): <br>
- [PlatformIO Workshop Notes for UNIHIKER K10](references/platformio-workshop.md) <br>
- [K10 AI Model Flashing and Recovery](references/k10-ai-model-flash.md) <br>
- [K10 ASR Audio Troubleshooting](references/k10-asr-audio-troubleshooting.md) <br>
- [K10 Arduino API](references/k10-arduino-api.md) <br>
- [K10 Arduino Examples](references/k10-arduino-examples.md) <br>
- [DFRobot PlatformIO Platform for UNIHIKER](https://github.com/DFRobot/platform-unihiker.git) <br>
- [UNIHIKER K10 Arduino/PIO Example](https://www.unihiker.com.cn/wiki/k10/Arduino_PIO_Example) <br>
- [UNIHIKER K10 Arduino/PIO API List](https://www.unihiker.com.cn/wiki/k10/Arduino_PIO_API_List) <br>
- [DFRobot Gravity I2C ADS1115 ADC Module](https://www.dfrobot.com.cn/goods-1734.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, PowerShell commands, C++ snippets, PlatformIO configuration, and troubleshooting guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include runnable local commands and project-file changes for PlatformIO-based K10 development.] <br>

## Skill Version(s): <br>
0.1.10 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
