## Description:

Packages an existing local HTML, CSS, or JavaScript site or built frontend into a self-contained Electron desktop application for macOS or Windows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ully](https://clawhub.ai/user/ully)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to package local static sites or production frontend builds as offline-first Electron desktop apps, with guidance for icons, platform packaging, signing checks, and local SQLite storage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify a local web project and package unintended files into desktop release artifacts.

Mitigation: Confirm the target folder before execution and review packaged contents, especially secrets, remote API dependencies, signing credentials, and files copied into release artifacts.

Risk: Local packaging does not automatically make remote APIs, OAuth flows, CDN-only assets, server databases, or secrets available offline.

Mitigation: Identify external services and decide connectivity, credential storage, and offline behavior before delivering an offline-first application.

## Reference(s):

- [Packaging Matrix](artifact/references/packaging-matrix.md)
- [Packaging Test Cases](artifact/references/test-cases.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, code snippets, and configuration changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or modify local Electron project files and report artifact paths, architecture, signing status, test results, and online dependencies.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
