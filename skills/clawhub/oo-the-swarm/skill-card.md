## Description: <br>
The Swarm connector helps agents search and read The Swarm company and profile data through the OOMOL `oo` CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill when they need an agent to fetch The Swarm company or profile records, search for matching IDs, or report authenticated team API credit usage through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill operates through an authenticated OOMOL connection and can return The Swarm company, profile, search, and credit-usage data. <br>
Mitigation: Use it only for requested The Swarm tasks, inspect the live connector schema before building payloads, and avoid sending secrets, API keys, customer data, or unrelated personal information. <br>
Risk: Credentialed connector access could be mistaken for approval to perform sensitive exports or actions in other systems. <br>
Mitigation: Treat OOMOL credentials and grant tokens as connector access only; require separate human or platform approval for payments, databases, exports, or other sensitive operations. <br>


## Reference(s): <br>
- [The Swarm homepage](https://www.theswarm.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-the-swarm) <br>
- [Publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, JSON, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill instructs the agent to inspect live connector schemas before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
