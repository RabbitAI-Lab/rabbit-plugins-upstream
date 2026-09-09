## Description:

ModelSelectorOpenClaw helps agents install, verify, repair, or uninstall a two-column provider/model picker enhancement for the OpenClaw Control UI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pondsi](https://clawhub.ai/user/pondsi)

### License/Terms of Use:

MIT

## Use Case:

Developers and OpenClaw users use this skill to replace a long flat chat model list with provider-first navigation, and to restore or remove that local UI patch after upgrades.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation modifies local OpenClaw Control UI files by injecting one script tag and copying a browser-side asset.

Mitigation: Install only on the intended local OpenClaw package directory, review the disclosed file changes first, and use the documented -Remove option to uninstall.

Risk: The injected browser script periodically makes a same-origin request to the Control UI root for update checking.

Mitigation: Use the skill only when that same-origin polling behavior is acceptable; uninstall with -Remove if the background check is not desired.

Risk: OpenClaw upgrades can overwrite dist/control-ui and remove the enhancement.

Mitigation: Re-run the idempotent installer after upgrades, or use an approved repair workflow outside this ClawHub artifact.

## Reference(s):

- [ModelSelectorOpenClaw README](README.md)
- [ModelSelectorOpenClaw Changelog](CHANGELOG.md)
- [ClawHub Skill Page](https://clawhub.ai/pondsi/skills/modelselectoropenclaw)

## Skill Output:

**Output Type(s):** [markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with PowerShell commands and JavaScript console checks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes reversible local OpenClaw Control UI patch guidance and verification steps.]

## Skill Version(s):

1.3.0 (source: frontmatter, changelog, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
