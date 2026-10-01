## Description:

Clarifies vague user requests into candidate directions, asks focused follow-up questions, and suggests ready-to-use prompts and relevant skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

People who are unsure how to phrase a request use this skill to explore possible intentions, define their goal and constraints, and obtain a prompt they can use with an AI agent. Developers can also use its local CLI to obtain candidate directions or skill mappings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Session-start loading can influence every new conversation.

Mitigation: Review before enabling persistent loading; obtain user consent, or invoke manually and disable always-load where supported.

Risk: Broad installation options can place the skill in multiple agent directories.

Mitigation: Inspect installation targets, avoid broad or global options, and pin package versions rather than running unversioned npx commands.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/yottameta/skills/yotta-prompt)
- [Project homepage](https://github.com/YottaMeta/yotta-prompt)
- [Usage FAQ](artifact/references/faq.md)
- [Scenario examples](artifact/references/scenarios.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Markdown, Shell commands]

**Output Format:** [Conversational text or Markdown; optional JSON from the CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides two to four candidate directions, follow-up questions, self-contained prompts, and optional skill installation suggestions.]

## Skill Version(s):

0.2.3 (source: skill frontmatter, package.json, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
