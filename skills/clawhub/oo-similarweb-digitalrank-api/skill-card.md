## Description:

Similarweb (similarweb.com). Use this skill for Similarweb requests that search, read, and report ranking, campaign, and subscription data through the OOMOL-connected Similarweb Digital Rank API service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect the live Similarweb connector schema, run authenticated read requests through the oo CLI, retrieve rank-tracker campaign details and top-sites rankings, and check remaining API usage allowance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote shell installer commands for the oo CLI.

Mitigation: Prefer vendor-documented, versioned, and verifiable installation steps, and review the installer before authenticating an OOMOL or Similarweb account.

Risk: The skill runs authenticated requests through a connected OOMOL and Similarweb account.

Mitigation: Use only accounts and API keys approved for the intended environment, inspect each live action schema before sending data, and avoid exposing sensitive request payloads.

## Reference(s):

- [ClawHub Similarweb Skill](https://clawhub.ai/oomol/skills/oo-similarweb-digitalrank-api)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Similarweb Connection](https://console.oomol.com/app-connections?provider=similarweb_digitalrank_api)
- [Similarweb Homepage](https://www.similarweb.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON request or response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect live action schemas before constructing Similarweb connector requests.]

## Skill Version(s):

1.0.3 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
