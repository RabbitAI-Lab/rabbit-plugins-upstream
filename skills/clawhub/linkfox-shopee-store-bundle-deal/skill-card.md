## Description: <br>
This skill helps agents manage Shopee Bundle Deal promotions for authorized stores, including creating, listing, updating, ending, and deleting bundle campaigns and campaign items. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Shopee store operators and commerce automation agents use this skill to manage authorized store Bundle Deal campaigns and participating items through the documented Shopee Bundle Deal API flow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, end, and delete live Shopee Bundle Deal promotions. <br>
Mitigation: Confirm each write action with the user before execution and use only Shopee accounts where promotion-management authority is appropriate. <br>
Risk: Full business API responses may be persisted in the working directory. <br>
Mitigation: Run the skill in a private workspace, avoid shared repositories for sensitive shop data, and review or remove saved response files after use. <br>
Risk: Authentication, dependency installation, and point-cost behavior may require user approval. <br>
Mitigation: Have the user approve API key setup, dependency or onboarding skill installation, and any repeated or exploratory calls that may consume points. <br>


## Reference(s): <br>
- [Bundle Deal API Reference](references/api.md) <br>
- [Shopee Open Platform Bundle Deal API](https://open.shopee.com/documents/v2/v2.bundle_deal.add_bundle_deal?module=110&type=1) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-bundle-deal) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, JSON] <br>
**Output Format:** [Markdown-style guidance with shell command examples and JSON API responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full API responses are saved under the current working directory; larger responses may be summarized unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.3 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
