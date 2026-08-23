## Description:

Diagnoses and troubleshoots Qdrant deployments by fetching current Qdrant-hosted skill guidance for symptoms such as slow search, memory growth, scaling issues, deployment choices, and client SDK questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qdrant](https://clawhub.ai/user/qdrant)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, operators, and support engineers use this skill to triage Qdrant cluster, collection, search quality, deployment, scaling, monitoring, and SDK questions with current Qdrant-hosted guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Troubleshooting prompts can contain confidential cluster names, incident details, or restricted operational context.

Mitigation: Redact sensitive identifiers and use the skill only when outbound requests to Qdrant documentation services are acceptable.

Risk: Live retrieved guidance may not cover a user's exact Qdrant issue.

Mitigation: State the coverage gap, run a more targeted Qdrant skill search, and avoid filling missing guidance from memory.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qdrant/skills/qdrant-advisor)
- [Qdrant skill search](https://skills.qdrant.tech/search?query=your+query+here)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with ordered diagnostics, documentation links, and occasional inline code or shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches only relevant live Qdrant skill branches and documentation for the user's symptom.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
