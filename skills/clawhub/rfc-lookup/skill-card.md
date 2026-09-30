## Description:

Looks up IETF RFCs, checks whether they are current, and reads relevant sections for accurate citations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shbernal](https://clawhub.ai/user/shbernal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to find applicable RFCs, check for superseded specifications, and cite the sections that support protocol answers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Routine lookups can fetch public RFCs over the network and cache them locally.

Mitigation: Allow network access and local caching only where appropriate.

Risk: Optional full-text mirror sync downloads about 512 MB into the configured directory.

Mitigation: Run sync only when explicitly requested and after checking storage and destination.

## Reference(s):

- [RFC Editor index](https://www.rfc-editor.org/rfc-index.txt)
- [RFC lookup on ClawHub](https://clawhub.ai/shbernal/skills/rfc-lookup)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with RFC and section citations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Flags superseded RFCs and quotes relevant specification language.]

## Skill Version(s):

0.5.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
