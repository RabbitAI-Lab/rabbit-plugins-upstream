## Description:

Coordinates deep research workflows for systematic research, competitor analysis, option comparison, trend analysis, fact-checking, and sourced report creation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sensenova-skills](https://clawhub.ai/user/sensenova-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to run multi-source research, verify evidence, and produce structured research reports for complex questions that need comparison, sourcing, or fact checking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled local research workbench can expose or modify local files beyond a passive progress page.

Mitigation: Use the skill only in a trusted environment, bind the workbench to localhost where possible, and avoid pointing it at sensitive directories.

Risk: Agent and API credentials may be available to the workflow environment.

Mitigation: Use least-privileged credentials, keep secrets in environment variables only, and avoid running the workflow with credentials unrelated to the research task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sensenova-skills/skills/sn-deep-research)
- [Skill orchestration instructions](artifact/SKILL.md)
- [Research agent evidence workflow](artifact/agents/research.md)
- [Report writer workflow](artifact/agents/report-writer.md)
- [Review agent workflow](artifact/agents/review.md)
- [Evidence schema](artifact/schemas/evidence.schema.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, JSON research artifacts, progress updates, and shell or configuration guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create a report directory with evidence files, source snapshots, outlines, content units, rendered reports, citations, and workbench progress artifacts.]

## Skill Version(s):

2026.8.19 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
