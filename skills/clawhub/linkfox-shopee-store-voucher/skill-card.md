## Description:

Helps agents manage Shopee store voucher campaigns through LinkFox's /shopee/developerProxy wrapper for add, list, get, update, end, and delete voucher operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and developers use this skill to create, inspect, update, end, or delete voucher campaigns for authorized Shopee shops through LinkFox gateway scripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change live Shopee voucher campaigns, including ending or deleting vouchers.

Mitigation: Manually confirm shop identity, voucher IDs, and destructive actions before running mutation scripts.

Risk: The skill handles LinkFox API keys, login, SMS-code, and payment flows.

Mitigation: Use a dedicated API key, verify LinkFox endpoint environment variables, and enter SMS codes only when intentionally creating or recovering credentials.

Risk: The skill saves full API responses locally.

Mitigation: Review the LinkFox session output directory and avoid sharing saved response files that may contain shop or campaign details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-voucher)
- [Voucher API reference](artifact/references/api.md)
- [Authentication and billing onboarding](artifact/references/onboarding.md)
- [Shopee add_voucher documentation](https://open.shopee.com/documents/v2/v2.voucher.add_voucher?module=112&type=1)
- [Shopee get_voucher_list documentation](https://open.shopee.com/documents/v2/v2.voucher.get_voucher_list?module=112&type=1)
- [Shopee update_voucher documentation](https://open.shopee.com/documents/v2/v2.voucher.update_voucher?module=112&type=1)
- [Shopee end_voucher documentation](https://open.shopee.com/documents/v2/v2.voucher.end_voucher?module=112&type=1)
- [Shopee delete_voucher documentation](https://open.shopee.com/documents/v2/v2.voucher.delete_voucher?module=112&type=1)

## Skill Output:

**Output Type(s):** [JSON, Files, Shell commands, Guidance]

**Output Format:** [JSON responses saved to local files, with stdout JSON or summaries and Markdown-style guidance for setup and troubleshooting]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are persisted under a LinkFox session directory; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.5 (source: server release evidence, created 2026-08-14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
