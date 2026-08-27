## Description:

Verify email address format and status for contact-list cleanup, CRM hygiene, candidate screening, supplier verification, and cold-outreach preparation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External users such as sales teams, recruiters, marketers, and trade operators use this skill to validate email addresses before outreach, list scrubbing, buyer checks, and CRM data cleansing. The skill returns structured validity results and fee information from the UpKuaJing Open Platform API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Email addresses are sent to UpKuaJing's remote API for validation.

Mitigation: Use the skill only for contact data that may be shared with that provider, and avoid sending sensitive or restricted email lists unless approved.

Risk: The skill stores the UpKuaJing API key locally in a plaintext environment file when users create or provide a key.

Mitigation: Protect the local account directory, avoid sharing the file, and rotate the key if it may have been exposed.

Risk: Validation and recharge operations may incur fees.

Mitigation: Require explicit user confirmation before any fee-incurring validation or top-up flow is run.

Risk: Request and response logging could expose email lists or API response data if enabled.

Mitigation: Keep request logging disabled for sensitive lists and review logs before sharing troubleshooting artifacts.

Risk: The skill performs outbound version-check behavior during API requests.

Mitigation: Review this behavior before installing in environments with restricted outbound network policies.

## Reference(s):

- [Email validity API reference](references/email-api.md)
- [Skill error report API reference](references/skill-error-report-api.md)
- [UpKuaJing homepage](https://www.upkuajing.com)
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/email-validity-check)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Validation output includes total count, per-email status records, fee details, and request identifiers when returned by the API.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
