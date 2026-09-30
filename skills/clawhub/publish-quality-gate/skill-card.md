## Description:

Checks release materials for potentially sensitive information before publication and guides a TRACE quality self-review after publication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); all rights reserved (documentation and theory)

## Use Case:

Developers and publishers use this skill to check selected release files for possible company, local-machine, personal, and confidential information, then review the published asset against TRACE quality dimensions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scan reports may display snippets of suspected secrets.

Mitigation: Scan only materials intended for review; keep reports private and do not paste them into public logs.

Risk: A clean scan may be mistaken for a complete security or release approval.

Mitigation: Review suspected matches and the release manually before publishing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/publish-quality-gate)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text scan findings and Markdown quality-review guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local scan reports suspected matches by category and returns a pass, findings, or usage-error exit status.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
