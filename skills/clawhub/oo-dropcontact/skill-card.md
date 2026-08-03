## Description: <br>
Dropcontact helps agents read, create, and update Dropcontact data through an OOMOL-connected account instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to inspect Dropcontact connector schemas, submit contact enrichment jobs after confirming the payload, and retrieve enrichment results through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Submitting enrichment sends contact data to Dropcontact through OOMOL and may consume service credits. <br>
Mitigation: Confirm the exact payload before running submit_enrichment, and check billing or connection errors before retrying failed submissions. <br>
Risk: First-time CLI installation or login steps can connect a user's OOMOL account. <br>
Mitigation: Only run install, login, or connection setup steps when the user intends to connect the account or an action fails with the matching setup error. <br>


## Reference(s): <br>
- [Dropcontact homepage](https://www.dropcontact.com/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill listing](https://clawhub.ai/oomol/skills/oo-dropcontact) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill directs agents to fetch the live connector schema before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
