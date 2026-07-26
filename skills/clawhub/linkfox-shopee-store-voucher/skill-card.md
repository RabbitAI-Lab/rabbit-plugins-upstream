## Description: <br>
Manages Shopee store vouchers through the LinkFox developer proxy, covering create, list, detail, update, end, and delete operations for authorized shops. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External marketplace operators and developers use this skill to manage voucher campaigns for authorized Shopee shops, including creating, reviewing, updating, ending, or deleting store vouchers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can update, end, or delete live Shopee shop voucher promotions. <br>
Mitigation: Before using update, end, or delete actions, require the agent to show the exact voucher ID and planned change, then obtain explicit confirmation. <br>
Risk: Full LinkFox and Shopee API responses are saved to local linkfox session files and may contain business-sensitive data. <br>
Mitigation: Treat saved response files as sensitive business data, restrict access to the workspace, and delete the files when they are no longer needed. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-voucher) <br>
- [Voucher API reference](references/api.md) <br>
- [Shopee Open Platform voucher documentation](https://open.shopee.com/documents/v2/v2.voucher.add_voucher?module=112&type=1) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Files, Guidance] <br>
**Output Format:** [JSON responses printed to stdout, with full responses saved as JSON files and large responses summarized unless inline output is requested.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires LinkFox API credentials and the linkfox-shopee-store-auth dependency; response files are written under a linkfox session directory.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
