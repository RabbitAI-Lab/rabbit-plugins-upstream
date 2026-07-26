## Description: <br>
Explore and analyze Amazon marketplace data through the KeyAPI REST API using live official docs. Use for product search, category browsing, product details, best sellers, deals, seller intelligence, influencer storefronts, reviews, offers, and ASIN/GTIN conversion. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xyzzero](https://clawhub.ai/user/xyzzero) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to turn Amazon marketplace research requests into documentation-verified KeyAPI REST workflows for product, category, deal, seller, review, influencer, and identifier analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: KeyAPI authentication uses KEYAPI_TOKEN, and the default setup can store the token in the user's shell profile. <br>
Mitigation: Prefer the interactive setup command, avoid passing tokens directly with --token when possible, and remove the managed shell-profile block or rotate the token when access is no longer needed. <br>


## Reference(s): <br>
- [Global Rules](references/global-rules.md) <br>
- [Scenario Cards](references/scenarios.md) <br>
- [Routing Policy](references/routing-policy.md) <br>
- [Amazon Rules](references/amazon-rules.md) <br>
- [Amazon Product Module Rules](references/amazon-product-rules.md) <br>
- [Amazon Seller Module Rules](references/amazon-seller-rules.md) <br>
- [Amazon Influencer Module Rules](references/amazon-influencer-rules.md) <br>
- [Setup And Auth](references/setup-and-auth.md) <br>
- [KeyAPI Docs Index](https://docs.keyapi.ai/llms.txt) <br>
- [KeyAPI Authentication](https://docs.keyapi.ai/overview/authentication#bearer-authentication) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, JSON, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce concise analysis, API request guidance, setup instructions, endpoint examples, and user-requested JSON output files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
