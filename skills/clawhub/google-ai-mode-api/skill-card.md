## Description:

Fetches Google's AI Mode answer for a query as structured JSON, including AI-generated text blocks, cited references, and shopping results for commercial queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve Google's AI Mode response for a query, including cited references for grounding and optional shopping results for commercial queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries are sent to Scavio's API and may consume paid credits.

Mitigation: Keep users aware of per-request cost, check credit usage, and avoid sending sensitive private information in queries.

Risk: AI Mode answers can be incomplete or misleading if used without checking source material.

Mitigation: Surface returned references with the answer and verify important claims against those references before relying on them.

Risk: The required SCAVIO_API_KEY could be exposed if stored in source control or shared logs.

Mitigation: Load the key from an environment variable or secret store and keep it out of committed files and transcripts.

## Reference(s):

- [Scavio Google AI Mode documentation](https://scavio.dev/docs/google-ai-mode?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-ai-mode-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-ai-mode-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/google-ai-mode-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON, Python, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns API-derived AI answer text, cited references, shopping results when present, response timing, credit usage, cache status, and setup or retry guidance.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
