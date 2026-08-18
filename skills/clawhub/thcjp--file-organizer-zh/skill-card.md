## Description:

A Chinese-language file organizer skill that helps agents classify files by type, identify duplicate files, and provide file-handling guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and automation teams use this skill to organize selected folders, classify common file types such as images, documents, code, video, audio, and archives, and detect duplicate files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad local file and command capability.

Mitigation: Run it only on explicitly chosen folders, prefer sandboxed execution, and review proposed file moves or deletions before allowing changes.

Risk: File organization or duplicate cleanup can move, overwrite, or delete important user data.

Mitigation: Keep backups, require a dry-run or preview step, and avoid destructive operations until the proposed changes are reviewed.

Risk: The artifact mentions API-key configuration without clearly explaining which service receives data.

Mitigation: Do not provide API keys unless the publisher documents the service, data flow, and purpose for credential use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/file-organizer-zh)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured text with occasional JSON or shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe file operation results, file metadata, execution status, and error guidance.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
