## Description: <br>
Manages Amazon store listings through LinkFox by retrieving, searching, creating, updating, deleting listings, checking listing restrictions, and fetching product type definitions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Amazon sellers, marketplace operators, and their agents use this skill to inspect listings, validate listing constraints, and make controlled listing changes through LinkFox-authenticated SP-API calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can modify or delete live Amazon listings through PATCH, PUT, and DELETE operations. <br>
Mitigation: Require explicit user confirmation before mutation operations, especially deletion, and review SKU, sellerId, marketplaceIds, productType, and patch or attributes payloads before execution. <br>
Risk: Full API responses are saved locally and may contain seller, listing, or operational data. <br>
Mitigation: Review saved response paths, avoid committing LinkFox response files, and apply local retention and access controls appropriate for seller data. <br>
Risk: Use requires local agent access to LinkFox and Amazon seller listing credentials. <br>
Mitigation: Install only in environments trusted to access those credentials and scope credential availability to the intended task and workspace. <br>


## Reference(s): <br>
- [Amazon Listings API reference](references/api.md) <br>
- [Amazon getListingsItem](https://developer-docs.amazon.com/sp-api/reference/getlistingsitem) <br>
- [Amazon searchListingsItems](https://developer-docs.amazon.com/sp-api/reference/searchlistingsitems) <br>
- [Amazon patchListingsItem](https://developer-docs.amazon.com/sp-api/reference/patchlistingsitem) <br>
- [Amazon putListingsItem](https://developer-docs.amazon.com/sp-api/reference/putlistingsitem) <br>
- [Amazon deleteListingsItem](https://developer-docs.amazon.com/sp-api/reference/deletelistingsitem) <br>
- [Amazon getListingsRestrictions](https://developer-docs.amazon.com/sp-api/reference/getlistingsrestrictions) <br>
- [Amazon searchDefinitionsProductTypes](https://developer-docs.amazon.com/sp-api/reference/searchdefinitionsproducttypes) <br>
- [Amazon getDefinitionsProductType](https://developer-docs.amazon.com/sp-api/reference/getdefinitionsproducttype) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Files, Shell commands, Guidance] <br>
**Output Format:** [JSON files with stdout summaries and Markdown guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full API responses are saved to a LinkFox session data directory; small responses may also be printed inline.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
