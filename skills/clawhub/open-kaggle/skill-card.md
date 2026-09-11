## Description:

Open Kaggle in the user's Brave browser and take the user to the Kaggle homepage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruchir17-cmd](https://clawhub.ai/user/ruchir17-cmd)

### License/Terms of Use:

MIT-0

## Use Case:

Users ask the agent to open, visit, or go to Kaggle in Brave. The skill opens the Kaggle homepage, reuses an existing matching tab or browser session when possible, verifies the destination, and stops at login if authentication is required.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may open Kaggle using the user's existing signed-in Brave profile.

Mitigation: Install and run it only when reuse of the existing Kaggle browser session is acceptable.

Risk: Authentication may be required before Kaggle is available.

Mitigation: The skill stops at the login page and tells the user to sign in; it should not enter or store credentials.

Risk: Browser navigation could land somewhere other than the intended Kaggle homepage.

Mitigation: The skill verifies that the loaded destination is the expected Kaggle website before reporting success.

## Reference(s):

- [Kaggle Homepage](https://www.kaggle.com/)
- [ClawHub Skill Page](https://clawhub.ai/ruchir17-cmd/skills/open-kaggle)
- [Publisher Profile](https://clawhub.ai/user/ruchir17-cmd)

## Skill Output:

**Output Type(s):** [Text, Guidance, Configuration]

**Output Format:** [Markdown status updates and concise user-facing guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reuse the user's existing Brave browser session and matching Kaggle tab.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
