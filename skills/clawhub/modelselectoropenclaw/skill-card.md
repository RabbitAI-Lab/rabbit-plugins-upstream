## Description:

ModelSelectorOpenClaw installs, verifies, repairs, or removes a browser-side enhancement that turns OpenClaw Control UI's flat model picker into a two-column provider and model picker.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pondsi](https://clawhub.ai/user/pondsi)

### License/Terms of Use:

MIT License - MIT-style with mandatory attribution

## Use Case:

Developers and OpenClaw users use this skill to install or remove a local Control UI enhancement that makes model selection faster when many providers and models are configured.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill patches local OpenClaw Control UI files in the installed package directory.

Mitigation: Review the disclosed file changes before installation, keep the generated index.html.bak-pcl backup, and use the documented -Remove command to uninstall.

Risk: Open Control UI tabs may poll the same origin and reload after detecting a newer injected picker script.

Mitigation: Install or update when a Control UI reload is acceptable, and review the same-origin update behavior described in the artifact documentation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pondsi/skills/modelselectoropenclaw)
- [README](artifact/README.md)
- [CHANGELOG](artifact/CHANGELOG.md)
- [LICENSE](artifact/LICENSE)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline PowerShell and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces install, verification, repair, and uninstall guidance for a local OpenClaw Control UI patch.]

## Skill Version(s):

1.5.3 (source: server release metadata; artifact frontmatter and changelog show 1.5.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
