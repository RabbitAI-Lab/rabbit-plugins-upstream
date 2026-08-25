## Description:

Helps users resolve macOS Xcode Command Line Tools installation failures by finding Apple sucatalog package URLs, downloading signed packages through terminal-friendly networking, and preparing manual installation steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[isxiaojian](https://clawhub.ai/user/isxiaojian)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when macOS Command Line Tools installation fails through the GUI, xcode-select, or softwareupdate, especially in network environments where terminal proxy downloads are more reliable. The skill helps identify official Apple package URLs, verify package signatures, and generate a local install script for the user to run.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The generated installer script changes system developer-tool configuration and requires sudo privileges.

Mitigation: Have the user inspect the generated script before running it and run it locally only when they intend to install or repair macOS Command Line Tools.

Risk: Incorrect or tampered package URLs could lead to installing untrusted software.

Mitigation: Confirm package URLs come from Apple's swscan or swcdn update endpoints and require pkgutil to report valid Apple signatures before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/isxiaojian/skills/macos-clt-offline-install)
- [Apple Software Update scan endpoint](https://swscan.apple.com)
- [Apple macOS 15 software update catalog](https://swscan.apple.com/content/catalogs/others/index-15-14-13-12-10.16-10.15-10.14-10.13-10.12-10.11-10.10-10.9-mountainlion-lion-snowleopard-leopard.merged-1.sucatalog)
- [Apple macOS 14 software update catalog](https://swscan.apple.com/content/catalogs/others/index-14-13-12-10.16-10.15-10.14-10.13-10.12-10.11-10.10-10.9-mountainlion-lion-snowleopard-leopard.merged-1.sucatalog)
- [Apple macOS 13 software update catalog](https://swscan.apple.com/content/catalogs/others/index-13-12-10.16-10.15-10.14-10.13-10.12-10.11-10.10-10.9-mountainlion-lion-snowleopard-leopard.merged-1.sucatalog)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline bash commands and generated shell script instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to generate a local install script that the user runs with sudo after validating Apple package signatures.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
