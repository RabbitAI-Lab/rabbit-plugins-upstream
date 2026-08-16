## Description:

Assembles a detailed company or project dossier from public sources, tracing every claim to verified evidence through coordinated role workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[t3ratech](https://clawhub.ai/user/t3ratech)

### License/Terms of Use:

MIT-0

## Use Case:

Research, diligence, and review teams use this skill to gather public company or project information, assess risk, trace evidence, and produce a sourced dossier.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundle includes an unscoped trading-risk role with broad MCP and event-publishing authority that does not fit the stated diligence purpose.

Mitigation: Review role permissions before installation and disable or strictly constrain MCP invocation and event publishing unless those capabilities are explicitly intended.

Risk: MCP tools or event publishing could affect sensitive integrations if installed in a connected environment.

Mitigation: Run the skill in an isolated workspace where MCP tools and event publishing cannot reach trading systems or other sensitive services.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/t3ratech/skills/due-diligence-team)
- [Publisher profile](https://clawhub.ai/user/t3ratech)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown dossier with evidence tracing]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Claims should be tied to collected public-source evidence.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
