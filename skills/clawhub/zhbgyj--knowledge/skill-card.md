## Description:

Integrates a local knowledge base for document search, knowledge ingestion, and switching between local retrieval and AnythingLLM conversation modes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhbgyj](https://clawhub.ai/user/zhbgyj)

### License/Terms of Use:


## Use Case:

External users and developers use this skill to query a local knowledge base, inspect document counts and previews, and switch between local retrieval and AnythingLLM-backed conversation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on an external local openclaw_integration helper that is not included in the artifact.

Mitigation: Review and trust the local integration implementation before relying on the skill in an agent workflow.

Risk: Knowledge-base queries and document previews may expose local document content through agent responses or the localhost integration service.

Mitigation: Use the skill only with expected local knowledge-base content and avoid indexing sensitive documents unless that exposure is acceptable.

Risk: The release quality evidence reports a low score and quarantine decision that requires moderation review before listing.

Mitigation: Complete moderation and quality review before publishing or deploying the release broadly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhbgyj/skills/knowledge)
- [Publisher profile](https://clawhub.ai/user/zhbgyj)

## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [Plain text or Markdown-style responses returned to the agent]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include retrieval answers, mode status, document counts, document previews, and help text.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
