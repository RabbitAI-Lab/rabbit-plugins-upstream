## Description:

Publishes, schedules, and checks the status of social posts, images, and videos across connected social channels through an InstallMyClaw workspace.

This skill is ready for commercial/non-commercial use.

## Publisher:

[junwei1213](https://clawhub.ai/user/junwei1213)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to publish, schedule, and monitor content on connected social media accounts from Claude Code or Codex. It supports account discovery, media upload, draft creation, explicit confirmation, status checks, and per-platform publishing guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a workspace publishing key and can upload media and publish to connected social accounts.

Mitigation: Store the key in an environment variable or secrets manager, never paste it into chat or commit it, and require a preview plus explicit confirmation before confirm or post actions.

Risk: The built-in updater can replace installed skill code from a moving GitHub branch without integrity checks.

Mitigation: Prefer the platform-managed updater, review changes before updating, and do not run the built-in update command unprompted during a publishing task.

Risk: A draft could target the wrong platform, account, caption, media, or schedule if the preview is not checked carefully.

Mitigation: Show the returned preview verbatim, require one clear confirmation per draft, and create a new draft after any user edit.

## Reference(s):

- [Platform notes](references/platforms.md)
- [ClawHub skill page](https://clawhub.ai/junwei1213/skills/imc-publish)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and an IMC_PUBLISH_API_KEY for a connected InstallMyClaw workspace; publishing is confirmation-gated.]

## Skill Version(s):

1.0.6 (source: server release metadata, artifact frontmatter, client script)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
