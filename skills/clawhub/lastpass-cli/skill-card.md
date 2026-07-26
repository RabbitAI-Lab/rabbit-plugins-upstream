## Description: <br>
Securely fetch credentials from LastPass vault via lpass CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gitchrisqueen](https://clawhub.ai/user/gitchrisqueen) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and automation operators use this skill to retrieve specific LastPass entry fields for deployments, API calls, or login flows that need secrets from a local vault. It is intended for fetching secrets into automation flows, not for interactive vault management. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can return sensitive LastPass secrets to the agent session. <br>
Mitigation: Install it only when credential retrieval is intentional, treat every returned value as sensitive, and prevent outputs from being logged, pasted into unrelated tools, or stored in transcripts or artifacts. <br>
Risk: The raw and notes fields can expose more account data than a single username or password field. <br>
Mitigation: Prefer password or username retrieval when possible and use raw or notes only when the broader entry content is necessary. <br>


## Reference(s): <br>
- [LastPass CLI Skill on ClawHub](https://clawhub.ai/gitchrisqueen/skills/lastpass-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands] <br>
**Output Format:** [Plain text values returned by lpass for the requested LastPass entry field.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returned values may include passwords, usernames, notes, or raw entry data and should be handled as sensitive.] <br>

## Skill Version(s): <br>
0.1.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
