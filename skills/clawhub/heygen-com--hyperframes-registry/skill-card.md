## Description:

Search, install, and wire HyperFrames registry blocks and components, and guide agents through contributing new registry items.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video engineers use this skill to find reusable HyperFrames visuals, install blocks or components, wire them into compositions, and prepare new registry items for upstream contribution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HyperFrames CLI commands may write project files, fetch registry content, or publish previews.

Mitigation: Review proposed commands before execution, run them in the intended project or a sandbox, and inspect written files before committing.

Risk: The feedback command can send failed search details externally, which may expose confidential project terms.

Mitigation: Require explicit approval before running feedback and redact sensitive search-miss or wanted values.

Risk: Mutable npx command execution can pull changing package versions.

Mitigation: Prefer pinned or local package versions, or run commands in a disposable sandbox.

Risk: The preview image upload path is intended only for HeyGen internal contributors with a named AWS profile.

Mitigation: Use the PR attachment path for external contributors and reserve the upload script for authorized internal users.

## Reference(s):

- [HyperFrames Registry on ClawHub](https://clawhub.ai/heygen-com/skills/hyperframes-registry)
- [Registry Discovery](artifact/references/discovery.md)
- [Install Locations](artifact/references/install-locations.md)
- [Wiring Blocks](artifact/references/wiring-blocks.md)
- [Wiring Components](artifact/references/wiring-components.md)
- [Contributing a Block or Component](artifact/references/contributing.md)
- [Templates](artifact/references/templates.md)
- [Component Quality Bar](artifact/references/component-quality-bar.md)
- [HyperFrames Registry Manifest](https://raw.githubusercontent.com/heygen-com/hyperframes/main/registry/registry.json)
- [HyperFrames Configuration Schema](https://hyperframes.heygen.com/schema/hyperframes.json)
- [GSAP CDN](https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline shell commands, HTML snippets, JSON configuration, and implementation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose project file changes, registry installation commands, preview commands, and contribution workflow steps.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
