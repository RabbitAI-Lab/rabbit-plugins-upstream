## Description: <br>
Helps agents operate rented virtual private servers across provider selection, first boot, access recovery, snapshots, resizing, firewalls, incidents, outbound mail, billing, backups, and migrations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and infrastructure-focused users use this skill to choose, provision, recover, secure, resize, migrate, and document VPS hosts while keeping local runbooks and inventory current. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local infrastructure notes can expose hostnames, IP addresses, provider accounts, exposure maps, and spend history if the local data directory is shared or compromised. <br>
Mitigation: Keep the Clawic data paths private, review generated runbooks before sharing, and store only credential pointers rather than secret values. <br>
Risk: VPS operations can include irreversible provider actions such as rebuilds, destroys, disk growth, address release, and snapshot deletion. <br>
Mitigation: Require explicit user confirmation, state blast radius and fallback path before action, and verify backups or recovery access before destructive changes. <br>
Risk: Pasted terminal logs, runbooks, or environment files may contain private keys, passwords, API tokens, backup passphrases, or recovery codes. <br>
Mitigation: Strip secret values before writing durable notes and replace them with pointers such as keychain, password-manager, file, environment, or vault references. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/vps) <br>
- [Skill homepage](https://clawic.com/skills/vps) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, structured tables, and local file update guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May maintain local VPS inventory, runbooks, exposure notes, spend records, and provider-account pointers under declared Clawic data paths; credentials are represented only as pointers.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
