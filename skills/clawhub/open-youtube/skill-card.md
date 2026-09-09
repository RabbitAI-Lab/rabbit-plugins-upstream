## Description:

Open YouTube in the user's Brave browser and take the user to YouTube's homepage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruchir17-cmd](https://clawhub.ai/user/ruchir17-cmd)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent open YouTube in Brave, reuse an existing YouTube tab when possible, and confirm that the homepage loaded without handling credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may focus or open Brave and load YouTube using the user's existing browser session.

Mitigation: Install only if that browser behavior is acceptable, and review the visible destination before taking further account actions.

Risk: A sign-in prompt could expose an authentication boundary.

Mitigation: Stop at login prompts; the skill instructions prohibit entering passwords, authentication codes, API keys, or other credentials.

## Reference(s):

- [ClawHub open-youtube skill](https://clawhub.ai/ruchir17-cmd/skills/open-youtube)
- [YouTube homepage](https://www.youtube.com/)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown skill instructions with YAML configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reuses the user's existing Brave browser session, avoids duplicate YouTube tabs, verifies the destination, and stops at login prompts.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
