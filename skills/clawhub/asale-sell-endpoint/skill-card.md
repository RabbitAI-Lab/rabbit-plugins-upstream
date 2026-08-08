## Description:

Sell a custom OpenAI-compatible endpoint on the asale market: probe it, connect it as an account, and price it above what its own tokens cost.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect a custom OpenAI-compatible API endpoint to the asale market, validate it through the local daemon, set selling terms, and review status before making it available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer runs live remote scripts without visible integrity checks.

Mitigation: Review the installer before running it and prefer a verified release or signed installer when the publisher provides one.

Risk: Connecting a custom endpoint spends and stores the user's API key for marketplace use.

Mitigation: Confirm the endpoint URL, API key, pricing floor, concurrency, and any token cap with the user before connecting the endpoint.

Risk: A price floor below the endpoint's token cost can create loss-making sales.

Mitigation: Set the minimum ratio from the endpoint's actual token pricing before enabling selling.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/asale-sell-endpoint)
- [asale homepage](https://asale.ai)
- [asale source repository](https://github.com/asale-ai/asale)
- [Unix installer](https://asale.ai/dl/install.sh)
- [Windows installer](https://asale.ai/dl/install.ps1)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API Calls]

**Output Format:** [Markdown with inline bash code blocks and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces operational guidance for a local daemon workflow; it should confirm endpoint details before commands that store API keys.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter reports 0.2.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
