## Description:

Screens a PatSnap/Zhihuiya patent query for high-value patent candidates and generates an HTML report, with an optional Word report, using weighted signals for simple-family citations, simple-family size, core inventors, and legal-event history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent analysts and IP teams use this skill to turn a PatSnap/Zhihuiya patent search expression into a traceable high-value patent screening report. The skill is intended for workflows that need ranked patent candidates, scoring rationale, source links, and local trace files for audit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent search queries and patent identifiers may be commercially sensitive and are sent to PatSnap/Zhihuiya APIs.

Mitigation: Use the skill only with data approved for that service and avoid entering confidential searches in unapproved environments.

Risk: Generated reports and trace files may contain confidential patent analysis and source data.

Mitigation: Store outputs in an access-controlled working directory and remove them when they are no longer needed.

Risk: Remote abstract images in Word generation may fetch external content.

Mitigation: Use the Word generator's --noimg option when remote image fetching is not acceptable.

Risk: API credentials could be exposed if copied into skill files, prompts, reports, or shared directories.

Mitigation: Provide PatSnap/Zhihuiya credentials through environment variables or an approved key file, and do not hard-code API keys.

## Reference(s):

- [High-Value Patent Screening Standard](references/screening-standard.md)
- [ClawHub Skill Page](https://clawhub.ai/yuanzhian-patsnap/skills/high-value-patent-package)

## Skill Output:

**Output Type(s):** [markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with generated HTML report files, optional DOCX files, JSON or XLSX trace data, and supporting shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires PatSnap/Zhihuiya API access and stores generated reports and trace files locally.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
