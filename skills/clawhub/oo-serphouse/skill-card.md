## Description:

SERPHouse helps agents use an OOMOL-connected SERPHouse account to inspect connector schemas and run read-oriented search, account, domain, language, and location actions through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to query SERPHouse data and run synchronous web SERP searches through an existing OOMOL connection without handling raw SERPHouse tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path can lead an agent to execute remote installer scripts for the oo CLI.

Mitigation: Do not allow an agent to run installer commands automatically; install the oo CLI only from a trusted official source with version pinning and checksum or signature verification after reviewing the installer.

Risk: SERPHouse actions use the connected account and may consume account credit during searches.

Mitigation: Use account_info when needed to check credit status, confirm user intent before broad searches, and stop on billing or insufficient-credit errors.

## Reference(s):

- [ClawHub SERPHouse skill page](https://clawhub.ai/oomol/skills/oo-serphouse)
- [SERPHouse homepage](https://www.serphouse.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured JSON action responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful action responses include connector data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
