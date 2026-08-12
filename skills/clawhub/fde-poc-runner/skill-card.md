## Description:

Run deployable solutions and agent skills in representative or controlled customer scenarios against pre-agreed evidence, tests, and success criteria, then produce a Continue, Adjust, or Stop decision report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xukun0821](https://clawhub.ai/user/xukun0821)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, field engineers, and customer validation teams use this skill to run controlled POC trials, preserve evidence, compare results with frozen criteria, and recommend Continue, Adjust, Pause, or Stop decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: POC runs may involve approved datasets, participants, environments, evidence storage, real-system connections, UAT, and Continue/Adjust/Stop decisions.

Mitigation: Confirm approval for datasets, participants, environments, and evidence storage before installation or use, and require human approval before connecting to real systems, running UAT, deleting samples, rerunning failed samples, or making Continue/Adjust/Stop decisions.

Risk: Evaluation summaries can be mistaken for full POC conclusions or root-cause analysis.

Mitigation: Use the summary script only as a local reporting helper, preserve raw evidence and failed records, and complete human review against frozen criteria before declaring a result.

## Reference(s):

- [FDE POC Runner on ClawHub](https://clawhub.ai/xukun0821/skills/fde-poc-runner)
- [POC Run Input Guide](references/poc-input-guide.md)
- [POC Operation Manual](references/poc-operations.md)
- [POC Evaluation and Decision Rules](references/evaluation-rules.md)
- [POC Operation and Verification Report Template](references/poc-run-report.md)
- [POC Run Quality Score](references/poc-quality-rubric.md)
- [UAT and Production Transition Verification](references/uat-and-transition.md)
- [POC Operations Field Manual](references/poc-field-handbook.md)
- [POC Run Complete Example](references/poc-worked-example.md)
- [AWS: Successful Generative AI POC](https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/dev-architecting.html)
- [AWS: Generative AI Experiment Evaluation Loop](https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/dev-experimenting-experimentation-loops.html)
- [AWS: Advance from POC to Pre-Production](https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/dev-advancing.html)
- [Anthropic: Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- [OpenAI Evals API](https://platform.openai.com/docs/api-reference/evals)
- [Azure: Architecture Testing Strategy](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/testing)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown reports and decision guidance with optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional local Node.js helper summarizes evaluation JSON and can exit nonzero when hard failures are present.]

## Skill Version(s):

1.0.0 (source: server release metadata and TRUST-CARD.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
