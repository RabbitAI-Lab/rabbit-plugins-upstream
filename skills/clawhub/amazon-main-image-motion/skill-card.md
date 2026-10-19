## Description:

Turns one approved white-background product image into a short clip for a listing's main video slot.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and their agents use an approved listing main image to plan and generate one short product-motion clip, with seller approval before billable generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A shared, persistent Device Token grants broad Beatra media and wallet-related permissions.

Mitigation: Review the requested access before authorizing, keep the token private, and review Beatra device revocation options when disconnecting.

Risk: Automatic package updates are silent by default.

Mitigation: If changes require prior review, disable automatic updates with `python3 scripts/mcp_client.py update --auto off` and check updates manually.

Risk: Installation and coarse runtime metadata are reported to Beatra.

Mitigation: Review the documented registration data and privacy terms before installing.

Risk: Generating or repeating a video can consume credits.

Mitigation: Confirm the live price and one-call production plan first; recover uncertain submissions using the same request identity instead of starting another charge.

## Reference(s):

- [Skill homepage](https://beatra.ai/skills/amazon-main-image-motion)
- [Main image motion workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Installation registration](artifact/references/installation-registration.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)

## Skill Output:

**Output Type(s):** [Guidance, Video]

**Output Format:** [Markdown shot plan and generated video clip]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One image per clip; report actual dimensions, duration, usage, and charged credits.]

## Skill Version(s):

0.1.9 (source: server-resolved ClawHub release and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
