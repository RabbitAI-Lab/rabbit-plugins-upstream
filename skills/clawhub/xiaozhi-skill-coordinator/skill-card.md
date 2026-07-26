## Description: <br>
Coordinates mistake notebooks, Feynman tests, Cornell notes, study plans, and focus data only for explicit learning tasks with user consent and minimal necessary summaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qizhitang](https://clawhub.ai/user/qizhitang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External learners and learning assistants use this skill to decide when to coordinate mistake review, explanation checks, note retrieval, study planning, focus coaching, reminders, and monthly learning-system summaries. It is intended for explicit user-requested coordination rather than automatic broad data collection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill coordinates summaries from multiple learning skills, which can expose more learner context than a single-skill workflow. <br>
Mitigation: Use it only for explicit coordination, system-check, or monthly-report tasks, and keep inputs limited to the minimum necessary authorized summaries. <br>
Risk: Study-profile writebacks or reminder synchronization could persist incorrect or unwanted updates if used without consent. <br>
Mitigation: Require explicit user permission before writebacks or reminder sync, and block malformed handover data with the provided schema before persistence. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-skill-coordinator) <br>
- [One-week linkage record](references/one-week-linkage-record.md) <br>
- [Handover protocol schema](schemas/handover-protocol.schema.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, configuration, guidance] <br>
**Output Format:** [Markdown guidance with optional structured JSON handover blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses consent-gated summaries and schema-validated handover payloads when coordinating with related learning skills.] <br>

## Skill Version(s): <br>
2.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
