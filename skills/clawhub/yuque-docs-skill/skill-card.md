## Description: <br>
Use this skill to create, update, delete, list, sync, pull, and inspect documents in a Yuque knowledge base through Yuque OpenAPI-backed CLI workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cpsean](https://clawhub.ai/user/cpsean) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and knowledge-base maintainers use this skill to push local Markdown content to Yuque, reconcile local and remote document changes, and inspect or update a Yuque repository table of contents. It is intended for single Yuque knowledge-base document operations, not team, permission, repository, or cross-repository administration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a user-provided Yuque API token, creating a manageable credential exposure risk if the token is shared in chat, logs, shell history, process monitoring, or committed files. <br>
Mitigation: Use the least-privileged token available, avoid repeating the token in responses, confirm .env is ignored by git, and rotate the token if exposure is suspected. <br>
Risk: Document synchronization and update commands can change or delete content in the configured Yuque knowledge base. <br>
Mitigation: Validate the target repository before running commands, use dry-run or status checks before mutating sync operations, and require explicit confirmation before remote deletion. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/CPsean/yuque-docs-skill) <br>
- [ClawHub skill page](https://clawhub.ai/cpsean/skills/yuque-docs-skill) <br>
- [Yuque token settings](https://www.yuque.com/settings/tokens) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and CLI result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May relay document IDs, titles, slugs, sync status, warnings, and errors; tokens must not be echoed back to the user.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
