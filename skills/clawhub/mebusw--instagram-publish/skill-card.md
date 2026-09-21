## Description:

Publishes single-image posts or multi-image carousels to Instagram via the Graph API from a Creator or Business account using public image URLs and an access token.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mebusw](https://clawhub.ai/user/mebusw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and operators use this skill to publish single-image posts or multi-image carousels to Instagram from public image URLs after completing Meta and Instagram account setup. It also helps configure credentials and troubleshoot common Instagram Graph API publishing errors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish to the connected Instagram account when a valid access token is available.

Mitigation: Install only for accounts where automated posting is intended, keep the access token private, and use --dry-run before publishing.

Risk: Public image URLs may fail if Meta's servers cannot reach them.

Mitigation: Use publicly reachable HTTPS image URLs and verify access from a logged-out browser before posting.

Risk: A leaked .env access token can allow unauthorized posting.

Mitigation: Keep .env out of version control, rotate leaked tokens immediately, and prefer low-risk or test accounts during setup.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mebusw/skills/instagram-publish)
- [Server-resolved GitHub source](https://github.com/mebusw/instagram-publish)
- [Meta for Developers](https://developers.facebook.com/)
- [Meta app dashboard](https://developers.facebook.com/apps/)
- [Instagram professional account settings](https://www.instagram.com/accounts/professional_account_settings/)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown guidance with shell commands and Python script execution output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses public image URLs and .env credentials; supports dry-run validation before final publishing.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
