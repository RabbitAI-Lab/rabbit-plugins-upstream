## Description:

Provides guidance for choosing an approved document version within a requested major release line.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Document maintainers and developers use a release profile to obtain guidance on which approved version to use within a major release line. The skill does not inspect candidate documents or choose a specific file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Guidance does not verify actual approvals or compare candidate document versions.

Mitigation: Check real candidate approval states and versions before selecting a document.

## Reference(s):

- [Document Release Guide on ClawHub](https://clawhub.ai/wxt-ai/skills/draft-precedence-guidance-identifier)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [JSON object containing a selection_guidance string]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns guidance from the supplied release_profile; does not scan documents or publish changes.]

## Skill Version(s):

1.1.1 (source: frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
