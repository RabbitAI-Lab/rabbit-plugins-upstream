## Description:

Summarizes long or ultra-long documents by chunking content, summarizing each chunk, and reducing the results into a structured summary with configurable format, tone, and focus.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external users use this skill to summarize documents that exceed a single model context window, including papers, reports, books, chat logs, long web pages, and batches of documents. It supports Map/Reduce and hierarchical reduction workflows for structured summaries with preserved chunk references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The learner component can create a persistent learned_patterns.json usage profile containing notes, preferences, error labels, and recent operation metadata.

Mitigation: Use the summarization workflow without learner commands for confidential documents, or remove/disable note and preference persistence before deployment.

Risk: Recorded notes or preferences may retain sensitive document context if users include confidential details while logging outcomes.

Mitigation: Require explicit user consent for learning logs, minimize recorded content, and provide a deletion process for learned_patterns.json.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with prompt templates, shell commands, and optional JSON chunk files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summaries can be customized by format, length, tone, and focus; chunker output is JSON when used.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
