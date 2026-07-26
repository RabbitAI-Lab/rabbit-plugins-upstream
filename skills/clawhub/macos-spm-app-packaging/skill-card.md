## Description: <br>
This skill helps developers scaffold, build, package, sign, notarize, and create appcast release artifacts for SwiftPM-based macOS apps without an Xcode project. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dimillian](https://clawhub.ai/user/dimillian) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to create a SwiftPM macOS app layout and manage no-Xcode build, app bundle packaging, signing, notarization, and Sparkle appcast release steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The helper scripts handle signing credentials and can modify the user's login keychain. <br>
Mitigation: Review and edit the release scripts before running them, and use setup_dev_signing.sh only when a persistent development signing identity is intended. <br>
Risk: Credential files, temporary files, and version.env parsing require careful handling before Apple or Sparkle signing keys are provided. <br>
Mitigation: Use private temporary directories, restrictive file permissions, safe version parsing, and explicit cleanup/removal steps before using real signing credentials. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dimillian/skills/macos-spm-app-packaging) <br>
- [Packaging notes](references/packaging.md) <br>
- [Release and notarization notes](references/release.md) <br>
- [Scaffold a SwiftPM macOS app](references/scaffold.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and reusable script/configuration templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces project scaffolding and release-packaging instructions that should be adapted to the local macOS app and signing setup.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
