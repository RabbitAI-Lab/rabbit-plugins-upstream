## Description:

Ringba (ringba.com). Use this skill for Ringba requests that search and read data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Ringba account data, campaigns, phone numbers, and publishers through the oo CLI connector without handling raw Ringba tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run oo connector commands against a connected Ringba account.

Mitigation: Use it for account data lookups and require explicit confirmation before running any connector action tagged write or destructive.

Risk: The skill may require installing or signing into the oo CLI before connector actions can run.

Mitigation: Only perform setup or sign-in steps after a command fails with an installation, authentication, connection, or billing error.

## Reference(s):

- [Ringba Skill Page](https://clawhub.ai/oomol/skills/oo-ringba)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Ringba Homepage](https://www.ringba.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command-output references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands inspect live connector schemas before constructing payloads.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
