## Description:

Helps agents search the web, retrieve pages, and interact with sites through a signed-in browser.

This skill is ready for commercial/non-commercial use.

## Publisher:

[eze-is](https://clawhub.ai/user/eze-is)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use this skill to find and read web information, navigate interactive sites, and access pages requiring an existing browser login.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser automation can access logged-in accounts and perform actions on their behalf.

Mitigation: Use a separate browser profile for sensitive accounts and review requested browser actions.

Risk: A local browser-control service remains running without strong access controls.

Mitigation: Stop the browser-control service after use when it is no longer needed.

Risk: Browser history and bookmarks can expose private browsing information.

Mitigation: Search history or bookmarks only when needed for the task.

Risk: Uploading a local file to an untrusted site can disclose its contents.

Mitigation: Do not upload arbitrary local files to untrusted sites.

## Reference(s):

- [Project homepage (listed in release metadata)](https://github.com/eze-is/web-access)
- [Browser API reference](references/cdp-api.md)
- [Version 2.5.3 migration guide](references/migration-2.5.3.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Text or Markdown, potentially including shell commands and extracted web content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include content retrieved from sites accessible in the user's browser session.]

## Skill Version(s):

2.5.4 (source: server-resolved release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
