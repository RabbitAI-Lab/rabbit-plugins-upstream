## Description:

Publish static sites and web content to a shareable ShipStatic link, with optional built-in password protection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shipstatic-com](https://clawhub.ai/user/shipstatic-com)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to publish a static site, page, report, dashboard, slide deck, document, portfolio, or small web app and share a link to it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Published sites are public unless password protection is requested, so unintended files may be exposed.

Mitigation: Check every file in the selected folder before publishing and use built-in password protection for content that should not be public.

Risk: Claim links can transfer site ownership, and saved credentials can make a deployment persistent in an account.

Mitigation: Keep claim links private and confirm the intended account before publishing with saved credentials.

Risk: Publishing an update leaves the earlier version available.

Mitigation: Do not include sensitive content in a published version; treat prior versions as still accessible after updating.

## Reference(s):

- [ShipStatic on ClawHub](https://clawhub.ai/shipstatic-com/skills/shipstatic)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain text with a published site link and relevant status or access details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a claim link, expiration details, or password-protection status when applicable.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
