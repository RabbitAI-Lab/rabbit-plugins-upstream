## Description:

Operates VMware/Omnissa Horizon VDI through a Connection Server for desktop pools, RDS farms, published apps, sessions, machines, entitlements, health, events, statistics, and instant-clone image updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

IT help-desk and VDI operations teams use this skill to inspect Horizon environments and perform broker-layer actions such as session logoff, desktop reset, entitlement changes, and image pushes through CLI or MCP workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can disrupt users or infrastructure by logging off sessions, resetting or removing machines, canceling tasks, or pushing images across an entire desktop pool.

Mitigation: Use a read-only Horizon admin role by default, enable write-capable credentials only for intended maintenance, and review dry-run output before approving disruptive commands.

Risk: The generated password file stores an obfuscated b64 value, which is not encryption.

Mitigation: Prefer secret-manager environment injection for production credentials and restrict local credential files to the documented 0600 permissions.

Risk: Server-resolved provenance is unavailable for this release.

Mitigation: Verify the vmware-vdi package source and release provenance before production deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-vdi)
- [Capabilities reference](artifact/references/capabilities.md)
- [CLI reference](artifact/references/cli-reference.md)
- [Setup guide](artifact/references/setup-guide.md)
- [Source repository cited by artifact](https://github.com/vmware-skills/VMware-VDI)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured MCP guidance, dry-run review steps, and operational cautions for write actions.]

## Skill Version(s):

1.1.1 (source: server release metadata and artifact install command)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
