## Description:

Use when building, uploading, or debugging PlatformIO Arduino/C++ projects for the UNIHIKER K10 information-technology experiment box, especially LVGL sensor dashboards or games, QMI8658 six-axis control, microphone FFT visualizers, sound-reactive lights, DFRobot_K10Box integration, knob-controlled motors, actuator tests, or K10-native versus box-hardware conflicts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rockets-cn](https://clawhub.ai/user/rockets-cn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to build and diagnose PlatformIO Arduino/C++ projects for the UNIHIKER K10 experiment box. It helps keep K10-native devices distinct from the box controller, IMU, line tracker, and actuators while producing safe LVGL, sensor, audio, motion-game, and actuator guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer downloads driver files from an upstream commit and writes them into a user-selected PlatformIO project.

Mitigation: Review the disclosed upstream commit and target project path before running the installer; use --force only when replacing the existing DFRobot_K10Box library is intended.

Risk: Actuator tests can move motors, sound the buzzer, or drive LEDs unexpectedly if triggered casually.

Mitigation: Trigger actuator tests only through explicit user action, keep the hardware area clear, and stop motors, buzzer, and LEDs on completion, cancellation, page exit, and startup.

Risk: Confusing K10-native sensors with experiment-box hardware can produce misleading diagnostics or unsafe actuator assumptions.

Mitigation: Probe expected I2C identities, keep K10-native and box values separately labeled, and enable actuator paths only after the box IO controller responds.

## Reference(s):

- [K10 Box Hardware Map](references/hardware-map.md)
- [LVGL Dashboard and Actuator Patterns](references/lvgl-dashboard.md)
- [K10 Box Audio FFT and Reactive Lights](references/audio-fft.md)
- [QMI8658 Six-Axis LVGL Games](references/six-axis-games.md)
- [K10 Box Troubleshooting](references/troubleshooting.md)
- [ClawHub skill page](https://clawhub.ai/rockets-cn/skills/unihiker-k10-box-platformio)
- [DFRobot PlatformIO platform](https://github.com/DFRobot/platform-unihiker.git)
- [DFRobot K10 Box driver source](https://gitee.com/zhaoruiz/ext-unihiker-k10-box)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline PlatformIO configuration, C++ examples, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include hardware verification steps, serial diagnostics, and safety checks for actuator use.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
