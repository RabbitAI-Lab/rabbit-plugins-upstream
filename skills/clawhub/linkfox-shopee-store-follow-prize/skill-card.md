## Description: <br>
Helps agents manage authorized Shopee store Follow Prize campaigns through LinkFox by creating, listing, inspecting, updating, ending, and deleting campaign records. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External merchants, operators, and agents use this skill to manage Follow Prize promotions for Shopee stores they are authorized to operate. It supports campaign creation, list and detail retrieval, updates, early ending, and deletion through the documented LinkFox and Shopee API workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, end, or delete live Shopee Follow Prize promotions. <br>
Mitigation: Use it only for stores the user is authorized to manage, and require explicit confirmation before any write or destructive campaign action. <br>
Risk: Full API responses may be retained locally under linkfox session folders. <br>
Mitigation: Treat saved response files as sensitive store data and remove them from shared, backed-up, or long-lived workspaces when they are no longer needed. <br>
Risk: The workflow uses LinkFox API credentials and Shopee campaign data with LinkFox gateway endpoints. <br>
Mitigation: Keep API keys in environment variables, avoid exposing command arguments or saved outputs, and run only in trusted workspaces. <br>
Risk: Credit or billing behavior is unclear for repeated use. <br>
Mitigation: Clarify cost behavior with the publisher before running repeated requests or broad campaign-management workflows. <br>


## Reference(s): <br>
- [Skill API reference](references/api.md) <br>
- [Shopee Follow Prize API documentation](https://open.shopee.com/documents/v2/v2.follow_prize.add_follow_prize?module=113&type=1) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-follow-prize) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/linkfox-ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON files] <br>
**Output Format:** [Markdown guidance, shell commands, and JSON API responses saved to local files with optional stdout output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full responses are saved under linkfox session folders; large responses are summarized unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.3 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
