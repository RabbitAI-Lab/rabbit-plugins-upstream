## Description:

Interact with EpidBot - AI-powered assistant for Brazilian public health data (DATASUS/SINAN).

This skill is ready for commercial/non-commercial use.

## Publisher:

[fccoelho](https://clawhub.ai/user/fccoelho)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and public health analysts use this skill to access EpidBot's authenticated API for public health data queries, dataset analysis, visualizations, reports, uploads, and knowledge base search.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, uploaded files, and analysis metadata may be sent to EpidBot, including sensitive public health context.

Mitigation: Use only authorized, properly de-identified data and avoid uploading patient, personal, regulated, or confidential health data unless the user has clearance.

Risk: The skill can publish or delete datasets and plots, including bulk plot deletion.

Mitigation: Require explicit user confirmation before publishing datasets publicly or deleting datasets, plots, or batches of plots.

## Reference(s):

- [EpidBot homepage](https://kwar-ai.com.br/epidbot)
- [ClawHub skill page](https://clawhub.ai/fccoelho/skills/epidbot)
- [EpidBot API base URL](https://api.epidbot.kwar-ai.com.br/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with curl commands, JSON examples, and environment variable configuration.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires EPIDBOT_API_KEY and EPIDBOT_BASE_URL; some workflows can upload, publish, or delete datasets and plots.]

## Skill Version(s):

2.4.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
