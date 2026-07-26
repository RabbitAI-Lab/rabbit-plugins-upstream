## Description: <br>
Missive (missiveapp.com). Use this skill for Missive searching and read-only data retrieval through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to search and retrieve Missive contacts, contact books, conversations, organizations, teams, and users through the OOMOL oo CLI. It is intended for read-focused Missive workflows where the agent should inspect live action schemas before constructing payloads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad Missive searches can expose more workspace content than the user intended. <br>
Mitigation: Ask for specific conversations, mailboxes, teams, date ranges, or other narrow filters before running broad searches or retrievals. <br>
Risk: The skill uses the user's connected Missive access to retrieve contact, conversation, organization, team, and user data. <br>
Mitigation: Install and use it only when the user is comfortable granting the agent read-only Missive access through their OOMOL-connected account. <br>


## Reference(s): <br>
- [Missive homepage](https://missiveapp.com/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-missive) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, JSON, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses may include Missive connector data and execution metadata returned by the oo CLI.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
