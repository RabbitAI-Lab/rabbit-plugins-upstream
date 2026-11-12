## Description:

Helps users discover, try, create, and refine WhoBot AI phone employees for business calling tasks and personal call assistance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[whobot](https://clawhub.ai/user/whobot)

### License/Terms of Use:

MIT-0

## Use Case:

Business owners, operations teams, and sales teams use this skill to find, try, create, and refine voice agents for follow-ups, invitations, reminders, lead screening, sales, and hotline calls. Individuals can use its personal-assistant flow for specific calls such as restaurant reservations.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Requests are sent verbatim to an external benchmark service.

Mitigation: Avoid including sensitive details in benchmark requests; provide only the information needed to find a suitable agent.

Risk: Setup installs a CLI from an unpinned latest version channel.

Mitigation: Review the install target and decide whether an unpinned latest release is acceptable before installing.

Risk: The security scan was partial because some local path-like references could not be matched to bundled files.

Mitigation: Review those unresolved references before relying on the behaviors they describe.

## Reference(s):

- [WhoBot skill release on ClawHub](https://clawhub.ai/whobot/skills/whobot-phonecall-skill)
- [WhoBot official website](https://whobot.com)
- [WhoBot product documentation](https://whobot.com/llms.txt)
- [WhoBot pricing](https://whobot.com/pricing)
- [WhoBot Skills documentation](https://www.whobot.com/skills)

## Skill Output:

**Output Type(s):** [Guidance, Text, Shell commands]

**Output Format:** [Conversational guidance and structured choice or confirmation prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Business actions such as calls and lead uploads follow confirmation steps; available actions and results are determined by the product response.]

## Skill Version(s):

2.0.7 (source: release.json and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
