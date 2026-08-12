## Description:

Helps agents manage Temu Europe marketplace products through LinkFox, including product and SKU queries, stock changes, listing edits, deletion, sale status, category and property checks, compliance updates, external codes, and video cover retrieval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Temu EU sellers, operators, and support agents use this skill to inspect and manage live product catalog records, SKU stock, publication state, compliance details, and related marketplace metadata through LinkFox-mediated Partner EU API calls.

### Deployment Geography for Use:

Europe (Temu EU / Partner EU workflows)

## Known Risks and Mitigations:

Risk: The skill handles LinkFox and Temu access tokens and merchant product data.

Mitigation: Use only in trusted seller workspaces, avoid placing tokens in shell history or source control, and control local token file permissions and retention.

Risk: Some scripts can modify or delete live product listings, stock, sale status, and compliance information.

Mitigation: Require explicit human confirmation and review request payloads before running delete, full update, stock, off-shelf, pre-sale, or compliance actions.

Risk: Gateway endpoint override environment variables can redirect requests.

Mitigation: Restrict who can set endpoint override variables and verify configured endpoints before sending real seller credentials or catalog data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-manage-product-eu)
- [API reference](references/api.md)
- [Partner EU Manage Product catalog](references/partner-eu-catalog.md)
- [Temu access token guide](references/access-token.md)
- [Onboarding and auth recovery](references/onboarding.md)
- [Temu Partner EU Manage Product documentation](https://partner-eu.temu.com/documentation?menu_code=7289390cfd724be4a196f11ebe45a896)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples, shell commands, and saved JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts write full API responses under a local linkfox session data directory and print either full JSON or a concise summary depending on response size.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
