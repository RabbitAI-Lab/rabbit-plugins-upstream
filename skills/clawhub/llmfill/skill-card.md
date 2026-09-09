## Description:

AI Word Form Filling auto-fills .docx forms, questionnaires, surveys, templates, DDQs, compliance forms, applications, and checklists using reference documents, a knowledge base, or web search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[viverglow](https://clawhub.ai/user/viverglow)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and document operations teams use this skill to fill Word forms and questionnaires from selected source documents, knowledge bases, or web search. It also supports creating and managing LLMFill knowledge bases used during form completion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected forms and knowledge-base files are sent to LLMFill for remote processing.

Mitigation: Use the skill only for documents you are authorized to upload, and avoid confidential, regulated, internal-only, or personal sensitive data unless approval and handling requirements are satisfied.

Risk: Credential configuration can persist or transmit the wrong environment secret.

Mitigation: Use a dedicated LLMFILL_API_TOKEN value for --token-env and do not point the skill at source-control, cloud, CI, or other unrelated secrets.

Risk: The install command uses a pinned package version but does not by itself prove strict artifact integrity.

Mitigation: Verify the npm installer artifact or registry digest before installation when strict supply-chain assurance is required.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/viverglow/skills/llmfill)
- [LLMFill Service](https://www.llmfill.com)
- [Account and Configuration](references/api-account.md)
- [Document Filling API](references/api-documents.md)
- [Knowledge Base API](references/api-knowledge.md)
- [curl Guide](references/curl-guide.md)
- [Error Codes](references/errors.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files]

**Output Format:** [Markdown guidance with bash and JSON examples; CLI commands can return JSON status and download .docx or .zip result files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Remote API calls may upload selected documents and knowledge-base files to LLMFill. Filled results are downloaded as annotated and clean .docx files, or a .zip for multiple documents.]

## Skill Version(s):

1.0.4 (source: server release metadata and README version entry)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
