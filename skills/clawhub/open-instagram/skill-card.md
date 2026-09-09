## Description:

Open Instagram in the user's Brave browser and take the user to the Instagram homepage. Use when the user asks to open, visit, or go to Instagram.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruchir17-cmd](https://clawhub.ai/user/ruchir17-cmd)

### License/Terms of Use:

MIT-0

## Use Case:

People who use an agent on a desktop can ask it to open Instagram in Brave, reuse an existing Instagram tab or browser session when available, and stop at sign-in if authentication is required.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill opens a social media site in the user's existing browser session.

Mitigation: Reuse the existing session only when available, stop at sign-in, and never enter passwords, authentication codes, API keys, or other credentials.

Risk: The skill could be mistaken for an account-action skill.

Mitigation: Keep behavior limited to opening and verifying Instagram; do not search, post, like, comment, follow, message, upload, purchase, create accounts, or modify settings unless separately requested.

## Reference(s):

- [Instagram homepage](https://www.instagram.com/)
- [ClawHub skill page](https://clawhub.ai/ruchir17-cmd/skills/open-instagram)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with browser-action status updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May focus or open Brave, reuse an existing Instagram tab, and report when Instagram is loaded or sign-in is required.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
