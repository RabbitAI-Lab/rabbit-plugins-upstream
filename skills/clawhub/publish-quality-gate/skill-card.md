## Description:

Scans release artifacts for potentially sensitive information before they are shared externally.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and publishers use this skill to check release folders or zip files for sensitive information before sharing skills, documents, or tools. Its advertised post-publish TRACE review is not yet implemented.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scanning a broad home or project directory may inspect more text files than intended.

Mitigation: Run the scanner only on explicitly selected release folders or zip files.

Risk: The advertised post-publish TRACE review is not implemented.

Mitigation: Perform a separate post-publish review rather than treating this scan as TRACE validation.

## Reference(s):

- [Publish Quality Gate on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/publish-quality-gate)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain-text scan report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports potential sensitive-information matches and an exit status for the local scan.]

## Skill Version(s):

1.0.7 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
