## Description:

mubu-integration lets agents and developers manage Mubu outlines from the command line, convert Mubu documents to and from Markdown, and connect Mubu notes with Obsidian workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liuboacean](https://clawhub.ai/user/liuboacean)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent operators use this skill to back up, browse, search, import, export, and optionally write Mubu outlines as Markdown for AI agent memory or Obsidian workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use Mubu account credentials to read and change cloud notes.

Mitigation: Install only for explicit Mubu tasks, keep credentials out of shared terminals and logs, and back up important notes before save, move, rename, or delete workflows.

Risk: Broad activation or inconsistent write-confirmation behavior could run the skill in contexts where account access was not intended.

Mitigation: Avoid casual auto-triggering on the words mubu or Mubu and require clear user intent before any authenticated operation.

Risk: Overriding the MUBU_BASE_URL endpoint can change where account requests are sent.

Mitigation: Leave MUBU_BASE_URL unset unless the endpoint has been reviewed and validated.

Risk: The purge operation is permanent deletion of Mubu content.

Mitigation: Treat purge as irreversible and back up important notes before using deletion workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/liuboacean/skills/mubu-integration)
- [Artifact README](artifact/README.md)
- [Skill instructions](artifact/SKILL.md)
- [Mubu API base URL](https://api2.mubu.com/v3/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON, OPML or FreeMind XML, and shell-command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Authenticated Mubu tasks may read or modify cloud notes when the user supplies credentials and explicitly confirms write operations.]

## Skill Version(s):

1.3.16 (source: server release evidence and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
