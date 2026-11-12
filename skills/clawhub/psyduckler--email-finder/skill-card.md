## Description:

Find email addresses for a domain by combining website scraping, search dorking, pattern guessing, DNS analysis, and SMTP verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyduckler](https://clawhub.ai/user/psyduckler)

### License/Terms of Use:


## Use Case:

External users and agents use this skill for authorized, targeted contact-email lookup on a company domain, optionally using a person's name to generate common address patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill actively discovers and verifies personal email addresses by contacting websites, DNS, Google, Hunter.io, and recipient mail servers.

Mitigation: Use only for authorized, targeted lookups; prefer --no-verify unless SMTP probing is necessary; avoid unsolicited bulk list building; and keep rate limits conservative.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/psyduckler/skills/email-finder)
- [ClawHub Publisher Profile](https://clawhub.ai/user/psyduckler)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [JSON to stdout with status logs on stderr]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes the normalized domain, detected email provider, MX/SPF/DMARC records, email count, and per-email source and deliverability status.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
