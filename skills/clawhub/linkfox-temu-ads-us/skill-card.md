## Description: <br>
Provides LinkFox gateway scripts and guidance for Temu US Ads API workflows, including ad creation, modification, details, reports, operation logs, goods eligibility, and ROAS prediction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Temu sellers, ecommerce operators, and developers use this skill to call LinkFox-mediated Temu US Ads APIs for campaign setup, budget or ROAS changes, reporting, operation logs, and related ad diagnostics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can proxy Temu seller and advertising requests through LinkFox, including broad custom Temu API types. <br>
Mitigation: Install and run it only in workspaces where LinkFox is trusted with Temu seller and ads access, and review each command before execution. <br>
Risk: Advertising actions can create ads, delete or pause ads, and change budget or ROAS settings. <br>
Mitigation: Require user confirmation for write actions and budget or ROAS changes, and prefer read-only detail, goods eligibility, report, or log queries when diagnosing. <br>
Risk: Temu access tokens may be passed in command JSON or saved in a local plaintext token store. <br>
Mitigation: Prefer short-lived direct token use when possible, protect any token store path, avoid printing or sharing raw tokens, and rotate tokens if exposure is suspected. <br>
Risk: Full API responses are persisted locally and may contain sensitive seller, campaign, report, or business data. <br>
Mitigation: Use a controlled workspace, clean up saved linkfox response files after use, and avoid adding those files to source control or shared logs. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-ads-us) <br>
- [API Reference](references/api.md) <br>
- [Temu Access Token Authorization](references/access-token.md) <br>
- [Authorization Flow](references/authorization-flow.md) <br>
- [Partner US Ads Catalog](references/partner-us-catalog.md) <br>
- [Ads API Documentation Index](references/apis/README.md) <br>
- [Temu Partner US Ads Documentation](https://partner-us.temu.com/documentation?menu_code=1e72b5cceef545ec8f9652b9e56dd054) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with Python command examples and JSON API responses saved to local files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Small responses may print full JSON to stdout; larger responses are summarized after the full response is written under a linkfox session data directory.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
