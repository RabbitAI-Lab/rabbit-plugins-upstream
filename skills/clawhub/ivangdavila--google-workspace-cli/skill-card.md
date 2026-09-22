## Description:

Google Workspace CLI helps agents operate Google Workspace through the gws CLI for Gmail, Drive, Calendar, Editors, Admin SDK, troubleshooting, automation, and MCP exposure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and Google Workspace administrators use this skill to plan and run Workspace operations through gws, including mail and file workflows, calendar and editor tasks, admin reporting, troubleshooting, and controlled automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Google Workspace scopes can grant broad access to mail, files, calendars, and tenant administration.

Mitigation: Use narrow OAuth scopes where possible, set an explicit --account for each operation, and keep the default write policy at dry-run-first.

Risk: Bulk sending, sharing, admin changes, and deletion can affect many users or resources.

Mitigation: Resolve stable IDs, review dry-run output or preview artifacts, require confirmation for writes, prefer trash or drafts over permanent actions, and verify state after execution.

Risk: Fetched Gmail, Docs, Chat, or other user-controlled content can carry prompt-injection text into downstream agent workflows.

Mitigation: Use the skill's sanitize mode for fetched content, prefer read-only scoped sessions for investigation, and avoid passing unsanitized external text into autonomous write loops.

Risk: MCP exposure can give an agent many Google Workspace tools, including write-capable methods when the token has write scopes.

Mitigation: Expose only the services needed for the current workflow, record MCP profiles, pair write-capable sessions with change-control gates, and use read-only scopes when mutation is not required.

Risk: Unattended automation can fail silently, repeat work, or run under the wrong account when authentication, pagination, or state tracking is weak.

Mitigation: Preflight authentication non-interactively, pass explicit accounts, bound pagination, persist resume tokens or high-water marks, use idempotency markers, and log run counts and failures.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/ivangdavila/skills/google-workspace-cli)
- [Clawic skill page](https://clawic.com/skills/google-workspace-cli)
- [Google APIs Discovery Service](https://www.googleapis.com/discovery/v1/apis)
- [Google Accounts OAuth endpoint](https://accounts.google.com)
- [Google OAuth token endpoint](https://oauth2.googleapis.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON request bodies, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands assume gws and jq are installed and require user-provided account, scopes, and target identifiers.]

## Skill Version(s):

1.0.3 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
