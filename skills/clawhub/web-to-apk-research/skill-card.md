## Description:

Provides actionable workflows and decision support to convert web apps into Android-installable apps using PWA, Capacitor with CI, or Trusted Web Activities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to choose and execute a practical path for turning a web project into an Android-installable experience, especially when working from Termux without local Java, Gradle, or Android SDK tooling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may guide an agent to modify a web project and add a GitHub Actions workflow for APK builds.

Mitigation: Review generated project files and CI workflow changes before committing or pushing them.

Risk: CI-based APK builds can run in repositories that also contain secrets or production deployment workflows.

Mitigation: Inspect workflow permissions, triggers, and secret usage before enabling the build workflow.

Risk: PWA and Trusted Web Activity paths depend on HTTPS, service worker behavior, and, for Play Store distribution, Digital Asset Links setup.

Mitigation: Verify HTTPS hosting, install behavior, offline behavior, and domain association before distributing the app.

## Reference(s):

- [Web-to-APK Options Analysis](references/options-analysis.md)
- [ClawHub Skill Page](https://clawhub.ai/pmuhammadagus-byte/skills/web-to-apk-research)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline JSON, YAML, HTML, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose web project changes and CI workflow files; user confirmation is required before execution.]

## Skill Version(s):

2.0.0 (source: ClawHub release metadata, artifact _meta.json, and SKILL.md metadata.openclaw)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
