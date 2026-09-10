## Description:

Open Reddit in the user's Brave browser and take the user to the Reddit homepage. Use when the user asks to open, visit, or go to Reddit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruchir17-cmd](https://clawhub.ai/user/ruchir17-cmd)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill when they want an agent to open Reddit in Brave, reuse an existing Reddit tab or browser session when available, and verify that the homepage loaded.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may open Reddit using an already signed-in Brave browser session.

Mitigation: Install only when reuse of the user's Brave profile is acceptable; the skill does not request credentials and stops if Reddit requires sign-in.

Risk: Opening Reddit could expose the user's account state or personalized homepage in the browser.

Mitigation: Use it only for opening and verifying the Reddit homepage; the skill does not post, like, comment, message, purchase, or change account settings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ruchir17-cmd/skills/open-reddit)
- [Reddit homepage](https://www.reddit.com/)

## Skill Output:

**Output Type(s):** [Guidance, Text]

**Output Format:** [Plain text confirmation after browser navigation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Opens one Reddit destination tab in Brave, reuses existing Reddit tabs and authenticated browser sessions when available, and stops at login prompts.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
