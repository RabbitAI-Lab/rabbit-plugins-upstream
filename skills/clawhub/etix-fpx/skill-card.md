## Description:

Query etix.com event, venue, and performer discovery data from a shell with the fpx CLI through a signed-in browser tab, without running the etix-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to fetch public Etix discovery data, resolve event or venue ids, and extract event or venue details through fpx when direct HTTP requests are blocked. The skill is scoped to anonymous public discovery reads and excludes Etix login, seller credentials, and ticket purchases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a domain-scoped browser bridge and persistent pairing to fetch Etix pages.

Mitigation: Confirm the Transporter/fpx bridge is approved only for etix.com and that persistent pairing is acceptable before installing or running the skill.

Risk: The skill is intended for public discovery data and explicitly excludes credentialed or financial actions.

Mitigation: Do not use Etix login, seller credentials, OAuth2 venue or box-office credentials, or ticket-purchase flows with this skill.

Risk: HTML responses can still be DataDome interstitial pages even when the fetch command exits successfully.

Mitigation: Check fetched HTML for DataDome challenge text such as captcha-delivery before parsing or trusting extracted event details.

## Reference(s):

- [Etix consumer endpoints for fpx](references/etix-endpoints.md)
- [extract-datalayer.mjs](references/extract-datalayer.mjs)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, jq examples, and JavaScript snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces guidance for one-shot fpx calls and local parsing of JSON, HTML JSON-LD, microdata, and dataLayer fields.]

## Skill Version(s):

0.6.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
