## Description:

DNS Doctor diagnoses SPF, DMARC, DKIM, MX, DNS, blacklist, and domain/SSL expiry issues through the DNS Doctor public API and returns validated copy-paste records when the API provides them.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dnsdoctor](https://clawhub.ai/user/dnsdoctor)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and domain administrators use this skill to diagnose email authentication and DNS posture issues, explain failing checks, and hand off validated records or next steps for human-applied DNS changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries share a domain's email-authentication posture with dnsdoctor.dev.

Mitigation: Use the skill only for domains whose owner is comfortable sending diagnostic data to DNS Doctor's API.

Risk: Incorrectly edited DNS records can weaken enforcement or disrupt legitimate mail.

Mitigation: Present API-returned record strings verbatim, have the domain owner review them, and leave publication at the DNS host to the human.

Risk: API tokens could expose read-only monitoring data if pasted into chat or stored casually.

Mitigation: Do not ask users to paste tokens; use an environment variable only for the token owner's verified monitoring reads.

Risk: DMARC enforcement can reject legitimate mail if tightened before alignment evidence is ready.

Mitigation: Check readiness before proposing enforcement, relay blockers when next_record is null, and avoid inventing a stronger record.

Risk: Monitoring automation can miss alerts if pagination is advanced incorrectly.

Mitigation: Page through alerts with the before cursor until next_before is null before advancing the since watermark, and de-duplicate repeated rows by id.

## Reference(s):

- [DNS Doctor methodology](https://dnsdoctor.dev/methodology)
- [DNS Doctor OpenAPI schema](https://dnsdoctor.dev/api/v1/openapi.json)
- [DNS Doctor API base](https://dnsdoctor.dev/api/v1)
- [DNS Doctor ClawHub skill listing](https://clawhub.ai/dnsdoctor/skills/dns-doctor)
- [DNS Doctor publisher profile](https://clawhub.ai/user/dnsdoctor)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with diagnostic summaries, curl command examples, and verbatim API-returned DNS records when present]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [DNS changes remain user-applied; API tokens are optional for read-only monitoring endpoints and should be supplied through environment variables.]

## Skill Version(s):

1.4.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
