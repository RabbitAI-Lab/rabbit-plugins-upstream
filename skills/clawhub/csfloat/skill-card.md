## Description: <br>
Queries csfloat.com for data on skins. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bluesyparty-src](https://clawhub.ai/user/bluesyparty-src) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and CSFloat users use this skill to query listings, view specific listings, and prepare CSFloat marketplace API commands from an agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill presents itself as a CSFloat data helper but includes commands for creating live marketplace listings. <br>
Mitigation: Review any create-listing command before execution, confirm the asset ID, price, listing type, and visibility, and remove that example if listing creation is not intended. <br>
Risk: The skill requires a CSFloat API key in the agent environment. <br>
Mitigation: Install only where sharing the CSFloat API key with the agent is acceptable, and avoid exposing the key in logs, prompts, or shared shell history. <br>


## Reference(s): <br>
- [CSFloat Documentation](https://docs.csfloat.com/#introduction) <br>
- [CSFloat Profile API Key Page](https://csfloat.com/profile) <br>
- [CSFloat Listings API](https://csfloat.com/api/v1/listings) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires jq and a CSFLOAT_API_KEY environment variable.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
