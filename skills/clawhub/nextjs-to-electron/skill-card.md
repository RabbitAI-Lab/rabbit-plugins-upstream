## Description:

Use when converting a Next.js static export into a Windows Electron desktop app, especially for offline machines without WebView2.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rockbenben](https://clawhub.ai/user/rockbenben)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this playbook to convert a client-side Next.js static export into a Windows Electron desktop app that can run offline. It guides the export, desktop integration, packaging, and release workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The supplied workflow template can publish GitHub releases and replace release assets.

Mitigation: Review the release workflow, target repository, tag, and assets before running it, and grant only the repository permissions needed for the release.

Risk: The security analysis is incomplete and does not establish that every component is safe.

Mitigation: Review the components not fully covered by the scan before using or adapting the skill.

## Reference(s):

- [Skill homepage](https://github.com/rockbenben/aishort-skills/tree/main/skills/nextjs-to-electron)
- [ClawHub skill page](https://clawhub.ai/rockbenben/skills/nextjs-to-electron)
- [Electron releases](https://releases.electronjs.org/releases.json)
- [Node.js release schedule](https://raw.githubusercontent.com/nodejs/Release/main/schedule.json)
- [Electron files and examples](artifact/electron-files.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with code and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Adapts steps and examples to the target Next.js project.]

## Skill Version(s):

1.1.15 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
