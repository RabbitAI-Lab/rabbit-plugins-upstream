## Description:

Assess how readily a public website can be crawled, parsed, and quoted by answer engines, and produce a prioritized audit report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aureliusclaw](https://clawhub.ai/user/aureliusclaw)

### License/Terms of Use:

MIT

## Use Case:

Website owners, developers, and SEO teams use the audit to review crawler access, snippet permissions, page structure, quotability, and freshness, then prioritize improvements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The auditor can reach private network services despite its public-website-only description.

Mitigation: Run it in an isolated environment that blocks private-network access until destination checks are fixed in both interfaces; review URLs before running.

Risk: Saved reports can replace existing files, and caller-selected destinations affect where they are written.

Mitigation: Review the report destination and use a dedicated output directory.

Risk: Robots.txt enforcement may be incomplete, and the CLI may exceed its stated time limit.

Mitigation: Review target URLs and enforce network and runtime limits in the surrounding environment.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/aureliusclaw/skills/geo-scan)
- [Project homepage listed in skill metadata](https://github.com/AureliusClaw/geo-scan)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Prioritized audit report in Markdown or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scores include evidence lines and describe sampled technical readiness, not actual citation behavior.]

## Skill Version(s):

1.2.3 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
