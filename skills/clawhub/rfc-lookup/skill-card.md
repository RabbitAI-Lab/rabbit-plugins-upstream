## Description:

Looks up IETF RFCs, finds relevant sections, and checks whether specifications have been superseded before citing them.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shbernal](https://clawhub.ai/user/shbernal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to find and read relevant RFC sections, check for superseded specifications, and cite protocol requirements accurately.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Normal lookups may contact the RFC Editor and cache RFC text locally.

Mitigation: Confirm network access and local caching are appropriate before use.

Risk: Sync downloads roughly 512 MB and manages files in the chosen mirror directory.

Mitigation: Run sync only when a full-text mirror is needed, and verify any custom mirror path first.

## Reference(s):

- [RFC lookup on ClawHub](https://clawhub.ai/shbernal/skills/rfc-lookup)
- [RFC Editor index](https://www.rfc-editor.org/rfc-index.txt)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown with RFC section citations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Identifies superseded RFCs and cites relevant sections.]

## Skill Version(s):

0.5.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
