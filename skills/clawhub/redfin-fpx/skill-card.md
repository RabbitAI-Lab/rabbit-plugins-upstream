## Description:

Helps agents query Redfin listings, property details, market data, and signed-in saved homes or searches through a paired browser and the fpx CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can ask an agent to find US homes, inspect listings and property history, review market information, or retrieve their own saved homes and searches when signed in to Redfin.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: A paired browser tab can make Redfin requests using the user's session.

Mitigation: Install only if comfortable granting fpx this access and pair only with an intended Redfin tab.

Risk: Saved homes and saved searches are personal account data when signed in.

Mitigation: Request saved-account information only when the user explicitly wants it used.

## Reference(s):

- [Redfin stingray endpoint reference](references/stingray-endpoints.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [Redfin FPX on ClawHub](https://clawhub.ai/chrischall/skills/redfin-fpx)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell examples and summarized Redfin data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Saved homes and searches require a signed-in Redfin session.]

## Skill Version(s):

1.1.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
