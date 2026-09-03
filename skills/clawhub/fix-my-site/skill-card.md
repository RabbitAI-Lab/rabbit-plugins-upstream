## Description:

Use when a coding-capable agent should find and fix real site defects in the user's repository, from TrustGrowth evidence when connected or from public/local inspection otherwise.

This skill is ready for commercial/non-commercial use.

## Publisher:

[trustgrowth](https://clawhub.ai/user/trustgrowth)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and site operators use this skill to diagnose real website defects, map them to repository code, implement focused fixes, verify tests or builds, and prepare pull requests. It can work from TrustGrowth evidence when connected or from public, local, and imported observations otherwise.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may edit website code and prepare commits or pull requests that affect outward-facing pages.

Mitigation: Review the diff and pull request before merge or deployment, and require owner confirmation for irreversible or publishing actions.

Risk: The skill may read repository, site, SEO, or analytics data through already configured connectors.

Mitigation: Review connector configuration and access scope before use, and avoid exposing credentials in reports or command output.

Risk: A local test pass does not prove that a deployed defect is closed on the live site.

Mitigation: Keep locally verified, deployed, and audit-verified states separate, and use post-deploy observation or re-audit before claiming closure.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/trustgrowth/skills/fix-my-site)
- [Connectors and categories](references/connectors.md)
- [Reporting contract](references/reporting.md)
- [WHY-NOT-SLOP](https://github.com/techwright-lab/groundcrew-seo/blob/main/WHY-NOT-SLOP.md)
- [ETHICS](https://github.com/techwright-lab/groundcrew-seo/blob/main/ETHICS.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports with code changes, command output, PR or patch references, and connector guidance when justified]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs distinguish locally verified, deployed, and audit-verified states; report-shaped results follow the Groundcrew reporting contract.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
