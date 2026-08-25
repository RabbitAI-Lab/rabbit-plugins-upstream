## Description:

Find corporate alumni and former colleagues with company ID and personnel ID lookups, then trace career history and expand professional networks for recruitment and B2B lead development.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters, sales teams, and B2B lead generation specialists use this skill to find alumni records for a target person and organization context, page through results, and expand professional relationship datasets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores and reads an UpKuaJing API key from a local plaintext file.

Mitigation: Protect ~/.upkuajing/.env as a secret, restrict local file access, and rotate the key if it may have been exposed.

Risk: The alumni lookup API and additional pages are paid calls.

Mitigation: Confirm pricing through the documented price page or price_info helper and require explicit user approval before each paid query.

Risk: Error reports can include request context involving personal or business data.

Mitigation: Review and minimize report contents before submission, and avoid sending raw sensitive data when reporting failures.

Risk: The scripts perform a once-daily vendor version check during API use.

Mitigation: Install only in environments where this vendor network contact is acceptable, and review outbound traffic policies before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/global-company-person-alumni)
- [UpKuaJing homepage](https://www.upkuajing.com)
- [UpKuaJing Open Platform](https://developer.upkuajing.com/)
- [Detailed price description](https://www.upkuajing.com/web/openapi/price.html)
- [Alumni List API](references/person-alumni-list-api.md)
- [Skill Error Report API](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python, an UPKUAJING_API_KEY, explicit confirmation before paid API calls, and pagination through cursor values when more results are available.]

## Skill Version(s):

1.0.5 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
