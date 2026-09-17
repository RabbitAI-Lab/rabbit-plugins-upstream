## Description:

Use this skill to operate AbuseIPDB for reading, creating, and updating data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security operators use this skill to query AbuseIPDB through an OOMOL-connected account for IP reputation checks, blacklist data, CIDR inspection, and report lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions may ask users to execute unverified remote installer scripts.

Mitigation: Install the oo CLI only after reviewing the installation path; prefer a package manager or a verified, version-pinned installer with checksum or signature validation.

Risk: Actions tagged as write can change data through the connected AbuseIPDB account.

Mitigation: Confirm the exact payload and effect with the user before executing any action marked as write.

## Reference(s):

- [ClawHub AbuseIPDB Skill](https://clawhub.ai/oomol/skills/oo-abuseipdb)
- [AbuseIPDB Homepage](https://www.abuseipdb.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline bash code blocks and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before command payload construction.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
