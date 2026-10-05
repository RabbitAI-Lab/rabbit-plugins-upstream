## Description:

Summarize repository changes for a release and create a local release-note entry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release coordinators use supplied repository patches to prepare structured change summaries and write local Markdown release notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A release-note file may be created in an unintended shared directory.

Mitigation: Choose a dedicated writable output directory and check its contents before running the downstream stage.

## Reference(s):

- [Release Change Journal on ClawHub](https://clawhub.ai/wxt-ai/skills/release-change-journal)

## Skill Output:

**Output Type(s):** [JSON, Markdown]

**Output Format:** [JSON change set and receipt; local Markdown release note]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The downstream stage writes a release note beneath the caller-selected output directory; it does not publish to an external service.]

## Skill Version(s):

3.0.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
