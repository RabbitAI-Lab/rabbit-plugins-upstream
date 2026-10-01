## Description:

Build a concise support case comment and follow-up tags from a supplied support digest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Support operations staff use a prepared case digest to draft a concise case comment and follow-up tags for a handoff. The operation also saves a local JSON case artifact; it does not post to an external support service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The operation reads the provided support digest and writes a local support case artifact that may contain case information.

Mitigation: Provide only appropriate case data, choose a controlled writable output directory, and review the local artifact before sharing it.

## Reference(s):

- [Support Case Workbench on ClawHub](https://clawhub.ai/wxt-ai/skills/support-followup-marker-workbench)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns a case comment with an ID, case ID, and tags; writes a local support_cases JSON artifact in the chosen output directory.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
