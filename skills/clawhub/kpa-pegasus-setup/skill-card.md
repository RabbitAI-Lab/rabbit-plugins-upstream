## Description:

Guides setup, troubleshooting, and optimization of Pegasus, RetroArch, and PPSSPP on the KONKR Pocket ADVANCE handheld, including library checks and device-specific configuration fixes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT-0

## Use Case:

KPA owners and Android handheld setup maintainers use the skill to install and tune Pegasus, RetroArch, and PPSSPP, troubleshoot device-specific behavior, and check or clean their game libraries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Download and launch paths may be unsafe.

Mitigation: Review the source and each command before execution; avoid installation until these paths have been reviewed or fixed.

Risk: Cleanup operations may permanently remove files.

Mitigation: Start with a read-only inventory and impact review, require explicit confirmation, keep a recovery path, and clean in small verified batches.

Risk: The temporary local HTTP server may be reachable by other network clients.

Mitigation: Use it only on a trusted local network, restrict access where possible, restore the normal source setting, and stop the server immediately after use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lisong2003-lgtm/skills/kpa-pegasus-setup)
- [Project repository link cited in the artifact (not server-verified provenance)](https://github.com/lisong2003-lgtm/kpa-pegasus-setup)
- [HARD_RULES.md](references/HARD_RULES.md)
- [PLAYBOOK.md](references/PLAYBOOK.md)
- [VERIFICATION.md](references/VERIFICATION.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with shell commands, configuration examples, and script references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Device-specific setup and troubleshooting guidance; some steps modify device files or settings.]

## Skill Version(s):

2.0.2 (source: frontmatter, changelog; released 2026-11-13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
