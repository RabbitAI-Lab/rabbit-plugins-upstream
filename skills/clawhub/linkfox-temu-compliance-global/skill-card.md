## Description:

Temu全球站-合规 helps agents use LinkFox gateway scripts and references for Temu Global product compliance APIs, including compliance metadata, label queries, certification upload/query flows, and real-image upload support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Temu operators, developers, and agent workflows use this skill to prepare and run product compliance API calls for Global site catalogs through LinkFox, including querying required compliance metadata, checking certification requirements, uploading supporting files or real images, and saving API responses for later inspection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes broader LinkFox and Temu account, token, billing, proxy, and persistence capabilities than a narrow compliance wrapper.

Mitigation: Install it only when a broad LinkFox/Temu operator tool is needed, and restrict use to trusted environments and expected LinkFox gateway URLs.

Risk: The skill handles LinkFox API keys and Temu access tokens, and local helper scripts can save or reveal tokens.

Mitigation: Treat all LinkFox API keys and Temu access tokens as secrets, avoid raw token export/list commands unless necessary, and review local token storage under ~/.linkfox.

Risk: The skill persists full API responses and session metadata to local linkfox directories.

Mitigation: Review saved response files before sharing workspaces or logs, especially when responses may contain shop, product, certification, or account data.

Risk: The onboarding flow includes billing and payment-order operations.

Mitigation: Confirm any payment order manually and avoid unattended payment or balance-recovery flows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-compliance-global)
- [API reference](artifact/references/api.md)
- [Access token guide](artifact/references/access-token.md)
- [Compliance API index](artifact/references/apis/README.md)
- [Partner Global catalog](artifact/references/partner-global-catalog.md)
- [Temu Partner Global API documentation](https://partner-global.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=fd12bdf5cb364366bdef85aad9cd8e48)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON files, API call guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON request/response data written to local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts save full responses under a linkfox session directory and print either the full JSON or a concise summary depending on response size.]

## Skill Version(s):

1.0.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
