## Description: <br>
Interact with Confluence Cloud from the command line when reading, creating, updating, or searching Confluence pages, managing attachments, labels, comments, or exporting content. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hochej](https://clawhub.ai/user/hochej) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, documentation maintainers, and operations teams use this skill to work with Confluence Cloud from an agent through confcli, including finding pages, reading or exporting content, and performing explicit write actions such as page updates, comments, labels, attachments, or copy-tree operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installation instructions fetch and execute a mutable remote shell script. <br>
Mitigation: Prefer a pinned release or package-manager installation with checksum or signature verification, and review the installer before execution. <br>
Risk: Authenticated confcli commands can create, update, delete, purge, or copy Confluence content. <br>
Mitigation: Use a Confluence token limited to the needed spaces and permissions, require explicit confirmation before write or destructive operations, and use dry-run where supported. <br>
Risk: Confluence API tokens are sensitive credentials. <br>
Mitigation: Configure tokens through environment variables or interactive login, and never paste tokens into an agent conversation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/hochej/skills/confluence-cli) <br>
- [Atlassian API tokens](https://id.atlassian.com/manage-profile/security/api-tokens) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands; confcli output may be JSON, table, or Markdown.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires configured Confluence domain, email, and API token; write or destructive actions require explicit user intent and should use dry-run where supported.] <br>

## Skill Version(s): <br>
0.2.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
