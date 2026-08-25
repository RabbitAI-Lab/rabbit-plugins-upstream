## Description:

Analyzes fixed-camera child behavior videos to identify repetitive stereotyped behaviors such as spinning, hand flapping, and body rocking, then reports event frequency, duration, trends, and non-diagnostic observations for caregivers and rehabilitation professionals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, rehabilitation professionals, and special-education staff use this skill to analyze uploaded or URL-based child behavior videos and generate structured, non-diagnostic behavior statistics and report links. It can also query cloud-hosted historical reports for the current internally associated user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Child behavior videos, video URLs, identity-linked request fields, and history-report queries may be sent to a cloud service.

Mitigation: Use only with guardian consent, verify the configured service endpoint before use, protect the workspace data directory, and avoid shared machines unless local data is access-controlled.

Risk: The skill stores or reuses identity and token-related state with limited user control.

Mitigation: Run it in a protected environment, restrict access to local configuration and workspace files, and review credential handling before deployment.

Risk: Behavior classifications may be wrong or misleading, especially for common actions that resemble stereotyped behavior or videos with multiple people in view.

Mitigation: Treat outputs as non-diagnostic support, require qualified professional review, and use clear full-body footage that meets the documented video constraints.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-autism-stereotyped-behavior-detect-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API reference](references/api_doc.md)
- [Analysis API reference](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown text containing structured JSON-like analysis results, status messages, history lists, and report export links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save the generated report text to a user-specified output file.]

## Skill Version(s):

1.0.10 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
