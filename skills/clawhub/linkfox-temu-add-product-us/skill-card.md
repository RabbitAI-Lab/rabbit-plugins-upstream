## Description: <br>
Helps agents use LinkFox's gateway and bundled scripts to publish and manage Temu Partner US product listings, including V2 add-product flows, category attributes, images, listing queries, edits, stock, and supply-price operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, operators, and developers use this skill to prepare and execute Temu US product-management workflows through LinkFox, including product creation, catalog lookup, image upload, inventory updates, and pricing checks. <br>

### Deployment Geography for Use: <br>
United States <br>

## Known Risks and Mitigations: <br>
Risk: Authenticated Temu product-management operations can create or modify listings, stock, pricing, migration state, and other commerce data. <br>
Mitigation: Use least-privilege Temu and LinkFox tokens, review commands and JSON payloads before execution, and avoid broad proxy calls unless the requested operation is clear. <br>
Risk: Tokens and API responses may be stored or printed in plaintext by the bundled scripts. <br>
Mitigation: Avoid sharing production tokens in chats or shell history, keep token-store and response directories out of source control, and delete or protect local output files after use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-add-product-us) <br>
- [API reference](references/api.md) <br>
- [Access token authorization](references/access-token.md) <br>
- [Authorization flow](references/authorization-flow.md) <br>
- [Partner US catalog](references/partner-us-catalog.md) <br>
- [Product publish APIs](references/product-publish-apis.md) <br>
- [Product query APIs](references/product-query-apis.md) <br>
- [Product edit APIs](references/product-edit-apis.md) <br>
- [Category and specification APIs](references/category-spec-apis.md) <br>
- [Stock and price APIs](references/stock-price-apis.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON files, API calls, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON request or response files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scripts save full LinkFox responses under a local linkfox session directory and may print small responses or summaries to stdout.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
