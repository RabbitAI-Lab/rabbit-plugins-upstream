## Description:

Pull detailed school information from LinkedIn data to help verify education institutions and analyze academic networks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters, researchers, analysts, and agents use this skill to retrieve school names, institution types, locations, websites, and social links from LinkedIn school data for education verification, institutional research, and academic network analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill performs real paid LinkedIn school-detail lookups through UpKuaJing.

Mitigation: Inform the user that lookup calls incur fees and wait for explicit confirmation before running a paid query.

Risk: The skill stores and uses an UpKuaJing API key from the user's environment or ~/.upkuajing/.env.

Mitigation: Install only when the user is comfortable using UpKuaJing as the provider, and keep the API key out of prompts, logs, and shared outputs.

Risk: Diagnostics and error reports may include request context that could contain sensitive user or prompt data.

Mitigation: Ask for explicit confirmation before sending diagnostics and avoid including sensitive prompt or user data in diagnostic context.

Risk: The security verdict is suspicious because the skill contacts the provider for lookup, account, pricing, diagnostics, and version-check requests.

Mitigation: Review the provider relationship, network behavior, account actions, and billing expectations before deployment.

## Reference(s):

- [LinkedIn School Detail API Reference](references/linkedin-school-detail-api.md)
- [Skill Error Report API Reference](references/skill-error-report-api.md)
- [UpKuaJing Homepage](https://www.upkuajing.com)
- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/linkedin-person-school-detail)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [JSON API responses and concise Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a school ID and an UpKuaJing API key; paid lookup calls require explicit user confirmation.]

## Skill Version(s):

1.0.5 (source: server release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
