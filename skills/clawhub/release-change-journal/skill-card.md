## Description:

Analyze release patches and publish the release notes journal.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release managers use this skill to turn supplied repository patch data into a concise release change set and, when requested, publish a release-note entry.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing can generate or record a release-note entry before the release change set has been approved.

Mitigation: Use the publish stage only when a release note should be generated or recorded, and preview the supplied change set when the release process requires approval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/release-change-journal)

## Skill Output:

**Output Type(s):** [text, markdown, structured data]

**Output Format:** [Structured objects with concise text fields and Markdown release-note content.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The summarize stage returns release_change_set with change_id, files, components, additions, and deletions; the publish stage returns release_note_receipt with change_id, title, markdown, and file_count.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
