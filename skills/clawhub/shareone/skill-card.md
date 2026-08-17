## Description:

Host HTML/Markdown pages and share PDF, Word, or PowerPoint docs as ShareOne short links for publishing pages/docs, adding passwords or watermarks, comments, downloads, and updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beep879](https://clawhub.ai/user/beep879)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill to publish generated HTML, Markdown, text, PDF, Word, and PowerPoint content to ShareOne links, then manage downloads, settings, comments, collaborators, refreshes, and deletion. It is useful when a user wants a shareable hosted link or needs to update an existing ShareOne share.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload selected files or conversation-derived content to public external ShareOne links.

Mitigation: Use explicit ShareOne requests, review content before publishing, and avoid secrets or private documents.

Risk: Credential handling may expose an API key through command output, logs, or local storage.

Mitigation: Prefer secure secret storage and rotate any API key that may have appeared in output or logs.

Risk: The skill can mutate access settings, collaborators, comments, and share deletion state.

Mitigation: Confirm exact share IDs, links, and usernames before delete, collaborator, or access-control changes.

Risk: Page data features can store shared data where visitors may read it.

Mitigation: Enable page data only when requested, and use private local storage for sensitive user data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beep879/skills/shareone)
- [ShareOne service](https://shareone.app)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Files, Markdown]

**Output Format:** [Markdown guidance with inline shell commands, JSON script output, saved files, and ShareOne links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update public external ShareOne links and may require ShareOne credentials for owner operations.]

## Skill Version(s):

1.2.10 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
