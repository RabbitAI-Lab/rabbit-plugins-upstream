## Description: <br>
Breezy HR helps an agent search and read Breezy HR companies, positions, candidates, and current-user data through the OOMOL oo connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and recruiting operations users can use this skill to let an agent retrieve Breezy HR company, position, candidate, and current-user records from an already connected OOMOL account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read Breezy HR candidate and user-profile data available to the connected account. <br>
Mitigation: Install and use it only for Breezy HR accounts whose records the agent is intended to access, and handle returned candidate data according to the user's privacy and compliance requirements. <br>
Risk: Setup, authentication, connection, and billing recovery steps involve connecting Breezy HR through OOMOL. <br>
Mitigation: Run those steps only after a matching failure and only when the user is comfortable connecting or reauthorizing Breezy HR through OOMOL. <br>
Risk: Incorrect payloads or stale assumptions about connector actions could query unintended records. <br>
Mitigation: Inspect the live action schema before building payloads and use the documented company, position, candidate, and email identifiers deliberately. <br>


## Reference(s): <br>
- [ClawHub Breezy HR skill](https://clawhub.ai/oomol/skills/oo-breezy-hr) <br>
- [Breezy HR homepage](https://breezy.hr/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector actions return JSON when run with --json; documented actions are read and search operations.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
