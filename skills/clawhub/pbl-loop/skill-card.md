## Description:

PBL Loop guides agents through start, checkpoint, and transfer modes for project-based capability learning while separating delivery evidence from capability evidence and tracking provenance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlxeva](https://clawhub.ai/user/dlxeva)

### License/Terms of Use:

MIT-0

## Use Case:

People using agent assistants for project-based learning use this skill to set a learning contract, checkpoint evidence, and test transfer readiness without confusing delivery status with capability growth.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can shape answers into a required start, checkpoint, or transfer schema when explicitly triggered.

Mitigation: Apply it only when the user asks for a learning goal, reflection, transfer, teaching, replication, or a PBL growth loop.

Risk: Durable notes could preserve learning-loop state beyond the current conversation if persistence is enabled.

Mitigation: Keep the default stateless posture unless the user authorizes notes in a user-selected project-local location.

## Reference(s):

- [Server-resolved GitHub provenance: dlxeva/pbl-loop](https://github.com/dlxeva/pbl-loop/tree/main/pbl-loop)
- [PBL Loop trigger / boundary tests](references/trigger-boundary-tests.md)
- [FlowGrid](https://github.com/dlxeva/FlowGrid)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Structured Markdown or JSON-style response fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Conversation-only by default; optional durable notes require user approval and a user-selected project-local location.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
