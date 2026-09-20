## Description:

TikHub helps agents inspect TikHub action schemas and run TikHub search, read, usage, pricing, and endpoint actions through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to query TikHub data, discover supported endpoints, check account usage or pricing, and invoke functional TikHub APIs with schemas verified before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote shell installer commands for the oo CLI.

Mitigation: Review installer commands before running them, prefer verified vendor documentation or pinned signed releases, and avoid elevated shells for curl|bash or irm|iex installation.

Risk: Running actions uses the connected TikHub account and may expose account or API-key information or consume paid TikHub/OOMOL usage.

Mitigation: Use an appropriate connected account, review action scope and payloads before execution, and check pricing or daily usage when cost exposure matters.

Risk: Incorrect endpoint payloads can produce failed or unintended TikHub API calls.

Mitigation: Fetch the live action schema before constructing payloads and confirm any write or destructive action details with the user before execution.

## Reference(s):

- [ClawHub TikHub skill](https://clawhub.ai/oomol/skills/oo-tikhub)
- [TikHub homepage](https://tikhub.io/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the oo CLI, an authenticated OOMOL account, and a connected TikHub API key; endpoint schemas are checked before action payloads are sent.]

## Skill Version(s):

1.0.6 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
