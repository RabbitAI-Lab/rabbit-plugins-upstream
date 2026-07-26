## Description: <br>
Initialize a minimal SwiftUI iOS app in the current directory by generating a single `.xcodeproj` with XcodeGen. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ignaciocervino](https://clawhub.ai/user/ignaciocervino) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers use this skill to create a clean, single-target SwiftUI iOS app scaffold in the current directory. It is intended for app initialization only, with XcodeGen producing the project from user-provided project name, deployment target, and optional bundle identifier. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Running the initializer in the wrong directory could create or mix project files with unrelated work. <br>
Mitigation: Run it only in an empty or intended project folder before generating files. <br>
Risk: The generated project depends on the local XcodeGen executable. <br>
Mitigation: Use a trusted local XcodeGen installation and verify Xcode is selected before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ignaciocervino/skills/swiftui-empty-app-init) <br>


## Skill Output: <br>
**Output Type(s):** [code, configuration, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with generated Swift and XcodeGen configuration content] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a minimal project.yml, SwiftUI source files, Info.plist content, and XcodeGen commands for a single app target.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
