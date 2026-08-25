## Description:

mubu-integration lets agents read, write, search, import, and export Mubu outlines as Markdown, JSON, OPML, or FreeMind content through the user's configured Mubu account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liuboacean](https://clawhub.ai/user/liuboacean)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI-agent users use this skill to connect Mubu outlines with Markdown workflows such as Obsidian notes, archival exports, and scripted account operations. It is most useful when a user explicitly asks an agent to query, export, create, update, move, rename, or purge Mubu content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change live Mubu account data, including create, save, move, rename, and purge operations.

Mitigation: Use it only for explicit Mubu action requests and confirm the target document or folder before any write operation.

Risk: Purge operations can permanently delete Mubu content.

Mitigation: Require clear user confirmation before purge and verify the item id, item type, and intended target before execution.

Risk: Local token or credential files can expose Mubu account access on shared machines.

Mitigation: Protect or remove ~/.mubu_token and ~/.workbuddy/.env.mubu on shared machines.

Risk: Trigger and confirmation boundaries are looser than advertised.

Mitigation: Invoke the skill only after an explicit Mubu-related request and present the planned action before create, save, move, rename, or purge commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/liuboacean/skills/mubu-integration)
- [ClawHub publisher profile](https://clawhub.ai/user/liuboacean)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, code, shell commands, configuration, guidance]

**Output Format:** [Human-readable guidance, shell commands, Markdown, JSON, and OPML or FreeMind XML.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may lead an agent to execute authenticated Mubu account operations when credentials are configured.]

## Skill Version(s):

1.3.14 (source: server release metadata and artifact changelog dated 2026-08-25)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
