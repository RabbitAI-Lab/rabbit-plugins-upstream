## Description:

Identifies weed species and coverage density from field top-view images, and outputs a weed distribution heatmap dataset to support precision weeding decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to send farmland image or video inputs for weed species identification, coverage-density estimation, heatmap-oriented structured results, and historical report lookup. It is intended to support precision weeding decisions, while field treatment choices should be reviewed against agronomic guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Field images, videos, or URLs are sent to lifeemergence.com/open.lifeemergence.com services for analysis and report retrieval.

Mitigation: Use only imagery and URLs that are approved for that external service, and avoid sensitive field imagery or private/internal URLs unless this data flow is acceptable.

Risk: The skill may create or reuse a local workspace identity, register or log in with the backend, and store tokens locally for report access.

Mitigation: Review the local workspace data and token storage behavior before installation, and rotate or remove stored credentials when the skill is no longer needed.

Risk: The security summary notes mismatched video/pet-analysis remnants that may confuse parameter meaning or review expectations.

Mitigation: Confirm the active scene code and command parameters before production use, especially when using category or video-related options.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-farmland-weed-identification-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown and JSON-flavored structured text, with optional report export links and local output files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May output weed species, coverage density, distribution regions, heatmap data, historical report records, and report links.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter says 1.0.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
