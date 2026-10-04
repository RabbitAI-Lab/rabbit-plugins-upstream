## Description:

Checks Chinese-language government disclosure text for five expected elements: decision basis, responsible department, deadline, appeal channel, and data source.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (code only); all rights reserved (documentation and theory)

## Use Case:

Developers and disclosure reviewers can use this local checklist to spot missing elements in draft public-sector disclosures before human review. Its result is not a legal or regulatory determination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A checklist result may be mistaken for legal or regulatory approval.

Mitigation: Treat it as a completeness prompt; verify against current official requirements and obtain qualified human review.

Risk: Draft disclosures may contain sensitive information.

Mitigation: Review sensitive text locally before granting the agent access to disclosure files.

Risk: Keyword matches can miss equivalent wording or mark incomplete content as present.

Mitigation: Manually inspect all five disclosure elements and their substantive accuracy before publication.

## Reference(s):

- [Skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/gov-disclosure-check)
- [LGD Hub](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Plain text or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Lists missing elements and a completeness result; exit status indicates pass, missing elements, or usage error.]

## Skill Version(s):

1.0.3 (source: ClawHub release; packaged frontmatter says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
