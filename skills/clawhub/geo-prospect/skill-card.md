## Description:

CRM-lite for managing GEO agency prospects and clients through lead tracking, audit notes, deal values, and pipeline summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[asale-ai](https://clawhub.ai/user/asale-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External teams and agency operators use this skill to maintain a local GEO sales pipeline, record prospect notes and audits, update deal status, and summarize revenue forecasts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or update persistent local CRM records, notes, audit paths, and deal values.

Mitigation: Use explicit /geo prospect commands, review record changes before relying on them, and back up the JSON CRM file when using it for active sales work.

## Reference(s):

- [ClawHub geo-prospect skill page](https://clawhub.ai/asale-ai/skills/geo-prospect)
- [ClawHub asale-ai publisher profile](https://clawhub.ai/user/asale-ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration]

**Output Format:** [Terminal confirmations, Markdown audit or proposal files, and JSON CRM records.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Persists prospect records, notes, audit paths, and deal values under ~/.geo-prospects/ or a configured SEOGEO_CRM_FILE path.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
