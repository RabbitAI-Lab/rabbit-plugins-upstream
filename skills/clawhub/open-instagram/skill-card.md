## Description:

Open Instagram in the user's Brave browser and take the user to the Instagram homepage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruchir17-cmd](https://clawhub.ai/user/ruchir17-cmd)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill as a browser shortcut to open Instagram in Brave, reuse an existing Instagram tab or session when available, and verify that the homepage loaded.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may use an already signed-in Brave browser session to load Instagram.

Mitigation: Do not enter credentials or authentication codes; stop and tell the user authentication is required if Instagram prompts for login.

Risk: A browser shortcut could be mistaken for permission to perform account actions.

Mitigation: Limit behavior to opening and verifying Instagram; do not post, like, comment, follow, message, upload, purchase, or change account settings unless separately and explicitly requested.

## Reference(s):

- [Instagram homepage](https://www.instagram.com/)
- [ClawHub skill page](https://clawhub.ai/ruchir17-cmd/skills/open-instagram)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with concise status updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May focus or open Brave, reuse an existing Instagram tab, and stop if login is required.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
