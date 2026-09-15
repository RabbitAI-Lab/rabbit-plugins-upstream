## Description:

Sif (sif.com). Use this skill for ANY Sif request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Sif through an OOMOL-connected account, inspect live connector schemas, and run Amazon market, keyword, competitor, ASIN, demand, trend, and opportunity analysis actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends running a remote installer directly, which the security review flagged for manual review.

Mitigation: Use an official versioned installer or package-manager flow with checksum or signature verification, and do not let an agent run the remote installer automatically.

Risk: Sif analysis actions may consume Sif points.

Mitigation: Check action costs and billing state before running analysis actions that incur points.

Risk: Write or destructive Sif actions could change or remove data if added to the connector.

Mitigation: Inspect the live action schema and confirm the exact payload and effect with the user before running tagged write or destructive actions.

## Reference(s):

- [Sif ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-sif)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Sif Homepage](https://www.sif.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return structured connector JSON containing data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
