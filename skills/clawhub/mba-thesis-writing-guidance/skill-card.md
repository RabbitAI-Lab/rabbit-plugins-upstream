## Description:

Guides agents and users through Chinese MBA and EMBA thesis planning, structure, evidence alignment, revision, and defense preparation without fabricating data, literature, cases, or advisor feedback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stephenlzc](https://clawhub.ai/user/stephenlzc)

### License/Terms of Use:

MIT

## Use Case:

External MBA and EMBA students, advisors, and agent-assisted writing workflows use this skill to narrow thesis topics, map five-chapter structures, select supporting theory, check evidence paths, revise drafts, and prepare for defense. It is guidance for planning and review, not a thesis ghostwriting or source-fabrication tool.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may guide an agent to scan thesis project files or create local project configuration that could include sensitive work, employer, colleague, customer, or internal data.

Mitigation: Install it only in the relevant thesis project, redact or anonymize sensitive materials before use, and review proposed school-format.yaml, thesis-config.yaml, and work-resource.md changes before saving.

Risk: MBA thesis work can be weakened by unsupported claims, fabricated sources, fabricated data, or over-delegated judgment.

Mitigation: Require the user to verify school rules, citations, data, and final claims; keep the skill limited to planning, checklist-based review, evidence alignment, and draft guidance.

## Reference(s):

- [Server-resolved source repository](https://github.com/stephenlzc/MBA-thesis-writing-guidance)
- [ClawHub skill page](https://clawhub.ai/stephenlzc/skills/mba-thesis-writing-guidance)
- [SKILL.md](SKILL.md)
- [README.md](README.md)
- [AI Use Boundaries](references/ai-use.md)
- [Thesis Structure Corpus Guide](references/corpus-guide.md)
- [Method Guide](references/methods/method-guide.md)
- [Claude Agent Skills Overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Humanize MBA Text Companion Skill](https://github.com/stephenlzc/humanize-mba-text-skill)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown and plain-text guidance with checklist references and YAML configuration suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose project-local school-format.yaml, thesis-config.yaml, and work-resource.md updates for user review.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
