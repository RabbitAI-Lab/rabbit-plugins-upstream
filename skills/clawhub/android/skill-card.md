## Description: <br>
Builds, debugs, ships, and hardens Android apps across Gradle, Jetpack Compose, XML Views, ADB, and Play release workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to diagnose Android build, install, runtime, and store release issues, and to generate or review Android app code, Gradle configuration, tests, hardening steps, and Play release guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill keeps local Android project memory such as toolchain versions, devices, releases, measurements, and decisions. <br>
Mitigation: Review the declared local Clawic data paths and keep credentials out of stored notes. <br>
Risk: Android device and release workflows can include destructive actions such as clearing app data, uninstalling apps, deleting build output, or halting a rollout. <br>
Mitigation: Require explicit confirmation and review the exact effect before executing destructive commands or release actions. <br>
Risk: Android troubleshooting guidance can affect signing, permissions, Play policy declarations, and security-sensitive app behavior. <br>
Mitigation: Review generated guidance against the project context and current platform or Play requirements before shipping changes. <br>


## Reference(s): <br>
- [Android Skill on ClawHub](https://clawhub.ai/ivangdavila/skills/android) <br>
- [Android Skill Homepage](https://clawic.com/skills/android) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown guidance with inline code and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Review proposed commands before execution, especially device, build, and release operations.] <br>

## Skill Version(s): <br>
1.0.3 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
