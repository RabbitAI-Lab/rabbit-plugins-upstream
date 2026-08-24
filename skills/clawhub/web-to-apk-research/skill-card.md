## Description:

Provides actionable workflows and decision support for converting web apps into Android installable apps using PWA, Capacitor with CI, or Trusted Web Activities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to choose and apply a practical path for turning a website or web app into an Android installable app, especially when working from Termux without local Android build tooling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may add PWA, Capacitor, or GitHub Actions files to a web project.

Mitigation: Review generated project changes before committing or pushing them.

Risk: A generated CI workflow could expose project behavior or interact with repository secrets.

Mitigation: Review the GitHub Actions workflow before enabling it, especially for public repositories or apps with secrets.

## Reference(s):

- [Web-to-APK Options Analysis](references/options-analysis.md)
- [ClawHub Skill Page](https://clawhub.ai/pmuhammadagus-byte/skills/web-to-apk-research)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with JSON, YAML, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose PWA files, Capacitor setup, or GitHub Actions workflow changes when the user confirms the target path.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact metadata reports internal OpenClaw version 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
