## Description:

Safe DNS record management for Namecheap domains. Fetch, add, remove, backup, and restore DNS records with automatic safety checks and dry-run mode. Prevents accidental DNS record wipeout via the Namecheap API's destructive setHosts method.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarekbird](https://clawhub.ai/user/jarekbird)

### License/Terms of Use:

MIT

## Use Case:

Developers and operators use this skill to inspect, add, remove, back up, verify, and restore DNS records for Namecheap-managed domains while previewing changes before applying them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make high-impact DNS changes through Namecheap credentials.

Mitigation: Use a least-privilege API key if available, review every proposed command, and prefer dry runs before applying DNS changes.

Risk: Unsafe domain handling around live DNS checks may expose shell execution risk.

Mitigation: Run only with trusted domain names until domain validation and shell-safe dig execution are fixed.

Risk: Backup and restore handling may allow an unexpected backup path or restore target.

Mitigation: Keep backups in a private, controlled directory and manually confirm the backup domain matches the intended restore domain until backup containment, schema validation, and restore target confirmation are fixed.

Risk: Namecheap DNS updates can replace records, including records invisible to the API.

Mitigation: Run the verify command before destructive operations, inspect ghost record warnings, and use force only when the listed records are intentionally being removed.

## Reference(s):

- [Namecheap API Documentation](https://www.namecheap.com/support/api/)
- [Namecheap Domains DNS API Methods](https://www.namecheap.com/support/api/methods/domains-dns/)
- [Namecheap API Access Settings](https://ap.www.namecheap.com/settings/tools/apiaccess/)
- [ClawHub Skill Page](https://clawhub.ai/jarekbird/skills/namecheap-dns)
- [Publisher Profile](https://clawhub.ai/user/jarekbird)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces human-reviewable command sequences and safety guidance for DNS operations.]

## Skill Version(s):

1.1.0 (source: server release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
