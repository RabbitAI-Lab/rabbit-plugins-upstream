## Description:

Detects black rot, melting, and stretching in succulent images or videos, returning structured state, severity, confidence, and report-link results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users such as home succulent growers, greenhouse operators, and flower shop staff use this skill to analyze succulent media for black rot, melting, and stretching signals. Agents can also query cloud report history and present structured findings, confidence, severity, and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images, videos, and report-history requests may be sent to external services.

Mitigation: Review configured service endpoints before installation and use only media approved for external processing.

Risk: The skill silently creates or reuses a local identity and stores token material in local data storage.

Mitigation: Treat the local data directory and SQLite database as sensitive, restrict access, and clear stored credentials when needed.

Risk: Bundled configuration may select development 192.168.1.234 endpoints.

Mitigation: Check or replace bundled configuration with approved production endpoints before running the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-succulent-special-state-detection-analysis)
- [API interface documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown and JSON text, with report links when returned by the API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud history records and report export URLs.]

## Skill Version(s):

1.0.10 (source: server release evidence; artifact frontmatter states 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
