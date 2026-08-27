## Description:

Generates complete Android projects for CodeAssist using Kotlin, Jetpack Compose, Material 3, native module.toml configuration, and bundled dependency templates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antonio338854](https://clawhub.ai/user/antonio338854)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create Android app project skeletons and Kotlin Compose source files that can be imported into CodeAssist and built on-device. It is intended for requests to generate CodeAssist-compatible Android apps without Gradle.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated Android projects may include permissions, backup settings, storage access, networking, or cleartext traffic settings that affect app security and privacy.

Mitigation: Review the generated AndroidManifest.xml and related configuration before building, testing, or shipping the app.

Risk: Generated project files and packaged ZIP archives are created in the workspace.

Mitigation: Inspect generated files before import or distribution and keep only the project artifacts intended for the user.

## Reference(s):

- [CodeAssist Kotlin + Compose skill page](https://clawhub.ai/antonio338854/skills/codeassist-kotlin-compose)
- [Publisher profile](https://clawhub.ai/user/antonio338854)
- [Dependencies and APIs](references/dependencies.md)
- [Config templates](references/config-templates.md)

## Skill Output:

**Output Type(s):** [Code, Files, Shell commands, Configuration instructions, Markdown]

**Output Format:** [Markdown guidance plus Kotlin source, Android resource files, module.toml configuration, and CodeAssist project ZIP structure]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CodeAssist native Android project layout with bundled dependency metadata and no Gradle files.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
