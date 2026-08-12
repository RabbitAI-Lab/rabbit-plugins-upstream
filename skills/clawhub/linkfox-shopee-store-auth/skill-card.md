## Description:

Helps agents generate Shopee ERP or Ads OAuth authorization URLs, list authorized stores, and check authorization status through LinkFox.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, e-commerce operators, and agents use this skill to prepare Shopee ERP or Ads authorization, inspect authorized stores, and provide store identifiers for downstream Shopee workflows without exposing raw access tokens.

### Deployment Geography for Use:

Global, with documented Shopee authorization regions cn, global, and br.

## Known Risks and Mitigations:

Risk: The skill requires LinkFox API-key access and can guide account onboarding and paid billing recovery.

Mitigation: Install and run it only in trusted workspaces, keep API keys private, and review any onboarding or payment action before proceeding.

Risk: Generated Shopee authorization URLs and saved response JSON files can expose sensitive account or store context.

Mitigation: Treat authorization URLs and saved LinkFox outputs as sensitive, avoid sharing them, and review or delete local linkfox/cache outputs after use.

Risk: Endpoint environment variables can redirect requests away from official LinkFox hosts.

Mitigation: Keep LinkFox endpoint environment variables pinned to official hosts unless intentionally testing in a controlled environment.

Risk: Shopee ERP and Ads authorizations are separate, so using the wrong app type can cause failed or incorrect downstream workflows.

Mitigation: Confirm appType and match shopId or merchantId with the intended ERP or Ads authorization before downstream calls.

## Reference(s):

- [API parameter and field reference](artifact/references/api.md)
- [Authentication and billing onboarding guide](artifact/references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-auth)

## Skill Output:

**Output Type(s):** [guidance, shell commands, JSON, files, configuration]

**Output Format:** [Markdown guidance with JSON API responses and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts save full API responses under a LinkFox session data directory; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
