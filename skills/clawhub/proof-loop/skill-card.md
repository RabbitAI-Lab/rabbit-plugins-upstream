## Description:

Run evidence-gated coding sprints with frozen ACs, separated builder/verifier roles, and durable proof artifacts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[leostehlik](https://clawhub.ai/user/leostehlik)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use Proof Loop to run coding tasks with frozen acceptance criteria, separate builder and verifier roles, and repo-local proof artifacts before work is considered done.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Helper commands can create or update proof-task files in the selected repository.

Mitigation: Confirm the repository root and task id before running helpers, and review generated artifacts before relying on them.

Risk: Installing harness guides changes agent guidance files in the target repository.

Mitigation: Treat guide installation as an explicit repository change and use dry-run or review mode before writing files.

Risk: A coding agent may treat the workflow as proof without independent verification.

Mitigation: Require a fresh verifier session and keep PASS, FAIL, or UNKNOWN verdicts tied to each frozen acceptance criterion.

## Reference(s):

- [Proof Loop Workflow](references/workflow.md)
- [Artifact Schemas](references/artifacts.md)
- [Agent Brief Template](references/brief-template.md)
- [Loopsmith Bridge](references/loopsmith-bridge.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance, JSON proof artifacts, and shell command recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates and checks repo-local task artifacts under .agent/tasks/<TASK_ID>/ when the user explicitly requests a Proof Loop workflow.]

## Skill Version(s):

0.2.4 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
