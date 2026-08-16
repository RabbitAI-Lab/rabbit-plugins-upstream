## Description:

Automates browser tasks across roles to map sites, plan runs, execute supervised web workflows, and verify results on sites without usable APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[t3ratech](https://clawhub.ai/user/t3ratech)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to coordinate browser automation roles for websites that lack usable APIs, including site mapping, workflow execution, evidence capture, and review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use broad browser, web, file, memory, MCP, and agent tools for web automation workflows.

Mitigation: Keep runs supervised for sensitive websites and review proposed file writes or MCP actions before allowing them.

Risk: Browser workflows can involve private account, session, or website data.

Mitigation: Avoid storing private account or session information in memory unless it is necessary for the task.

Risk: A team that fails its own evaluations may not be ready for use.

Mitigation: Run the bundled evaluation set before use and resolve failures before relying on the skill for work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/t3ratech/skills/web-automation-team)
- [Publisher profile](https://clawhub.ai/user/t3ratech)
- [Artifact SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and plain text with browser workflow plans, evidence summaries, commands, or configuration snippets when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include review findings and supervised browser-action guidance.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
