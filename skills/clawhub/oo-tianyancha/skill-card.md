## Description:

Tianyancha helps agents search and read company intelligence from Tianyancha through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Tianyancha action schemas and query company profiles, ownership, personnel, risk, news, tender, and identity verification data through the OOMOL oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables agents to query Tianyancha through an OOMOL account, which may require account connection and OOMOL billing.

Mitigation: Install and use it only when the agent should access Tianyancha through the user's OOMOL account, and review intended queries before execution.

Risk: Future connector actions or payloads could have write or destructive effects even though the artifact-backed actions are read/search oriented.

Mitigation: Inspect the live action schema before building payloads and require explicit user confirmation for any action marked write or destructive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-tianyancha)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Tianyancha homepage](https://www.tianyancha.com/data)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May instruct agents to inspect live connector schemas before issuing read/search company-data actions.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
