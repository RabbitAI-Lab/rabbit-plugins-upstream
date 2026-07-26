## Description: <br>
Helps agents manage Temu US product pricing through LinkFox, including price-order queries, batch SKU base-price changes, recommended price queries, and base-price estimates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and Temu marketplace operators use this skill to prepare and run LinkFox-backed Temu US pricing workflows, including querying price orders, estimating base prices, and changing SKU supply/base prices. <br>

### Deployment Geography for Use: <br>
Global, limited to Temu US marketplace pricing workflows. <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive LinkFox and Temu seller tokens and can perform pricing operations. <br>
Mitigation: Pass tokens only when needed, avoid the plaintext local token store unless that risk is acceptable, and never commit or sync generated linkfox/ or ~/.linkfox files. <br>
Risk: The skill includes broad Temu proxy and file-download helpers in addition to narrower pricing scripts. <br>
Mitigation: Prefer the specific us_price_* scripts for normal pricing tasks and review request parameters before using the generic proxy or download helpers. <br>


## Reference(s): <br>
- [API reference](references/api.md) <br>
- [Temu accessToken authorization](references/access-token.md) <br>
- [Authorization flow](references/authorization-flow.md) <br>
- [Partner US price API catalog](references/partner-us-catalog.md) <br>
- [Price API documents index](references/apis/README.md) <br>
- [Temu Partner US documentation](https://partner-us.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API Calls, Files, Configuration] <br>
**Output Format:** [Markdown guidance with shell commands and JSON request/response files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes full API responses under a linkfox/ session data directory and may summarize large responses on stdout.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
