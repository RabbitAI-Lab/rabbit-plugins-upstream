## Description: <br>
Buttondown operates a user's Buttondown account through the OOMOL-connected oo CLI for reading, creating, updating, and deleting account, newsletter, subscriber, and tag data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to manage Buttondown account, newsletter, subscriber, and tag workflows through an OOMOL-connected account. It supports direct reads and requires confirmation before write or destructive actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, or delete Buttondown subscribers and tags. <br>
Mitigation: Confirm the exact payload, target, and expected effect with the user before write actions, and require explicit approval before destructive actions. <br>
Risk: The skill connects to a user's Buttondown account through OOMOL-managed credentials. <br>
Mitigation: Install only when the user trusts OOMOL and intends to grant Buttondown access through the oo CLI. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-buttondown) <br>
- [Buttondown Homepage](https://buttondown.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before action execution and returns connector data with an execution id when commands run.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence release.version and metadata.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
