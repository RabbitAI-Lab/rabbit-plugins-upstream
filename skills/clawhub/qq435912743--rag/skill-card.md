## Description:

RAG indexes local documents, retrieves the top relevant chunks for a question, and produces citation-backed answers in offline extractive mode or optional LLM mode.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and knowledge-work teams use this skill to build local document question-answering workflows, retrieve evidence from private notes, manuals, papers, logs, or knowledge bases, and generate answers with source citations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill indexes user-selected local documents, which may include sensitive or confidential content.

Mitigation: Index only intended folders, keep generated index files in approved storage, and avoid including sensitive paths unless they are required for the task.

Risk: Optional LLM mode can send retrieved excerpts and user questions to an external OpenAI-compatible provider.

Mitigation: Use the default offline extractive mode for sensitive material, and set OPENAI_API_KEY, OPENAI_BASE_URL, and OPENAI_MODEL only when external processing is approved.

Risk: Operational notes in learned_patterns.json may reveal details about usage patterns or failures.

Mitigation: Review or clear learned_patterns.json before sharing the skill or logs outside the intended environment.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown answers with citation markers, JSON retrieval results, and shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can run fully offline by default; optional LLM generation sends retrieved excerpts and questions to the configured OpenAI-compatible provider.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
