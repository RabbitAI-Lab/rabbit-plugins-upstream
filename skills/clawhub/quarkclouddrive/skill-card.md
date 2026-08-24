## Description:

quarkclouddrive lets an agent authenticate with Quark Drive to upload, read, search, share, transfer, organize, summarize, and answer questions over cloud files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[quarkdrive](https://clawhub.ai/user/quarkdrive)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to operate Quark Drive accounts from an agent workflow, including file upload, reading, search, sharing, transfer, media organization, and file-based AI summary or question answering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires Quark Drive account authorization and can operate on cloud files and shares.

Mitigation: Authorize only an account whose files you are comfortable letting the agent access, and review file-changing requests before allowing upload, move, share, transfer, organize, or uninstall actions.

Risk: The installer can download or update skill code and may change the local Node.js installation.

Mitigation: Run the installer only in an environment where installer-managed downloads and Node.js changes are acceptable, and review installation output before continued use.

Risk: The skill passes original user prompts for service tracking and may use remote AI processing for file summary, question answering, search, or organization.

Mitigation: Avoid highly sensitive prompts or files unless raw prompt telemetry and remote AI processing are acceptable for the intended account and workflow.

## Reference(s):

- [Quark Drive](https://pan.quark.cn)
- [Authorization and account management](references/auth.md)
- [File upload](references/file-upload.md)
- [File read](references/file-read.md)
- [File search](references/file-search.md)
- [File sharing](references/file-share.md)
- [Share transfer](references/file-saveas.md)
- [File operations](references/file-ops.md)
- [Photo and video organization](references/file-organize.md)
- [AI assistant](references/assistant.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with command invocations and structured cloud-file results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Quark Drive links, local file paths, OAuth prompts, search-result tables, and AI-generated summaries or answers.]

## Skill Version(s):

1.0.13 (source: server release metadata; artifact frontmatter says 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
