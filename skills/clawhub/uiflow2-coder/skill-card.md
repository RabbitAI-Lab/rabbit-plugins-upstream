## Description:

UIFlow2 MicroPython coding assistant for writing, debugging, reviewing, and explaining code for M5Stack devices using bundled UIFlow2 documentation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuyun2000](https://clawhub.ai/user/yuyun2000)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to generate, debug, review, and explain UIFlow2 MicroPython code for M5Stack controllers, UI components, networking, and hardware accessories. It guides agents to consult bundled official documentation before producing code and to include minimal hardware validation steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated code may control physical devices such as relays, motors, servos, or power-related modules.

Mitigation: Require explicit user confirmation of the target board, wiring, power limits, and safe test conditions before executing on hardware.

Risk: Examples and docs cover USB keyboard and mouse emulation that can send input to a host computer.

Mitigation: Run HID-emulation code only with informed user consent on an isolated test host, and review the exact keystroke or mouse actions first.

Risk: Examples and docs cover cameras, microphones, location lookup, biometric enrollment/deletion, and NFC/RFID or storage writes.

Mitigation: Review privacy- and data-affecting behavior before use, avoid hardcoded secrets, and test with non-sensitive data and disposable tags or storage media.

Risk: The skill relies on bundled documentation and examples that may not match every firmware, board, or accessory revision.

Mitigation: Check the specific bundled API document for the selected device and perform a minimal hardware validation step before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuyun2000/skills/uiflow2-coder)
- [Complex examples reference](artifact/references/complex-examples.md)
- [UIFlow2 documentation file tree](artifact/file_tree.txt)
- [Bundled copyright and licenses](artifact/docs/COPYRIGHT.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with UIFlow2 MicroPython code blocks, documentation references, and validation steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should be checked against bundled UIFlow2 docs and reviewed before running on physical devices.]

## Skill Version(s):

1.0.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
