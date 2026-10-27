## Description:

Issues new Huawei Cloud BSS vouchers to sub-customer or partner accounts, individually or in batches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Huawei Cloud billing administrators and partners use this skill to issue new BSS vouchers to sub-customer or partner accounts, including batches of recipients.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Known duplicate-protection gaps can lead to vouchers being issued more than once, especially during retries.

Mitigation: Correct duplicate-protection defects before live use. Preview each batch, avoid concurrent runs, direct CLI issuance, and --force, and reconcile uncertain outcomes with Huawei before retrying.

Risk: Credential-selection defects can result in use of an unintended Huawei Cloud account.

Mitigation: Correct credential-selection defects before live use, verify the active account, use narrowly scoped credentials, and confirm the quota, recipients, and amount. Keep the issuance ledger in a private directory.

## Reference(s):

- [IAM policies](artifact/references/iam-policies.md)
- [KooCLI installation and credential setup](artifact/references/cli-installation-guide.md)
- [Verification method](artifact/references/verification-method.md)
- [Acceptance criteria](artifact/references/acceptance-criteria.md)
- [Data flow diagram](artifact/references/dataflow-diagram.md)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, JSON, Text]

**Output Format:** [Command-line invocation with text or JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live issuance is a financial change and requires explicit confirmation.]

## Skill Version(s):

1.0.2 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
