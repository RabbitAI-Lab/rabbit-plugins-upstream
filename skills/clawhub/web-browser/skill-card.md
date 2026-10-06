## Description:

Helps agents test and inspect browser interfaces, diagnose styling inside closed shadow DOM, and assist with issuing or managing service credentials after user sign-in.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill to verify web interfaces, investigate browser styling and shadow DOM behavior, and guide user-approved sign-in before issuing, storing, or revoking service credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser captures may expose autofilled passwords or other secrets in page content or accessibility snapshots.

Mitigation: Require explicit approval before capturing a sign-in or credential-input screen; minimize captured content and redact sensitive values.

Risk: Credential issuance, scope changes, or revocation can grant excessive access or disrupt an existing integration.

Mitigation: Confirm the service, account, requested scope, destination store, and any revoke or delete action with the user before acting.

Risk: Temporary files, environment files, shell arguments, or chat output may expose reusable credentials.

Mitigation: Prefer Vault, OS keyrings, or provider secret stores; avoid command-line passwords and plaintext temporary or .env files.

Risk: Browser tracing on untrusted or invalid-TLS login pages and unpinned browser tooling can endanger signed-in sessions.

Mitigation: Do not use the CDP trace login path on untrusted or invalid-TLS sites, and pin npm and Playwright dependencies before using logged-in sessions.

## Reference(s):

- [ClawHub web-browser release](https://clawhub.ai/drumrobot/skills/web-browser)
- [UI testing guide](artifact/ui-test.md)
- [Credential issuance guide](artifact/credential-issue.md)
- [CDP trace guide](artifact/cdp-trace.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands]

**Output Format:** [Markdown explanations and reports with code or shell commands as needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include browser test results and credential-handling instructions; sensitive values should not appear in reports.]

## Skill Version(s):

0.2.10 (source: server-resolved release, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
