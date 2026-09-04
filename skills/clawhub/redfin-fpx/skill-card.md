## Description:

Query redfin.com from a shell with the fpx CLI to resolve locations and addresses, search listings, inspect property details, retrieve market and rental data, extract climate-risk and photo information, and access signed-in saved homes or saved searches through a paired browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate fpx setup steps, Redfin endpoint calls, and parsing guidance for real-estate search, property detail, history, trend, rental, climate-risk, photo, saved-home, and saved-search workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Redfin requests are routed through the user's paired browser tab and may include signed-in saved homes, saved searches, or other account-specific pages.

Mitigation: Use a signed-out or separate browser profile when account-specific Redfin data should not be available to the skill's commands.

Risk: The skill produces shell commands and endpoint calls that depend on a paired Transporter browser session.

Mitigation: Review generated commands before running them and confirm the active browser profile and Redfin tab are appropriate for the task.

## Reference(s):

- [Redfin Stingray Endpoints for fpx](references/stingray-endpoints.md)
- [ClawHub Skill Page](https://clawhub.ai/chrischall/skills/redfin-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON parsing examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should be reviewed before execution because requests route through the user's paired browser session and may access signed-in Redfin account data.]

## Skill Version(s):

0.12.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
