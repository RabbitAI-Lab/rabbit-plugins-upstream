## Description:

PatentMax Competitive helps agents prepare paid competitive patent intelligence workflows that generate company technology and patent landscape reports from patent data, supporting sources, and user-provided business context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts, business teams, and IP-adjacent users use this skill to prepare competitive patent intelligence reports for project approval, due diligence, competitor benchmarking, or litigation preparation. It helps an agent gather inputs, run the PatentMax API workflow, monitor long-running jobs, interpret quality status, and produce a decision-oriented report summary or DOCX file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can transmit API keys and sensitive business materials to an external endpoint.

Mitigation: Use the skill only in a trusted shell environment, submit only materials approved for external transfer, and avoid credentials, personal data, privileged legal material, restricted third-party documents, or unnecessary trade secrets.

Risk: The API host can be changed with PATENTMAX_BASE_URL, which may redirect requests and secrets to an untrusted service.

Mitigation: Leave PATENTMAX_BASE_URL unset unless the HTTPS endpoint is fully trusted; prefer a pinned or allowlisted host before production use.

Risk: Generated reports can be incomplete or require review when source coverage or analysis quality is degraded.

Mitigation: Check quality_status and quality_details, disclose limitations in deliverables, and do not present the report as legal advice or a guarantee of patent freedom-to-operate.

Risk: Paid asynchronous tasks can incur unnecessary cost if users run weak inputs or resubmit while a job is still running.

Mitigation: Quote cost and obtain confirmation before execution, prepare detailed materials first, use idempotency keys, and resume with status checks instead of resubmitting.

## Reference(s):

- [Materials guide](references/materials-guide.md)
- [Workflow](references/workflow.md)
- [FAQ](references/faq.md)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)
- [PatentMax console and API](https://api.ip930.com)
- [ClawHub skill page](https://clawhub.ai/ip930/skills/patentmax-competitive)
- [Publisher profile](https://clawhub.ai/user/ip930)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell commands; script responses are JSON and downloadable reports are DOCX files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a PatentMax API key. Jobs are asynchronous, may take tens of minutes, and include quality status that should be disclosed when degraded or requiring review.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
