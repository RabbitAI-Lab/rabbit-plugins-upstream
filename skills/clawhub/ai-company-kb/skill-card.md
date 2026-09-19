## Description:

AI Company shared knowledge base interface for unified management of operations records, strategy documents, audit logs, cross-agent knowledge sharing, state sync, and IMA real-time sync for zero-handoff protocol.

This skill is ready for commercial/non-commercial use.

## Publisher:

[johnsmithfan](https://clawhub.ai/user/johnsmithfan)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and agent operators use this skill to save, read, and synchronize shared company knowledge such as audit logs, shared state, strategy documents, financial records, compliance reports, and task handoff records across AI Company agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent audit logs and shared-state files may retain sensitive company records, prompts, credentials, personal data, legal material, or financial records.

Mitigation: Use only in governed workspaces with explicit retention, access-control, redaction, and deletion policies for knowledge-base and audit data.

Risk: IMA or cross-agent synchronization may network-sync sensitive records beyond the local workspace without clear opt-in in the artifact.

Mitigation: Enable synchronization only after confirming intended destinations, authorization, and data handling controls; keep local-only operation for sensitive records when those controls are absent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/johnsmithfan/skills/ai-company-kb)
- [ClawHub homepage metadata](https://clawhub.com/skills/ai-company-kb)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, JSON, Configuration]

**Output Format:** [Markdown and structured knowledge-base records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write persistent audit logs, shared-state files, and handoff documents, with optional API synchronization.]

## Skill Version(s):

1.0.1-en2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
