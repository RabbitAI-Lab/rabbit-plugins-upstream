## Description:

Analyzes reptile enclosure feeding videos to detect prey attacks, swallowing, feeding refusal, and post-feeding regurgitation, then returns structured alerts and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External reptile keepers, vivarium operators, and developers use this skill to analyze feeding-window videos or URLs for attack, swallow, regurgitation, refusal, alert-level, and historical-report signals. It supports behavior records and non-diagnostic care guidance rather than veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reptile enclosure videos or URLs are sent to the configured analysis service.

Mitigation: Review the configured endpoints and data-handling expectations before use, and submit only footage that is appropriate to transmit to that service.

Risk: The skill can create or reuse a local identity and persist service tokens in a workspace SQLite database.

Mitigation: Run the skill in a dedicated workspace, treat workspace data files as secrets, and rotate tokens if those files are exposed.

Risk: Published configuration includes environment-specific service URLs, including dev or private HTTP endpoints.

Mitigation: Audit configuration before installation and use only intended HTTPS production endpoints for normal releases.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-reptile-feeding-refusal-vomiting-analysis)
- [API interface documentation](artifact/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown text with structured JSON-style analysis fields, report links, and optional saved output files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write an output file when --output is supplied; analysis and history queries use configured API endpoints.]

## Skill Version(s):

1.0.9 (source: server release evidence; artifact frontmatter says 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
