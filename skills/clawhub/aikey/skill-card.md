## Description:

Routes creators and business owners to appropriate AI KEY skills for content and business tasks, with guided onboarding and next-step navigation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

Independent creators and business owners use this skill to select relevant AI KEY tools, get a ready-to-send task prompt, or identify the next step after completing a task.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic update checks may contact GitHub and write a local check timestamp without separate confirmation.

Mitigation: Review the update-check behavior before installation; use a no-script version if network checks or local writes are not acceptable.

Risk: Local scripts can list installed AI KEY skills and their real paths, and the skill may write local memory files.

Mitigation: Review the scripts and limit filesystem access to directories you are comfortable sharing with the agent.

## Reference(s):

- [AI KEY release on ClawHub](https://clawhub.ai/iamzifei/skills/aikey)
- [AI KEY interaction guide](references/交互规范.md)
- [AI KEY decision rules](references/规则卡.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with a recommended skill, a reusable task prompt, or numbered next steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offers a guided onboarding walkthrough when requested.]

## Skill Version(s):

0.3.10 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
