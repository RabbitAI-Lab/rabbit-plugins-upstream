## Description:

Open Pinterest in the user's Brave browser and take the user to the Pinterest homepage. Use when the user asks to open, visit, or go to Pinterest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruchir17-cmd](https://clawhub.ai/user/ruchir17-cmd)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to have an agent open Pinterest in Brave, reuse an existing Pinterest tab or authenticated browser session when available, and stop if sign-in is required.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pinterest may recognize the user through an existing signed-in Brave profile.

Mitigation: Use only after the user asks to open Pinterest, do not enter credentials, and stop if Pinterest requires sign-in.

Risk: A browser-opening workflow could be mistaken for permission to perform Pinterest account actions.

Mitigation: Keep the skill limited to opening and verifying Pinterest unless the user separately asks for another action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ruchir17-cmd/skills/open-pinterest)
- [Pinterest homepage](https://www.pinterest.com/)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Text guidance with browser navigation steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reuses one existing Pinterest tab when available, opens one destination tab otherwise, verifies the destination, and stops if login is required.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
