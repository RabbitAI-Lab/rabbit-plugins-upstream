## Description: <br>
Operate Raisely campaign, profile, and webhook data through an OOMOL-connected account using schema-driven oo CLI connector actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and fundraising teams use this skill to read Raisely campaign and profile data and to manage Raisely webhooks through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, or delete Raisely webhooks, which may change account behavior or remove webhook configuration. <br>
Mitigation: Confirm the exact payload, target, and expected effect with the user before running write or destructive actions. <br>
Risk: The skill operates a Raisely account through OOMOL and the oo CLI connection. <br>
Mitigation: Install and use it only when the user intends the agent to operate that account and trusts the oo CLI and OOMOL connection brokering credentials. <br>


## Reference(s): <br>
- [ClawHub Raisely skill page](https://clawhub.ai/oomol/skills/oo-raisely) <br>
- [Raisely homepage](https://raisely.com/) <br>
- [oo CLI repository](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands use the oo CLI to inspect live connector schemas and run Raisely actions with JSON payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: skill frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
