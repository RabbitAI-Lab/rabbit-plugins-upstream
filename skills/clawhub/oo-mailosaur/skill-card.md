## Description: <br>
Mailosaur (mailosaur.com). Use this skill for Mailosaur requests that read, create, update, or delete data through the OOMOL-connected oo CLI connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to manage Mailosaur inbox servers, messages, usage limits, and recent usage transactions from an agent workflow connected through OOMOL. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can delete Mailosaur messages, attachments, inbox servers, and stored server messages. <br>
Mitigation: Require explicit user approval for destructive actions and confirm the exact target before running the command. <br>
Risk: Write actions can create or rename Mailosaur inbox servers. <br>
Mitigation: Inspect the live connector schema and confirm the payload and intended effect with the user before execution. <br>
Risk: The skill lets an agent operate a connected Mailosaur account through OOMOL. <br>
Mitigation: Install and use it only when that account-level access is intended. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mailosaur) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [Mailosaur homepage](https://mailosaur.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, JSON] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
