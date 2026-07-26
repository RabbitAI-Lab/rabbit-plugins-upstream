## Description: <br>
Leadfeeder helps agents search and read Leadfeeder company, account, and user data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, sales operations teams, and agents use this skill to inspect Leadfeeder schemas, enrich IP addresses, retrieve company and account data, match companies, and search company intelligence through the oo CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access Leadfeeder company intelligence, account details, user details, and possible credit details through the connected OOMOL account. <br>
Mitigation: Install only when the publisher is trusted and the user intends the agent to query Leadfeeder data from that connected account. <br>
Risk: Future connector actions could be marked write or destructive. <br>
Mitigation: Review prompts carefully and require explicit user confirmation before any action documented as write or destructive. <br>
Risk: Connector payloads may be incorrect if an agent relies on stale assumptions. <br>
Mitigation: Inspect the live Leadfeeder action schema with the oo CLI before building each payload. <br>


## Reference(s): <br>
- [Leadfeeder skill page](https://clawhub.ai/oomol/skills/oo-leadfeeder) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [Leadfeeder homepage](https://www.leadfeeder.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill directs agents to inspect live connector schemas before constructing Leadfeeder action payloads.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
