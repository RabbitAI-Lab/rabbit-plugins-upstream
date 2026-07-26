## Description: <br>
Manage and update agent trust scores with Bayesian updates, domain-specific trust, revocation, forgetting curves, challenge-response verification, and a local dashboard. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[felmonon](https://clawhub.ai/user/felmonon) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to maintain local trust graphs for agents, record interactions, verify identity via challenges, and inspect trust state through CLI reports and dashboard views. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Crafted Moltbook usernames, domains, or post IDs may be turned into local shell commands by helper paths. <br>
Mitigation: Do not pass untrusted Moltbook values until subprocess calls use argument lists with input validation. <br>
Risk: Local ATP trust notes may contain sensitive relationship, reputation, or interaction data. <br>
Mitigation: Treat ~/.atp data as sensitive local data and restrict access before use in shared environments. <br>
Risk: The skillsign dependency is unpinned. <br>
Mitigation: Review and pin the skillsign dependency before operational deployment. <br>
Risk: The demo dashboard can expose trust status when served on an accessible network. <br>
Mitigation: Run the dashboard only on networks where exposing trust status is acceptable. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/felmonon/skills/trust-protocol) <br>
- [Project Homepage](https://github.com/FELMONON/trust-protocol) <br>
- [skillsign Identity Dependency](https://github.com/FELMONON/skillsign) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, DOT, shell commands, configuration, guidance] <br>
**Output Format:** [CLI text, JSON graph exports, DOT graph exports, local JSON files, and dashboard views] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Stores trust graph, interaction, challenge, and Moltbook bridge data in local files.] <br>

## Skill Version(s): <br>
2.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
