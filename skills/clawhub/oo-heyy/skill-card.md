## Description: <br>
Heyy lets an agent read, create, and update Heyy data through the OOMOL oo CLI connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to operate a connected Heyy account from an agent, including contact, label, channel, and custom attribute workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can change Heyy contacts, labels, and contact attributes. <br>
Mitigation: Confirm the exact payload and expected effect with the user before running write actions. <br>
Risk: The skill may require installing the oo CLI from a remote installer when the CLI is missing. <br>
Mitigation: Use the remote CLI installer only from a trusted environment and only when setup is required. <br>
Risk: The integration operates a connected Heyy account through OOMOL server-side credentials. <br>
Mitigation: Install only when the user trusts OOMOL and wants agent access to the connected Heyy account. <br>


## Reference(s): <br>
- [Heyy homepage](https://heyy.io) <br>
- [oo CLI repository](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-heyy) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance, text] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
