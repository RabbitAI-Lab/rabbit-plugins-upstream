## Description:

Open Vercel in the user's Brave browser and take the user to the Vercel homepage or dashboard when an authenticated session is available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruchir17-cmd](https://clawhub.ai/user/ruchir17-cmd)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other Vercel users can use this skill to open Vercel in Brave, reuse an existing Vercel tab or signed-in session when present, and stop at login if authentication is required.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may reuse an already-signed-in Brave session and expose the loaded Vercel page to the agent.

Mitigation: Install and run it only in environments where the user is comfortable with the agent viewing the Vercel page; the skill must not handle credentials or make account changes.

## Reference(s):

- [Vercel](https://vercel.com/)

## Skill Output:

**Output Type(s):** [guidance, shell commands]

**Output Format:** [Text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Opens or focuses Brave, navigates to Vercel, verifies the destination, and reports whether user sign-in is needed.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
