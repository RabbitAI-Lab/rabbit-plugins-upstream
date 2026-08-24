## Description:

Generates an engineering manager 1-on-1 brief from GitHub activity using a deterministic five-tool-call agent pipeline.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jacksync](https://clawhub.ai/user/jacksync)

### License/Terms of Use:

MIT-0

## Use Case:

Engineering managers use this skill to prepare for 1-on-1 meetings by converting a direct report's recent GitHub pull request and review activity into a concise markdown brief. The skill runs local ingestion and scoring, prepares an LLM prompt, and expects the agent to produce and finalize the brief.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires GitHub read access appropriate to the repositories being analyzed.

Mitigation: Use the least-privileged token that supports the intended scope, set GITHUB_ORG to narrow ingestion, and avoid passing tokens with broader access than needed.

Risk: The prepared LLM prompt may be sent to the selected AI provider, and PR insights mode can include bounded raw review or comment excerpts.

Mitigation: Review .pullstar/llm_input_<login>.json before inference and avoid --pr-insights for confidential discussions unless that transfer is acceptable.

Risk: Sparse GitHub activity can produce a low-signal or empty meeting brief.

Mitigation: Use the documented quality gate to check total_score and brief content before presenting the result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jacksync/skills/pullstar-1on1)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Shell commands, Guidance]

**Output Format:** [JSON artifacts with a final Markdown 1-on-1 brief]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes local .pullstar artifacts; opt-in PR insights can include bounded pull request discussion excerpts in the LLM input.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
