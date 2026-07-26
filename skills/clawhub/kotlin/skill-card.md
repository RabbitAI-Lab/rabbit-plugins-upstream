## Description: <br>
Writes, debugs, and reviews Kotlin across coroutines and flows, null safety, collections, Java interop, Compose state, Kotlin Multiplatform, server-side Kotlin, testing, build, serialization, and performance issues. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to write, debug, migrate, and review Kotlin code for Android, JVM/server, library, and multiplatform projects. It is intended for Kotlin-specific language, runtime, and compiler guidance, not Java-only codebases or Android release signing and distribution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local preference memory can retain stack details, recurring issues, or other project context. <br>
Mitigation: Review ~/Clawic/data/kotlin/config.yaml and ~/Clawic/data/kotlin/memory.md periodically, and do not store secrets or sensitive project data there. <br>
Risk: Generated Kotlin guidance, code, shell commands, or configuration may not match a project's Kotlin, Android, JVM, or library versions. <br>
Mitigation: Review generated changes against the project build files and tests before applying them. <br>


## Reference(s): <br>
- [ClawHub Kotlin Skill Page](https://clawhub.ai/ivangdavila/skills/kotlin) <br>
- [Clawic Kotlin Skill Page](https://clawic.com/skills/kotlin) <br>
- [Kotlin Skill Definition](artifact/SKILL.md) <br>
- [Kotlin Setup Notes](artifact/setup.md) <br>
- [Kotlin Memory Template](artifact/memory-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with Kotlin code, configuration, and shell command snippets when useful] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May tailor recommendations to locally stored Kotlin preferences under ~/Clawic/data/kotlin/ when present.] <br>

## Skill Version(s): <br>
1.0.3 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
