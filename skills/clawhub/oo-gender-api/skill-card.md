## Description: <br>
Gender-API.com connects an agent to Gender-API.com through OOMOL's gender_api connector for gender, country-of-origin, ethnicity, and account-usage lookups. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to run Gender-API.com lookups from an OOMOL-connected account, including likely gender from names or email addresses, likely country-of-origin and ethnicity metadata, and remaining-credit statistics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Requests may send names, email addresses, IP addresses, locale, country, and caller ID hints to Gender-API.com through OOMOL. <br>
Mitigation: Use the skill only when this intermediary flow is acceptable, and avoid sending optional context hints unless they are needed for the lookup. <br>
Risk: Setup may require installing the oo CLI or connecting a Gender-API.com account. <br>
Mitigation: Review CLI installation commands before running them and perform authentication or connection steps only after a command fails for that reason. <br>
Risk: Account credits can be consumed when running Gender-API.com lookups. <br>
Mitigation: Use the statistics action to check remaining credits and stop when billing or insufficient-credit errors appear. <br>


## Reference(s): <br>
- [Gender-API.com homepage](https://gender-api.com/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-gender-api) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses from the connector are JSON objects containing data and meta.executionId.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
