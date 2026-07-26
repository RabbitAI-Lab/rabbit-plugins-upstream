## Description: <br>
Calls Shopee Open Platform Public APIs through LinkFox scripts for partner shops, merchants, OAuth token exchange, token refresh, resend-code tokens, and IP range lookup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and e-commerce operators use this skill to call Shopee Public module endpoints for authorized shop and merchant lookup, token exchange and refresh, resend-code token retrieval, and Shopee IP range discovery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review says token-related API requests and responses are saved locally in full without redaction or retention controls. <br>
Mitigation: Use only in trusted workspaces, avoid shared machines, inspect generated linkfox data files after use, and delete saved token-related responses when they are no longer needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-public) <br>
- [Shopee Public API Reference](references/api.md) <br>
- [Shopee Open Platform Public API index](https://open.shopee.com/documents/v2/v2.public.get_shops_by_partner?module=104&type=1) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with Python shell commands and saved JSON API responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes complete API responses to a local linkfox session data directory and prints full JSON or a summary based on response size.] <br>

## Skill Version(s): <br>
1.0.3 (source: server evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
