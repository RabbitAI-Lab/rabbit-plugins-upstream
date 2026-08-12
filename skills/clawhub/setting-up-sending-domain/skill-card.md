## Description:

Use when adding or verifying a Mailtrap sending domain, DNS propagation issues, registrar or DNS provider steps, compliance after verification, or click tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mailtrap](https://clawhub.ai/user/mailtrap)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to add and verify Mailtrap sending domains, configure the required DNS records, troubleshoot propagation, and complete compliance steps before sending email from a controlled domain.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may lead an agent or user to handle a Mailtrap API token while automating setup.

Mitigation: Keep tokens out of chat and logs, store them securely, and use the documented authorization pattern only for accounts the user controls.

Risk: Incorrect DNS changes can prevent Mailtrap domain verification or affect mail authentication for a domain.

Mitigation: Apply records only for domains the user controls, copy all DNS values exactly from the live Mailtrap UI or API response, and verify public propagation before retrying verification.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/mailtrap/skills/setting-up-sending-domain)
- [Mailtrap Sending Domain Setup](https://docs.mailtrap.io/email-api-smtp/setup/sending-domain.md)
- [Cloudflare Sending Domain Guide](https://docs.mailtrap.io/email-api-smtp/setup/sending-domain/cloudflare.md)
- [AWS Route 53 Sending Domain Guide](https://docs.mailtrap.io/email-api-smtp/setup/sending-domain/aws-route-53.md)
- [Google Cloud DNS Sending Domain Guide](https://docs.mailtrap.io/email-api-smtp/setup/sending-domain/google-cloud-dns.md)
- [Squarespace Sending Domain Guide](https://docs.mailtrap.io/email-api-smtp/setup/sending-domain/squarespace.md)
- [GoDaddy Sending Domain Guide](https://docs.mailtrap.io/email-api-smtp/setup/sending-domain/godaddy.md)
- [Namecheap Sending Domain Guide](https://docs.mailtrap.io/email-api-smtp/setup/sending-domain/namecheap.md)
- [DigitalOcean Sending Domain Guide](https://docs.mailtrap.io/email-api-smtp/setup/sending-domain/digitalocean.md)
- [Cloudflare API Documentation](https://developers.cloudflare.com/api/)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, API calls]

**Output Format:** [Markdown with DNS setup steps, troubleshooting commands, API endpoint examples, and reference links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance should be checked against live Mailtrap UI or API DNS record values before applying changes.]

## Skill Version(s):

1.0.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
