## Description:

Audits articles, reports, drafts, or series by extracting verifiable claims, tracing them to primary or reliable secondary sources, classifying source support, and producing structured audit outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Editors, analysts, researchers, and publication teams use this skill to audit high-risk factual claims, verify source support, compare versions across platforms, and produce audit reports with optional regression gold-set CSVs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may inspect local files, research databases, internal logs, or other source material while auditing claims.

Mitigation: Confirm which local files, databases, and logs the agent may access before running an audit.

Risk: Generated audit CSVs may contain article claims, source URLs, or internal evidence summaries.

Mitigation: Review generated CSV gold sets and audit artifacts before sharing or storing them outside the intended workspace.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/claim-to-source-auditor-skill)

## Skill Output:

**Output Type(s):** [Text, Markdown, CSV, Guidance]

**Output Format:** [Structured Markdown audit report with CSV claim tables and optional regression gold-set CSV.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes claim verdicts, severity levels, source register entries, cross-platform comparison notes, and regression check results.]

## Skill Version(s):

1.0.6 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
