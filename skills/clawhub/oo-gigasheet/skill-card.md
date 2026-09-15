## Description:

Gigasheet (gigasheet.com). Use this skill for Gigasheet requests involving search, reading data, dataset metadata, exports, storage usage, and enrichment credits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Gigasheet through an OOMOL-connected account, including searching library metadata, describing datasets, listing exports, and checking usage information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that could execute unverified scripts.

Mitigation: Install the oo CLI through a verified official method, inspect or verify installer integrity where possible, and do not let an agent automatically run curl-to-bash or irm-to-iex commands.

Risk: Using the connector can route Gigasheet read access through OOMOL.

Mitigation: Connect Gigasheet only after reviewing the account, scopes, and data access expectations for the OOMOL connector.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-gigasheet)
- [Gigasheet Homepage](https://www.gigasheet.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI and live connector schemas before action execution.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
