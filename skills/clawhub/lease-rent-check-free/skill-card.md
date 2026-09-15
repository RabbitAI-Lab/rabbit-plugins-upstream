## Description:

租金账单/租赁结算表逐项核对，执行逐行复算、合计勾稽、重复与空缺检测，并让每条结论引用原文行号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, leasing, and operations users can run this skill to check copied rent worksheet or lease settlement table text for arithmetic inconsistencies, missing fields, duplicate tenants, and roll-forward rent arrears. It is intended for worksheet verification, not legal, tax, or lease-term advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact includes a paid-upgrade block that directs the assistant toward an unpinned external installer and purchase flow.

Mitigation: Use the bundled free local checker independently, and verify the package, merchant, product, and payment flow before allowing any installer, newly installed skill instructions, wallet authorization, or payment confirmation.

Risk: Rent worksheets may contain sensitive tenant and payment information.

Mitigation: Run only the local Node checker on materials you are comfortable processing locally, and avoid sending rent worksheet text to unrelated services.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/lease-rent-check-free)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text or JSON from a local Node command]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers; insufficient input returns missing fields instead of a pass/fail conclusion.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
