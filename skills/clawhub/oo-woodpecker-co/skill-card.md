## Description: <br>
Woodpecker.co connector skill for reading campaigns, mailboxes, prospects, active users, campaign details, campaign statistics, and mailbox configuration through OOMOL's oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to let an agent retrieve Woodpecker.co account data through an authenticated OOMOL connector for sales outreach support and reporting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad routing language could cause an agent to use the skill for Woodpecker.co requests beyond the listed read actions. <br>
Mitigation: Keep use to explicit Woodpecker.co read requests and the listed connector actions; avoid broader oo subcommands unless separately intended. <br>
Risk: The skill depends on an installed oo CLI, an authenticated OOMOL account, a connected Woodpecker.co provider, and available OOMOL credit. <br>
Mitigation: Run setup, login, connection, or billing steps only after matching command failures and avoid repeating one-time setup on routine reads. <br>
Risk: If write or destructive connector actions are introduced later, they could change or remove Woodpecker.co data. <br>
Mitigation: Confirm the exact action, target, payload, and effect with the user before running any write or destructive action. <br>


## Reference(s): <br>
- [Woodpecker.co homepage](https://woodpecker.co/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [OOMOL Woodpecker.co connection](https://console.oomol.com/app-connections?provider=woodpecker_co) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, JSON, guidance] <br>
**Output Format:** [Markdown guidance with oo CLI commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read actions return connector JSON with data and execution metadata.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
