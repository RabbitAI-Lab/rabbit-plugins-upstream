## Description: <br>
Helps agents query and manage Shopee store return and refund workflows through the Shopee Open API Returns module, including return lists, details, confirmations, disputes, offers, proof upload, and reverse tracking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, operators, and support agents use this skill to inspect and process authorized Shopee store return and refund cases. It is intended for return/refund lookup, seller decisions, dispute handling, proof management, and reverse logistics tracking after the required Shopee store authorization skill is available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change merchant return or refund state through actions such as confirm, dispute, offer, accept_offer, cancel_dispute, and upload operations. <br>
Mitigation: Require explicit user confirmation before running state-changing actions and review the request body for the intended shop, return_sn, and seller decision. <br>
Risk: Full API responses may contain sensitive business or customer data and can be saved in local linkfox output folders. <br>
Mitigation: Review saved response files after use, delete data that is no longer needed, and avoid sharing saved outputs unless they have been checked for sensitive information. <br>
Risk: The skill depends on an authorized Shopee store token supplied through the companion auth skill. <br>
Mitigation: Install and authorize only the intended Shopee store, keep LinkFox API keys scoped to the operator's role, and stop if the dependency check reports a missing or unexpected auth setup. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-returns) <br>
- [Shopee Returns API reference](references/api.md) <br>
- [Shopee Open Platform Returns index](https://open.shopee.com/documents/v2/v2.returns.get_return_list?module=102&type=1) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, JSON] <br>
**Output Format:** [Markdown guidance, shell command examples, stdout JSON or summaries, and saved JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a LinkFox API key and the linkfox-shopee-store-auth dependency for authorized store tokens; large responses may be summarized on stdout while full responses are saved locally.] <br>

## Skill Version(s): <br>
1.0.3 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
