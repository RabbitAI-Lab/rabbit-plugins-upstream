## Description:

Helps OpenClaw users sync bank transactions through Plaid or GoCardless, fetch bills from Gmail, and export financial records to Beancount or Ledger formats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xbinkai](https://clawhub.ai/user/xbinkai)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users use this skill to configure financial account connections, request bank and email-bill sync, and export locally stored records for accounting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The third-party plugin accesses sensitive banking and Gmail credentials and financial records.

Mitigation: Review the package before installation and grant only the API permissions needed for the intended accounts.

Risk: Financial exports may be exposed if saved to cloud-synced or version-controlled folders.

Mitigation: Keep exports in a protected local folder outside cloud sync and version control.

Risk: Background sync or a webhook service could continue handling account data beyond a user-initiated session.

Mitigation: Confirm background sync and webhook services remain disabled unless intentionally enabled.

## Reference(s):

- [BillClaw on ClawHub](https://clawhub.ai/xbinkai/skills/billclaw)
- [Required OpenClaw plugin](https://www.npmjs.com/package/@firela/billclaw-openclaw)
- [Optional BillClaw CLI](https://www.npmjs.com/package/@firela/billclaw-cli)
- [Optional BillClaw Connect OAuth server](https://www.npmjs.com/package/@firela/billclaw-connect)
- [Publisher security guidance](artifact/SECURITY.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with command and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the third-party OpenClaw plugin for account sync and exports.]

## Skill Version(s):

0.8.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
