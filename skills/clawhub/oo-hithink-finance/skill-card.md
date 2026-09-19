## Description:

Provides agents with Tonghuashun Financial Data access for searching and retrieving A-share, index, fund, market, valuation, and financial statement data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external users use this skill to let an agent inspect Tonghuashun connector schemas and retrieve market, security, index, fund, valuation, and financial report data from a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Use a package-managed or otherwise verified oo CLI installation when possible, review OOMOL installation documentation first, and avoid running curl-to-bash or irm-to-iex commands blindly.

Risk: The connector requires an authenticated OOMOL account and a connected Tonghuashun Financial Data account.

Mitigation: Only connect the account when the user intends to use this data connector, and rely on OOMOL-managed credentials rather than handling raw tokens directly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-hithink-finance)
- [Tonghuashun Financial Data homepage](https://fuyao.aicubes.cn/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown guidance with bash, PowerShell, and JSON command examples; connector responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the oo CLI, an authenticated OOMOL account, and a connected Tonghuashun Financial Data account.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
