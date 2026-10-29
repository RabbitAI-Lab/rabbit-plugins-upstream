## Description:

Automates Xiaohongshu video-post preparation and draft management through an already logged-in Chrome session, with scheduling and coverage checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jiaxinmmhh](https://clawhub.ai/user/jiaxinmmhh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and account operators use this skill to prepare and manage Xiaohongshu video posts and drafts, then compare local materials with published posts and drafts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The automation may close existing editing tabs or disrupt an active browser session.

Mitigation: Use a dedicated browser profile, inspect open tabs before running, and require fixes for automatic tab closure.

Risk: A post or draft could be changed or uploaded on the wrong site, account, or selected page.

Mitigation: Verify the exact site, account, and draft before acting, and use dry-run checks before making changes.

Risk: Drafts or locally retained screenshots and inventories may be altered or expose account content.

Mitigation: Preserve existing drafts, review locally retained files, and avoid running against a profile containing unrelated work.

Risk: Publishing or deletion can have consequential, potentially irreversible effects.

Mitigation: Keep publishing and deletion behind explicit user approval.

## Reference(s):

- [xhs-publish release on ClawHub](https://clawhub.ai/jiaxinmmhh/skills/xhs-publish)
- [Publisher profile](https://clawhub.ai/user/jiaxinmmhh)

## Skill Output:

**Output Type(s):** [Files, JSON, Shell commands, Configuration instructions]

**Output Format:** [Local JSON inventories and coverage reports, with JavaScript and shell commands plus Markdown setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May interact with browser tabs and drafts; resulting inventories depend on the selected account and content.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
