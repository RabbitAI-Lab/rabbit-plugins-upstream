## Description: <br>
Billclaw helps OpenClaw users manage financial data by syncing bank transactions via Plaid or GoCardless, fetching bills from Gmail, and exporting records to Beancount or Ledger formats. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xbinkai](https://clawhub.ai/user/xbinkai) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use Billclaw with OpenClaw to connect Plaid, GoCardless, and Gmail accounts, sync transactions and bills into local storage, and export accounting records. <br>

### Deployment Geography for Use: <br>
Global, with Plaid bank sync in the United States and Canada and GoCardless integration in Europe. <br>

## Known Risks and Mitigations: <br>
Risk: Billclaw handles sensitive bank and Gmail-related data. <br>
Mitigation: Enable only the providers needed, use user-controlled Plaid and Gmail credentials, and protect or delete local ~/.firela/billclaw/ data when appropriate. <br>
Risk: High-trust financial use depends on third-party @firela npm packages. <br>
Mitigation: Review npm and source provenance before use, install only the required package components, and keep packages updated. <br>


## Reference(s): <br>
- [ClawHub Billclaw skill page](https://clawhub.ai/xbinkai/skills/billclaw) <br>
- [BillClaw project page](https://github.com/fire-la/billclaw) <br>
- [BillClaw OpenClaw npm package](https://www.npmjs.com/package/@firela/billclaw-openclaw) <br>
- [BillClaw CLI npm package](https://www.npmjs.com/package/@firela/billclaw-cli) <br>
- [BillClaw Connect npm package](https://www.npmjs.com/package/@firela/billclaw-connect) <br>
- [Plaid Dashboard](https://dashboard.plaid.com/) <br>
- [Google Cloud API credentials](https://console.cloud.google.com/apis/credentials) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance covers credential setup, local storage, OpenClaw commands, and export workflows; the plugin performs financial and Gmail API actions only when explicitly invoked.] <br>

## Skill Version(s): <br>
0.5.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
