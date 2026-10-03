## Description:

Provides document release-line selection guidance from a supplied release profile.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Document maintainers and release teams use this skill to formulate a rule for preferring approved versions within a requested major release line. It does not inspect repository records or choose a specific document.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Guidance may be mistaken for a verified selection of an actual document.

Mitigation: Check real document versions and approval states independently before selecting or publishing a release.

## Reference(s):

- [Document Release Guide on ClawHub](https://clawhub.ai/wxt-ai/skills/draft-precedence-guidance-identifier)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [JSON object containing a selection_guidance string]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory only; does not inspect or publish documents.]

## Skill Version(s):

1.1.0 (source: ClawHub release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
