## Description:

NeuralMemory provides associative memory with spreading activation for persistent, intelligent recall across agent sessions without requiring an LLM dependency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nhadaututtheky](https://clawhub.ai/user/nhadaututtheky)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to add persistent associative memory to OpenClaw or MCP-based workflows. It helps agents store decisions, preferences, errors, TODOs, and other context, then recall related memories across sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create an agent-wide persistent memory layer with broad automatic capture and recall of conversation context.

Mitigation: Review the OpenClaw configuration before enabling it and consider setting autoCapture and autoContext to false until memory capture and recall are explicitly approved.

Risk: Stored memories may include secrets, credentials, regulated data, or private conversations if users allow unrestricted capture.

Mitigation: Avoid storing sensitive data unless there is a retention, access, and deletion plan appropriate for the deployment.

Risk: Additional indexing, sync, and backup tools can expand where persistent memory data is copied or retained.

Mitigation: Review and limit indexing, sync, backup, autoFlush, and autoConsolidate behavior before deploying the skill in shared or production environments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/nhadaututtheky/skills/neural-memory)
- [Publisher Profile](https://clawhub.ai/user/nhadaututtheky)
- [Skill Homepage](https://github.com/nhadaututtheky/neural-memory)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash, PowerShell, and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent-facing memory workflow guidance and configuration examples; runtime behavior may read from and write to a local persistent memory store.]

## Skill Version(s):

4.62.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
