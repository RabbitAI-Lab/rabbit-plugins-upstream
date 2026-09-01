## Description:

DNS Doctor helps diagnose email authentication, DNS, blacklist, and domain or TLS expiry issues through the DNS Doctor public API and returns validated fix records when the service can produce them.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dnsdoctor](https://clawhub.ai/user/dnsdoctor)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, administrators, and domain owners use this skill to diagnose email deliverability and authentication problems, explain DNS Doctor API findings, and provide exact validated records for human-controlled DNS publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Domain names submitted for diagnosis are sent to dnsdoctor.dev.

Mitigation: Tell users before scanning and avoid submitting domains they do not want shared with the DNS Doctor service.

Risk: Optional monitoring features use an API token.

Mitigation: Use a user-managed environment variable for the token and never ask users to paste credentials into the chat.

Risk: Incorrect DNS records or premature enforcement changes can disrupt legitimate email delivery.

Mitigation: Present only API-returned records verbatim, keep publication under human approval, and confirm changes after the user publishes them.

## Reference(s):

- [DNS Doctor methodology](https://dnsdoctor.dev/methodology)
- [DNS Doctor OpenAPI schema](https://dnsdoctor.dev/api/v1/openapi.json)
- [DNS Doctor ClawHub skill page](https://clawhub.ai/dnsdoctor/skills/dns-doctor)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands, summarized API findings, and verbatim DNS record strings from the API.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [DNS publication remains human-controlled; optional monitoring reads require a user-managed API token.]

## Skill Version(s):

1.5.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
