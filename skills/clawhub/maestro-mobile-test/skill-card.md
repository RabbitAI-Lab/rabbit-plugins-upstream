## Description:

Write and run end-to-end Maestro CLI tests for React Native and Expo apps on Android emulators or iOS simulators, including YAML flows, setup guidance, and CI-oriented execution patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create, organize, and run native mobile end-to-end tests for React Native and Expo applications with Maestro. It is intended for emulator or simulator workflows where browser-based testing cannot verify native components, device APIs, secure storage, notifications, or platform-specific behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can run unverified internet-downloaded shell code and install system packages on a developer machine.

Mitigation: Prefer a pinned, verified Maestro release or review the downloaded installer before running setup.

Risk: The skill can install developer tools, write ~/.maestro/activate.sh, boot emulators, run adb commands, and execute Maestro flows.

Mitigation: Use it only in a development environment, review commands and generated flows before execution, and point tests at non-production apps and backends.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dennisrongo/skills/maestro-mobile-test)
- [Maestro documentation](https://maestro.mobile.dev)
- [Maestro test suites and reports](https://maestro.mobile.dev/cli/test-suites-and-reports)
- [Maestro flow API reference](https://maestro.mobile.dev/reference/api)
- [Maestro GitHub repository](https://github.com/mobile-dev-inc/maestro)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with YAML flow examples and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or create Maestro YAML flows and local setup or runner commands for mobile test execution.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
