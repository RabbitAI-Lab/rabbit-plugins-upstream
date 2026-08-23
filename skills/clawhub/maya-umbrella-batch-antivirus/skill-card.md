## Description:

Scan/clean Maya scene malware on Windows. Use for Maya杀毒, Maya病毒扫描, Maya病毒查杀, 清理Maya病毒, 病毒查杀, Maya antivirus, Maya virus scan/removal; not general antivirus.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, technical artists, and pipeline operators use this skill to scan Autodesk Maya .ma and .mb scene files for Maya Umbrella malware and, after explicit approval, run bounded cleanup with preserved reports and backups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The portable CLI is downloaded and installed before use.

Mitigation: Confirm the exact release version, checksum asset, and LOCALAPPDATA destination before installation; run the installer as the current user and reject checksum or capability validation failures.

Risk: Cleanup force-saves affected Maya scenes in place.

Mitigation: Review the scan report, affected file list, source hashes, backup behavior, Maya version, and report digest before explicit cleanup approval.

Risk: A broad or drifting scan scope could clean files the user did not approve.

Mitigation: Resolve exact paths, require repeated --path arguments, bind cleanup to the approved report hash and source hashes, and run a separate post-clean scan over the same accepted scope.

## Reference(s):

- [Operation Contract](references/operation-contract.md)
- [ClawHub Skill Page](https://clawhub.ai/loonghao/skills/maya-umbrella-batch-antivirus)
- [maya_umbrella_scanner Release Repository](https://github.com/loonghao/maya_umbrella_scanner)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with PowerShell command examples and JSON report references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Windows-only workflow for Autodesk Maya scene files; cleanup depends on explicit scan-report approval, local Maya, backups, and post-clean verification.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
