## Description:

MyOTP.App helps agents add SMS, WhatsApp, or Telegram OTP, 2FA, MFA, and phone verification to applications through a REST API using an X-API-Key header.

This skill is ready for commercial/non-commercial use.

## Publisher:

[myotp](https://clawhub.ai/user/myotp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to implement phone verification, two-factor authentication, password reset, signup verification, and transaction step-up flows with MyOTP.App across SMS, WhatsApp, and Telegram channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents can create MyOTP.App accounts and initiate credit top-ups without a clear human approval boundary.

Mitigation: Require explicit human approval before top-ups, set hard spend limits, and pin or vet payment tooling before enabling autonomous payment flows.

Risk: Broad OTP or 2FA requests could automatically route through this paid third-party provider.

Mitigation: Require provider confirmation for broad authentication requests and install the skill only when MyOTP.App is an intended provider.

Risk: API keys and phone-number or OTP data may expose credentials or PII if handled loosely.

Mitigation: Restrict MYOTP_API_KEY access, use IP allowlists, keep OTP verification server-side, and avoid logging OTPs or full phone numbers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/myotp/skills/myotp)
- [Publisher profile](https://clawhub.ai/user/myotp)
- [MyOTP.App homepage](https://myotp.app)
- [API reference](https://myotp.app/api-reference/)
- [Sample code](https://myotp.app/sample-code-new/)
- [Pricing](https://myotp.app/pricing/)
- [Security and trust](https://myotp.app/security/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with REST request examples, code snippets, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires MYOTP_API_KEY and curl; may guide agents through MyOTP.App account setup, API calls, and credit top-ups.]

## Skill Version(s):

1.0.4 (source: server release and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
