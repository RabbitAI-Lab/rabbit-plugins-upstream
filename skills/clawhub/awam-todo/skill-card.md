## Description:

Helps users capture and manage personal to-dos from conversation, with dated local Markdown storage, task dependencies, subtasks, and a local web dashboard.

This skill is ready for commercial/non-commercial use.

## Publisher:

[awamwang](https://clawhub.ai/user/awamwang)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and teams use this skill to record, organize, and update local to-dos through an agent or a browser dashboard, including due dates, dependencies, subtasks, and task status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local web service exposes unauthenticated cross-origin task read/write endpoints.

Mitigation: Do not leave the service running while browsing untrusted sites; bind only to 127.0.0.1 and prefer a release with authentication, CSRF, and origin checks.

Risk: Unsafe date-based paths may allow unintended access to task files or local path metadata.

Mitigation: Review storage locations and avoid sensitive data until strict date and path validation is available.

Risk: The web dashboard can change task files and open local folders or an editor.

Mitigation: Run it only when needed and review its access to local files and configured editor before installation.

## Reference(s):

- [awam-todo ClawHub release](https://clawhub.ai/awamwang/skills/awam-todo)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Conversational text and Markdown task summaries, with local task files updated by commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Task records and indexes are stored locally; the dashboard supports task management.]

## Skill Version(s):

0.4.0 (source: SKILL.md frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
