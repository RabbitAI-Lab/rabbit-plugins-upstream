## Description: <br>
Manages Amazon Ads Sponsored Products, Sponsored Brands, and Sponsored Display entities through LinkFox scripts for listing, creating, and updating campaigns, ad groups, ads, keywords, targets, creatives, and budget rules. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and advertising operators use this skill to inspect and manage Amazon Ads account entities across Sponsored Products, Sponsored Brands, and Sponsored Display. It supports operational workflows that need ad entity metadata, campaign setup, bid or budget changes, targeting changes, and budget rule management. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Create and update operations can immediately change Amazon Ads campaigns, bids, budgets, targeting, creatives, and budget rules. <br>
Mitigation: Require explicit user confirmation for spend-affecting actions and review the proposed entity scope and field changes before execution. <br>
Risk: Full API responses may contain ad-account data and are written as plaintext files in the current workspace. <br>
Mitigation: Run the skill only in workspaces approved for advertising account data and review or remove response files according to local data handling policy. <br>
Risk: The skill requires LinkFox authorization with authority over Amazon Ads entities. <br>
Mitigation: Install and use it only with accounts where that authority is intended, and protect the required LinkFox API key environment variables. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-ads-manager) <br>
- [Amazon Ads Manager API Overview](references/api.md) <br>
- [Sponsored Products API Reference](references/api/sp.md) <br>
- [Sponsored Brands API Reference](references/api/sb.md) <br>
- [Sponsored Display API Reference](references/api/sd.md) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [JSON files and stdout JSON or summaries, with Markdown confirmation and result text from the agent] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full API responses are written under the current workspace's linkfox data directory; large responses are summarized on stdout unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
