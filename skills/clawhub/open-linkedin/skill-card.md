## Description:

Open LinkedIn in the user's Brave browser and take the user to the LinkedIn homepage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruchir17-cmd](https://clawhub.ai/user/ruchir17-cmd)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill when they want an agent to open LinkedIn in Brave, reuse an existing LinkedIn tab or session when available, and confirm the homepage loaded. The skill stops at sign-in prompts and does not perform account actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may use an existing logged-in browser session.

Mitigation: Do not enter credentials or authentication codes, stop at login prompts, and avoid account-modifying actions unless separately requested.

Risk: Opening LinkedIn could create duplicate tabs or navigate to the wrong destination.

Mitigation: Reuse an existing LinkedIn tab when available, open only one destination tab otherwise, and verify that the LinkedIn homepage is visibly loaded.

## Reference(s):

- [LinkedIn homepage](https://www.linkedin.com/)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration]

**Output Format:** [Text instructions with browser-opening actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reuses an existing Brave session and LinkedIn tab when available, verifies the destination, and stops at login prompts.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
