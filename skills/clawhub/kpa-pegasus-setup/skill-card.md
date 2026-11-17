## Description:

Provides setup, troubleshooting, and optimization guidance for Pegasus, RetroArch, PPSSPP, and EKA2L1 on the KONKR Pocket ADVANCE handheld.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT-0

## Use Case:

External users setting up a KONKR Pocket ADVANCE handheld use this skill to configure its game frontend and emulators, troubleshoot metadata and controls, verify the library, and plan cleanup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags executable downloads and installation behavior, and its analysis coverage is partial.

Mitigation: Review the full instructions and download sources before running setup scripts; use the documented dry-run mode first.

Risk: Cleanup operations may remove device or host files, including data without a device-side undo path.

Mitigation: Review the proposed file list and affected paths, keep a verified backup, and run cleanup only after explicit confirmation.

Risk: Setup and repair scripts can write configuration to a connected handheld and inspect host or device state.

Mitigation: Check the target device and paths before execution, and review each script’s planned changes before applying them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/lisong2003-lgtm/skills/kpa-pegasus-setup)
- [Installation guide](INSTALL.md)
- [Setup and troubleshooting playbook](references/PLAYBOOK.md)
- [Safety rules and operating constraints](references/HARD_RULES.md)
- [Verification and cleanup guidance](references/VERIFICATION.md)
- [EKA2L1 and N-Gage setup guide](references/EKA2L1_NGAGE.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Files]

**Output Format:** [Markdown guidance, shell commands, scripts, and configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes device setup and maintenance scripts; outputs and side effects depend on the selected operation.]

## Skill Version(s):

2.4.0 (source: SKILL.md frontmatter, CHANGELOG, released 2026-11-16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
