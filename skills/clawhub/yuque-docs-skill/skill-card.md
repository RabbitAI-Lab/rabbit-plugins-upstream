## Description:

Use this skill when a user wants to create, update, delete, or list documents in a Yuque knowledge base, or manage Yuque repository table of contents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cpsean](https://clawhub.ai/user/cpsean)

### License/Terms of Use:

MIT

## Use Case:

Developers and documentation maintainers use this skill to manage Yuque knowledge base documents from an agent workflow, including listing, creating, updating, deleting, pulling, and syncing Markdown content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A local environment or configuration value can redirect the Yuque API token to an arbitrary server.

Mitigation: Review the skill before installation in untrusted repositories or shared shells, verify that .env uses a Yuque HTTPS base URL, and avoid project-controlled .env files that set YUQUE_BASE_URL to a non-Yuque host.

Risk: A broad or misplaced Yuque token could expose documents outside the intended knowledge base.

Mitigation: Use a Yuque token scoped to the intended knowledge base and keep .env ignored by git.

Risk: Document write and delete operations can change or remove Yuque content.

Mitigation: Use dry-run or list/get/toc checks before changes, and require explicit confirmation for deletion.

## Reference(s):

- [Yuque CLI command reference](artifact/references/yuque-cli.md)
- [Source repository](https://github.com/CPsean/yuque-docs-skill)
- [ClawHub skill page](https://clawhub.ai/cpsean/skills/yuque-docs-skill)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-capable CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill may create or update local configuration and sync-state files, and it can direct API-backed document changes in Yuque.]

## Skill Version(s):

0.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
