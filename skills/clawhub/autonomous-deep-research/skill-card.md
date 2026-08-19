## Description:

Autonomous Deep Research helps an agent decompose open-ended research questions, retrieve local or online evidence when supporting tools are available, synthesize findings with confidence signals, identify coverage gaps, and iterate toward a structured report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and external agent users can use this skill to produce iterative research reports for complex, multi-part questions where the agent should show sub-questions, findings, confidence, gaps, and next steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reports and optional learning data are written locally, and learning notes or preferences can persist in learned_patterns.json.

Mitigation: Avoid recording sensitive information in research prompts, notes, preferences, or persisted learning data unless local retention is acceptable.

Risk: When local RAG or web-fetch tools are unavailable, the skill falls back to local heuristic answers that are explicitly lower confidence and may require follow-up retrieval.

Mitigation: Review confidence, needs_web, open_gaps, and next_steps fields before relying on the report, and run additional retrieval for unresolved gaps.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/autonomous-deep-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [JSON research report with Markdown-formatted synthesized answer]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report fields include the original question, sub-questions, findings, synthesized answer, coverage, open gaps, and next steps.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
