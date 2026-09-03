## Description:

Detects and mitigates hallucinations in agent outputs by prompting self-checks, claim verification, confidence calibration, and correction logging.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tooled-app](https://clawhub.ai/user/tooled-app)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to add runtime hallucination checks, grounding steps, and recovery practices to LLM-based agent workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill instructs agents to keep local hallucination correction and metrics notes, which could retain sensitive claims or context.

Mitigation: Use a no-log convention for private or regulated work, redact sensitive claims, or periodically delete the memory logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tooled-app/skills/anti-hallucination-skill)
- [Publisher profile](https://clawhub.ai/user/tooled-app)
- [OpenClaw](https://openclaw.ai)
- [Ollama](https://ollama.com)

## Skill Output:

**Output Type(s):** [guidance, markdown, configuration]

**Output Format:** [Markdown protocol guidance with checklists and integration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May ask the agent to maintain local hallucination correction and metrics logs.]

## Skill Version(s):

1.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
