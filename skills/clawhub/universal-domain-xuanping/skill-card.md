## Description:

Assesses any domain through read-only external checks across eight risk dimensions and adds a deterministic I-Ching Xuan-Ping reading for entertainment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[openmsg88](https://clawhub.ai/user/openmsg88)

### License/Terms of Use:

MIT-0

## Use Case:

Site owners, developers, and security reviewers can use this skill to gather an initial evidence-based risk overview for a domain and identify findings that need manual verification. Its hexagram reading is entertainment only and is separate from the assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review rates the skill suspicious because domain checks may reach internal network services.

Mitigation: Avoid installation until the redirect and internal-network access risk is addressed. If using it, consider whether the environment can reach internal services.

Risk: Partial scan coverage and incomplete evidence may lead to reassuring conclusions.

Mitigation: Treat reports cautiously and manually verify findings; unresolved evidence should remain pending rather than support a complete conclusion.

## Reference(s):

- [Risk Grading Criteria](artifact/references/RISK_GRADING.md)
- [ClawHub release page](https://clawhub.ai/openmsg88/skills/universal-domain-xuanping)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Structured Markdown risk report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Eight risk dimensions with red, amber, green, or pending states; registration-age and data-credibility notes; a separate entertainment-only hexagram.]

## Skill Version(s):

1.1.0 (source: server-resolved release, SKILL.md frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
