## Description:

Grow runs the Groundcrew SEO growth loop for a site, covering survey, fix, verify, and report phases as a full cycle or as a named phase.

This skill is ready for commercial/non-commercial use.

## Publisher:

[trustgrowth](https://clawhub.ai/user/trustgrowth)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site owners, and SEO operators use Grow to coordinate a Groundcrew cycle that surveys SEO and AI-visibility issues, applies safe local fixes, verifies changes, and produces an evidence-backed report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured analytics or search connectors and connected audit triggers may access or act on site data.

Mitigation: Install only for the expected Groundcrew SEO workflow and review proposed actions before allowing connected API audit triggers.

Risk: Local branch-based fixes may change site code and could become outward-facing if accepted downstream.

Mitigation: Review proposed fixes before merging, publishing, or allowing irreversible changes such as redirects, robots policy updates, or content changes.

Risk: The referenced provider-selection guide is absent from this artifact.

Mitigation: Confirm available connectors and data-source choices before relying on connector-dependent survey or verification results.

## Reference(s):

- [Reporting contract](references/reporting.md)
- [Connectors and categories](references/connectors.md)
- [Groundcrew WHY-NOT-SLOP doctrine](https://github.com/techwright-lab/groundcrew-seo/blob/main/WHY-NOT-SLOP.md)
- [Groundcrew ETHICS doctrine](https://github.com/techwright-lab/groundcrew-seo/blob/main/ETHICS.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown reports and prioritized findings with inline commands, verification evidence, and code-change guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stops at gates before outward-facing or irreversible changes; unverified fixes remain labeled as unverified.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
