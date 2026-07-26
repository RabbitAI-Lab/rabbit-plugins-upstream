## Description: <br>
Helps agents manage Temu Europe product listings through LinkFox gateway scripts and reference docs for Partner EU product, SKU, inventory, compliance, sale-status, pre-sale, and delete APIs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Temu sellers, operators, and developers use this skill to query and update product listings for Temu Europe via LinkFox. It supports product discovery, detail and SKU lookup, stock edits, listing edits, compliance updates, sale-status changes, pre-sale changes, and deletion workflows. <br>

### Deployment Geography for Use: <br>
Europe for Temu EU product-management workflows. <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform account-impacting Temu product actions, including deletion, stock overwrite, full listing update, compliance edit, and sale-status changes. <br>
Mitigation: Require explicit human confirmation and review request payloads before running those operations against real stores. <br>
Risk: The skill handles LinkFox and Temu seller credentials and includes helpers for local token storage. <br>
Mitigation: Use least-privilege Temu tokens, keep token-store paths private, avoid raw token reveal or unmasked listing helpers, and rotate tokens if exposed. <br>
Risk: Saved LinkFox response files may contain sensitive product or store data. <br>
Mitigation: Clean up saved response files, restrict access to project output directories, and avoid sharing full JSON dumps unless needed. <br>


## Reference(s): <br>
- [LinkFox Temu Europe product API reference](references/api.md) <br>
- [Partner EU product API catalog](references/partner-eu-catalog.md) <br>
- [Temu access token authorization guide](references/access-token.md) <br>
- [Per-interface API reference index](references/apis/README.md) <br>
- [Temu Partner EU Manage Products documentation](https://partner-eu.temu.com/documentation?menu_code=2283b8dc7fcc42529633b0b41114aef8) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration, Files] <br>
**Output Format:** [Markdown guidance with Python command examples and JSON API responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scripts save complete LinkFox responses under ./linkfox/<date>/<session>/data and print either full JSON or a response summary depending on response size.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
