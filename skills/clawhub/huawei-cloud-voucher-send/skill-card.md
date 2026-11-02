## Description:

Issues new Huawei Cloud BSS vouchers to sub-customer accounts in batches, with a preview mode and explicit confirmation for live sends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Huawei Cloud partner and cloud operations teams use this skill to issue quota-backed vouchers to one or more sub-customer accounts and review per-customer results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Faulty duplicate protection can lead to issuing the same voucher more than once, and issuance is a money-moving action.

Mitigation: Treat duplicate protection as unreliable: avoid concurrent sends, reconcile remote results before retrying, preview every batch, and explicitly approve each live issuance.

Risk: Credential or account selection errors can send vouchers from the wrong cloud account or to unintended recipients or amounts.

Mitigation: Verify the active account, recipients, and amounts before sending; use narrowly scoped credentials and keep the local ledger private.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/wlc-dev/skills/huawei-cloud-voucher-send)
- [KooCLI installation and credential setup](artifact/references/cli-installation-guide.md)
- [Least-privilege IAM guidance](artifact/references/iam-policies.md)
- [Operation verification notes](artifact/references/verification-method.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Text]

**Output Format:** [Command-line requests with a human-readable summary or JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May issue irreversible cloud vouchers when explicitly confirmed.]

## Skill Version(s):

1.0.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
