## Description: <br>
Detrack (detrack.com) lets an agent read, create, update, and delete Detrack data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to manage Detrack delivery and collection workflows through the oo CLI, including job lookup, depot listing, job creation, updates, and deletion with confirmation for state-changing actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Create, update, and delete actions can change or remove operational Detrack delivery records. <br>
Mitigation: Review the exact payload, target job, and expected effect with the user before approving write or destructive actions. <br>
Risk: Detrack actions require a signed-in OOMOL account with an active Detrack connection. <br>
Mitigation: Use first-time setup steps only after authentication or connection errors, then retry with the connected account. <br>


## Reference(s): <br>
- [ClawHub Detrack skill page](https://clawhub.ai/oomol/skills/oo-detrack) <br>
- [Detrack homepage](https://www.detrack.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before building payloads; OOMOL injects credentials server-side.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence release and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
