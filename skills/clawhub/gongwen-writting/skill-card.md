## Description:

Assists Chinese office and administrative users with drafting common state-owned enterprise and government-style official documents by retrieving document-structure guidance from an external Gongwen API and turning it into a complete draft.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yourtsao](https://clawhub.ai/user/yourtsao)

### License/Terms of Use:

MIT-0

## Use Case:

Office staff, secretaries, and administrative writers use this skill to draft Chinese official documents such as requests, reports, notices, meeting minutes, speeches, plans, summaries, and research reports. The skill asks for the user's email, retrieves a writing skeleton from gongwen-api.xyz, and instructs the agent to mark missing names, dates, document numbers, figures, or amounts as pending instead of inventing them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the user's email address and writing request to gongwen-api.xyz.

Mitigation: Use it only when the user accepts that external service handling the request, and avoid including sensitive internal details unless disclosure is appropriate.

Risk: Quota exhaustion can trigger paid WeChat payment flows.

Mitigation: Stop drafting when quota errors occur, present payment prompts clearly, and continue only after the user explicitly chooses a paid option.

Risk: The skill stores a USER_TOKEN in config.json after registration.

Mitigation: Do not display the full token in conversation or logs, and treat the local config file as sensitive user-specific configuration.

Risk: Generated official documents may require facts the user did not provide.

Mitigation: Mark missing numbers, document identifiers, names, dates, amounts, and similar facts with pending placeholders instead of fabricating them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yourtsao/skills/gongwen-writting)
- [Yourtsao publisher profile](https://clawhub.ai/user/yourtsao)
- [Gongwen API gateway](https://gongwen-api.xyz)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Chinese official-document drafts in text or Markdown, with inline command and API-call guidance for registration, quota consumption, and payment flows.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses an external API for document skeleton retrieval; missing facts are expected to be marked with pending placeholders.]

## Skill Version(s):

1.0.0 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
