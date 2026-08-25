## Description:

Provides actionable workflows and decision support to convert web apps into Android-installable apps using PWA, Capacitor with CI, or Trusted Web Activities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to choose and execute a practical path for converting a web app or website into an Android-installable experience. It is especially oriented toward Termux environments where native Android build tooling is unavailable locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated PWA, service worker, or GitHub Actions files may change project behavior or the build pipeline.

Mitigation: Review generated manifest, service worker, and CI workflow files before committing or pushing changes.

Risk: Secrets could be exposed if credentials are committed while setting up deployment or CI.

Mitigation: Do not commit secrets; use repository or CI secret storage when credentials are required.

Risk: Attempting native Android builds directly in Termux can waste time on unsupported Java, Gradle, or Android SDK toolchains.

Mitigation: Use CI for native Android builds and reserve local Termux work for web, PWA, and project configuration steps.

## Reference(s):

- [Web-to-APK Options Analysis](references/options-analysis.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON, YAML, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose PWA files, Capacitor setup commands, GitHub Actions workflow configuration, and decision guidance for Android packaging paths.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
