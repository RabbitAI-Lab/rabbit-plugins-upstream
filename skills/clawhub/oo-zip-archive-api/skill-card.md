## Description:

Zip Archive API (archiveapi.com). Use this skill for ANY Zip Archive API request — reading, creating, and updating data. Whenever a task involves Zip Archive API, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Zip Archive API through an OOMOL-connected account, including compressing publicly accessible files into ZIP archives and extracting publicly accessible archives into transit-hosted files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup instructs users to execute mutable remote installer scripts directly in a shell.

Mitigation: Review the installer path before installing, prefer a verified official release or package source, and run curl-to-bash or irm-to-iex commands only after accepting the remote-code execution risk.

Risk: The extract_archive action is marked as a write action.

Mitigation: Confirm the exact extract_archive payload and expected effect with the user before running the connector action.

## Reference(s):

- [Zip Archive API homepage](https://archiveapi.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-zip-archive-api)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses from connector actions are JSON objects with data and meta.executionId fields.]

## Skill Version(s):

1.0.2 (source: frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
