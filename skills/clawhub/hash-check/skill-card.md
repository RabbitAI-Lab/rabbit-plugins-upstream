## Description:

Generates and checks SHA-256 manifests for directories so an agent can help verify file integrity after download, transfer, or storage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and other external users can use this skill to generate or compare directory hash manifests as part of routine integrity checks. It is most relevant when files have been downloaded, moved, or handed off and the user wants a repeatable SHA-256 comparison.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review says documented dry-run safeguards do not match the script behavior, and generation mode writes immediately.

Mitigation: Run only in a test copy or backed-up directory until the user has verified the command behavior for the target release.

Risk: The security review says the manifest option can overwrite user-writable files.

Mitigation: Use a simple manifest filename in the target directory and avoid paths that could overwrite existing files.

Risk: The security review says check mode may still pass when extra files have been added.

Mitigation: Review any reported added files separately instead of treating a pass result as proof that the directory contains only expected files.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhaoxinghua09-cell/skills/hash-check)
- [Publisher Profile](https://clawhub.ai/user/zhaoxinghua09-cell)
- [Project Homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses rc=0 for pass, rc=1 for findings, and rc=2 for usage or environment errors.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
