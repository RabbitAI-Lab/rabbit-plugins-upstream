## Description:

Clarifies vague requests by offering candidate directions, asking for missing requirements, and suggesting ready-to-use prompts and relevant YottaMeta skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

People who are unsure how to phrase a request use this skill to choose an intended task, clarify its goal and constraints, and obtain a prompt they can use with an agent. It can also suggest a related YottaMeta skill and installation command.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Session-start loading may influence vague requests before other work begins.

Mitigation: Review always-load behavior before enabling it; use manual invocation or disable persistent loading if unwanted.

Risk: Memory or persistence suggestions could save private or secret information.

Mitigation: Show the intended storage location and content, obtain explicit user confirmation, and exclude private or secret details unless expressly authorized.

Risk: Unpinned npm installation can fetch a different package version later.

Mitigation: Pin and review the npm package version in higher-assurance environments.

## Reference(s):

- [ClawHub release](https://clawhub.ai/yottameta/skills/yotta-prompt)
- [Project homepage (listed in release metadata)](https://github.com/YottaMeta/yotta-prompt)
- [Scenario examples](references/scenarios.md)
- [Frequently asked questions](references/faq.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Conversational text or Markdown; optional JSON from the CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offers 2–4 candidate directions and a ready-to-use prompt; CLI can return structured mappings.]

## Skill Version(s):

0.2.4 (source: skill frontmatter, package.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
