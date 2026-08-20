## Description:

Write and run YAML end-to-end tests for React Native and Expo apps with Maestro CLI on Android emulators or iOS simulators.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and QA engineers use this skill to create native mobile E2E flows, run them against emulators or simulators, and avoid common React Native and Expo testing pitfalls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can install system packages and run a remote shell installer.

Mitigation: Review the setup script before running it; prefer manually installing Java and Maestro from trusted, versioned sources, and avoid the curl-to-bash path unless you accept remote code execution on the local machine.

Risk: The setup and run scripts can make local development environment changes involving sudo, winget, brew, emulator, adb, and PATH updates.

Mitigation: Run these commands only in an intended development environment after reviewing the changes, and treat adb reverse, emulator boot, and PATH updates as deliberate local configuration changes.

## Reference(s):

- [Maestro documentation](https://maestro.mobile.dev)
- [Maestro command reference](https://maestro.mobile.dev/cli/test-suites-and-reports)
- [Maestro flow schema](https://maestro.mobile.dev/reference/api)
- [Maestro repository](https://github.com/mobile-dev-inc/maestro)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with YAML flows and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Maestro flow files, setup commands, emulator runner commands, and mobile testing troubleshooting guidance.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
