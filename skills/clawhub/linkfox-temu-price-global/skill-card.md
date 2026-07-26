## Description: <br>
Temu Global pricing API skill for non-US/EU marketplaces that routes LinkFox gateway calls for price orders, recommended prices, SKU supply-price lists, and batch SKU price updates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Temu sellers, commerce operators, and developer agents use this skill to query and update non-US/EU Temu Global product pricing through LinkFox gateway scripts. It supports price-order lookup, recommended and estimated supply prices, SKU supply-price lists, and controlled batch SKU price changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles Temu seller access tokens and LinkFox gateway credentials. <br>
Mitigation: Use dedicated least-privilege credentials, run only on trusted machines, keep token files out of shared workspaces, and rotate or revoke tokens when access is no longer needed. <br>
Risk: Batch SKU price-change calls can modify live marketplace prices. <br>
Mitigation: Require manual review of goods IDs, SKU IDs, currency, and new supplier prices before calling the batch price-change endpoint. <br>
Risk: Gateway responses and downloaded files may be stored locally. <br>
Mitigation: Review saved files under local LinkFox paths, remove sensitive outputs after use, and avoid pasting stored responses containing secrets into unrelated prompts or tools. <br>
Risk: Broad proxy and file-download behavior can reach external Temu and LinkFox services. <br>
Mitigation: Use only the documented Temu Global pricing operations, verify requested endpoints and parameters, and inspect downloaded files before opening or sharing them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-price-global) <br>
- [API gateway reference](references/api.md) <br>
- [Temu access token guide](references/access-token.md) <br>
- [Price API index](references/apis/README.md) <br>
- [Partner Global catalog](references/partner-global-catalog.md) <br>
- [Temu Partner Global documentation](https://partner-global.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands, Python script invocations, and JSON request/response payloads.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scripts save full gateway responses under local LinkFox session directories and may print summaries for large responses.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
