## Description: <br>
Neutrino API (neutrinoapi.com) supports agent requests for searching and reading Neutrino data through the documented connector workflow instead of direct API calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to run Neutrino lookup and validation actions through an OOMOL-connected account, including IP blocklist checks, IP geolocation, domain lookups, email validation, and phone validation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Lookup inputs may include IP addresses, domains, email addresses, or phone numbers that are sensitive or personal. <br>
Mitigation: Use the skill only when sending that data to Neutrino through an OOMOL-connected account is appropriate for the user and task. <br>
Risk: First-time CLI installation or account connection can affect the local environment or authenticated account state. <br>
Mitigation: Review installation, sign-in, and connection steps before running them, and use them only when an action fails because setup is missing or expired. <br>


## Reference(s): <br>
- [Neutrino API homepage](https://www.neutrinoapi.com/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-neutrino) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces guidance for invoking oo CLI connector schema and run commands; command responses are JSON from Neutrino via OOMOL.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
