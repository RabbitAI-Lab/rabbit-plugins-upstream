## Description:

Provides DNS configuration guidance for records, TTL planning, email authentication, CAA records, redirects, wildcard records, Cloudflare proxy behavior, and debugging commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site operators, and domain administrators use this skill to plan DNS record changes, configure email authentication and CAA records, handle redirects and wildcard behavior, and debug DNS resolution during migrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation terms such as "configure" or "correctly" may invoke the skill outside explicit DNS tasks.

Mitigation: Invoke it for explicit DNS topics such as records, TTL, SPF, DKIM, DMARC, CAA, nameservers, or migration planning.

Risk: Incorrect DNS changes can disrupt mail delivery, certificates, redirects, or service availability.

Mitigation: Review proposed changes before applying them, test authoritative and public resolver responses, and stage TTL changes ahead of migrations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/dns)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline DNS record examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only guidance; no credentials or persistence are required.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
