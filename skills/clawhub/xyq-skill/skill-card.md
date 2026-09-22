## Description:

Uses the XiaoYunque/Pippit CLI to generate and edit images, generate and process videos, query and deliver media results, manage personal Canvas assets and drafts, check credits, and handle account authorization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ydtincle](https://clawhub.ai/user/ydtincle)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to route media creation, media processing, Canvas editing, result retrieval, credit lookup, and authorization tasks through an authenticated XiaoYunque/Pippit CLI workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated CLI use can expose account state or credentials if logs or errors are handled carelessly.

Mitigation: Use the documented login and status flows, avoid echoing access keys, and redact credential-like values before showing command output.

Risk: Media generation and processing may consume account credits, especially if a submission is repeated after an uncertain result.

Mitigation: Confirm unclear credit-consuming actions, keep returned thread and run IDs, and query existing tasks instead of resubmitting when success is uncertain.

Risk: Local image, video, or audio paths provided to generation and Canvas commands may be uploaded to the remote service.

Mitigation: Submit only user-approved local files and resolve missing or inaccessible paths before running upload-backed commands.

Risk: First-run or upgrade flows may install or update the Pippit CLI in the user's cache.

Mitigation: Run the documented CLI check first, require the expected Node and network prerequisites, and stop if installation or command validation fails.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ydtincle/skills/xyq-skill)
- [XiaoYunque service endpoint](https://xyq.jianying.com)
- [Artifact: SKILL.md](artifact/SKILL.md)
- [Artifact: installation guide](artifact/scripts/install.md)
- [Artifact: async delivery workflow](artifact/workflows/async-delivery.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands, JSON response checks, local file paths, task identifiers, and media delivery instructions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May initiate authenticated remote media jobs, upload local media through the CLI, download generated outputs locally, and return task links or IDs for later querying.]

## Skill Version(s):

1.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
