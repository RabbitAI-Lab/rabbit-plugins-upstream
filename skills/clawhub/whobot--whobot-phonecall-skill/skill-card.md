## Description:

Helps businesses discover, try, create, and tune WhoBot AI phone agents for customer and personal calling tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[whobot](https://clawhub.ai/user/whobot)

### License/Terms of Use:

MIT-0

## Use Case:

Business owners, operations teams, and sales leaders use this skill to find relevant phone agents, review examples, try calls, create or tune agents, manage lead campaigns, and handle account tasks.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Setup uses an unpinned CLI release channel, so the installed version may change over time.

Mitigation: Review the package and setup guidance before installation; pin and verify a version when repeatability matters.

Risk: Calls and uploaded lead information may involve data leaving the user's environment.

Mitigation: Review WhoBot's privacy terms, obtain any required consent, and share only the information needed for the requested task.

Risk: Call recordings may be saved locally.

Mitigation: Tell affected people as required and restrict access to recordings, with retention and deletion handled under the organization's policy.

Risk: The security review was partial because some referenced local files could not be matched.

Mitigation: Review the referenced materials and release contents before installation or sensitive actions; treat the scanner verdict as a caution, not proof of malicious intent.

## Reference(s):

- [Product overview](references/product.md)
- [Find benchmark agents](references/find-benchmark.md)
- [Set up and update the tool](references/setup.md)
- [Lead campaign guidance](references/leads.md)
- [Personal assistant guidance](references/personal-assistant.md)
- [WhoBot website](https://whobot.com)
- [WhoBot management platform](https://work.whobot.com/)
- [WhoBot skill information](https://www.whobot.com/skills)
- [ClawHub skill page](https://clawhub.ai/whobot/skills/whobot-phonecall-skill)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Concise Chinese conversational responses and structured choice or confirmation cards]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Relies on current tool results for call, account, and campaign status; does not invent unavailable details.]

## Skill Version(s):

2.1.5 (source: skill frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
