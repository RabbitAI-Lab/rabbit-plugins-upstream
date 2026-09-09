## Description:

Exports ChatGPT conversation history through a browser relay or bookmarklet into local JSON and Markdown files, with index-only defaults, explicit consent, private file modes, destination checks, and purge support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT

## Use Case:

Developers and ChatGPT users use this skill to create local backups or reviewable archives of their own ChatGPT conversations. It is suited for user-confirmed exports where plaintext sensitivity, local storage location, and cleanup are considered before running.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive ChatGPT history can be written to local plaintext files.

Mitigation: Use index-only mode unless full content is needed, keep exports in a fresh private local directory, avoid sharing raw exports, and purge files promptly after use.

Risk: The authoritative security summary reports relay file-safety gaps that could redirect plaintext exports despite containment claims.

Mitigation: Prefer the default fresh export directory, avoid reused destinations, verify destinations before use, and treat relay destination-safety claims as incomplete until child symlink and race-safe writing are fixed.

Risk: Exporting depends on the active ChatGPT browser session and private ChatGPT endpoints.

Mitigation: Run the export only while logged in to the intended account, review the requested scope before confirming, and stop if the destination or account context is unclear.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/globalcaos/skills/chatgpt-exporter-ultimate)

## Skill Output:

**Output Type(s):** [JSON, Markdown, Shell commands, Guidance]

**Output Format:** [Local JSON and Markdown export files with shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Index-only mode is the default; full conversation content can produce sensitive plaintext files.]

## Skill Version(s):

1.9.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
