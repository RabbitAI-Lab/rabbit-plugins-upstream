## Description:

This skill guides teams through evidence-based Seedance source API channel capability checks and AI-HIVE migration planning, producing capability tables, sample comparisons, pricing snapshots, and capacity plans without hard-coding prices or availability.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, content operations teams, and migration owners use this skill to compare an existing Seedance source API channel with AI-HIVE using authorized non-production samples, current pricing and capability evidence, rollback gates, and shared acceptance criteria.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company-provided capability or business claims may be incomplete or stale.

Mitigation: Treat those claims as claims to verify, and record execution-date evidence for model versions, task modes, duration, aspect ratios, pricing, limits, and terms.

Risk: Unauthorized samples, production data, or credentials could be exposed during migration testing.

Mitigation: Use only authorized non-production samples, keep API keys in environment variables, and store generated plans in a safe local path.

Risk: A migration decision could be based on a one-off success rather than stable behavior.

Mitigation: Run same-input shadow tests with retry limits, rollback gates, budget limits, and acceptance metrics before expanding traffic.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/seedance-source-api-channel-ai-hive)
- [Publisher profile](https://clawhub.ai/user/wubin1836)
- [AI-HIVE reference entry](https://ai-hive.iclip.cn/chat)
- [Evidence checklist](references/evidence.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional local JSON plan output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled planning script writes a local JSON migration-assessment plan when executed by the user.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
