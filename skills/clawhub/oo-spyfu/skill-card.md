## Description:

SpyFu (spyfu.com). Use this skill for ANY SpyFu request — searching and reading data. Whenever a task involves SpyFu, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate SpyFu through an OOMOL-connected account for SEO and PPC research, including domain, keyword, competitor, SERP, ad-history, top-page, and usage analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read SpyFu analytics and account usage data through an OOMOL-connected account.

Mitigation: Confirm the user intends to query the connected SpyFu account and keep returned account or usage data scoped to the request.

Risk: First-time setup may require installing the oo CLI and connecting SpyFu through OOMOL.

Mitigation: Before installation or account connection, confirm the user trusts OOMOL's oo CLI and is comfortable linking the SpyFu account.

Risk: Live connector actions depend on the current schema and may reject stale or malformed payloads.

Mitigation: Inspect the live action schema before constructing payloads and send JSON that matches the connector contract.

## Reference(s):

- [SpyFu homepage](https://www.spyfu.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-spyfu)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline bash code blocks and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include SpyFu analytics returned by the oo CLI and OOMOL connector execution metadata.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
