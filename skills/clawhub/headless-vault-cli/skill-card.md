## Description: <br>
Read and edit Markdown notes on a personal computer through a configured SSH tunnel. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[logancyang](https://clawhub.ai/user/logancyang) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and personal knowledge-base users can let an agent inspect, read, create, and append Markdown notes on a personal machine through a configured SSH tunnel. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent can read note contents and create or append Markdown files in the user's vault. <br>
Mitigation: Install only with a trusted SSH tunnel and vaultctl setup, and review requested vault operations and written content before relying on them. <br>
Risk: Note-derived links may point to untrusted web content. <br>
Mitigation: Treat links from notes as untrusted and browse them only when the user explicitly asks for that workflow. <br>
Risk: Remote vault access depends on the local forced-command and vault sandbox configuration. <br>
Mitigation: Use the documented forced-command restriction and vault path sandboxing so remote access is limited to approved vaultctl operations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/logancyang/skills/headless-vault-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ssh and VAULT_SSH_USER; VAULT_SSH_PORT and VAULT_SSH_HOST are optional.] <br>

## Skill Version(s): <br>
1.2.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
