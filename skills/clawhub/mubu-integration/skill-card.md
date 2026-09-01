## Description:

Integrates Mubu with Obsidian and agent workflows by importing Mubu outlines into Obsidian, syncing Markdown to Mubu, and querying or exporting Mubu notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liuboacean](https://clawhub.ai/user/liuboacean)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, knowledge workers, and AI-agent users use this skill to read, export, import, and update Mubu outlines as Markdown for Obsidian workflows, backups, and account-backed note management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access private Mubu outlines using the configured account.

Mitigation: Install only for trusted agent workflows, keep token and environment files private, and avoid exposing account credentials in prompts, scripts, or logs.

Risk: Create, save, move, rename, and purge actions can modify account content, and purge is irreversible.

Mitigation: Confirm target document or folder IDs before write actions; use purge only when the item and type have been verified and explicit confirmation is intended.

Risk: Automatic trigger wording is broad for a skill that can read and modify private notes.

Mitigation: Invoke the skill deliberately for Mubu-specific tasks after credentials, target IDs, and intended read or write scope are clear.

Risk: The integration relies on unofficial Mubu web endpoints that may change or rate-limit requests.

Mitigation: Review failures before retrying at scale, keep request volume reasonable, and verify endpoint behavior before relying on write-heavy workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/liuboacean/skills/mubu-integration)
- [README](artifact/README.md)
- [Changelog](artifact/CHANGELOG.md)
- [Mubu API base endpoint](https://api2.mubu.com/v3/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands; CLI outputs may include Markdown, JSON, OPML, or FreeMind XML.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Mubu account credentials; read, export, and write actions operate on account content.]

## Skill Version(s):

1.3.15 (source: server release metadata, package __version__, CHANGELOG released 2026-08-28)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
