## Description:

Find alumni connections from LinkedIn-derived data using a person ID and school ID.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External users such as recruiters, sales teams, and B2B lead-generation specialists use this skill to identify alumni-related ties between people and educational institutions. It supports talent sourcing, institutional network research, and contact enrichment workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores the UpKuaJing API key in a plaintext file under the user's home directory.

Mitigation: Use least-privilege local access, avoid sharing the file, rotate exposed keys, and prefer environment-level secret management where available.

Risk: Alumni lookup API calls can incur fees, including additional calls for paginated results.

Mitigation: Confirm paid execution with the user before making chargeable calls and use provider pricing information instead of estimating costs.

Risk: The skill queries LinkedIn-derived personal data.

Mitigation: Review privacy, consent, contractual, and regulatory obligations before use and limit queries to appropriate business purposes.

Risk: Error reports may include request context or response details.

Mitigation: Ask for confirmation before reporting errors and avoid including raw personal data, secrets, or unnecessary sensitive details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/linkedin-person-alumni)
- [UpKuaJing homepage](https://www.upkuajing.com)
- [UpKuaJing Open Platform](https://developer.upkuajing.com/)
- [UpKuaJing price information](https://www.upkuajing.com/web/openapi/price.html)
- [LinkedIn person alumni list API reference](references/linkedin-person-alumni-list-api.md)
- [Skill error report API reference](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Shell commands, Guidance]

**Output Format:** [JSON responses and concise Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python, httpx, and an UpKuaJing API key; alumni list calls are paid and paginated.]

## Skill Version(s):

1.0.5 (source: server evidence and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
