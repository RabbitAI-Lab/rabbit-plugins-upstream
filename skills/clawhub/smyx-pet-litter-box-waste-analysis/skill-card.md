## Description:

Analyzes cat litter-box images or videos via cloud APIs to report stool characteristics, urine clump size, trends, and health risk alerts without providing disease diagnosis or treatment advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze cat litter-box media for structured observations about feces morphology, urine clump size, report history, and non-diagnostic health risk alerts for smart litter boxes and multi-cat household monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded litter-box media, supplied video URLs, identity data, and report history may be sent to third-party cloud services.

Mitigation: Use only with explicit consent for cloud processing, avoid private household footage unless the data handling is acceptable, and document retention and account-linking expectations before deployment.

Risk: The skill silently creates or reuses local identities and persists tokens in the workspace data directory.

Mitigation: Review local identity and token storage before installation, isolate the workspace for sensitive use, and rotate or remove stored credentials when access is no longer needed.

Risk: History retrieval can expose prior analysis reports associated with the active identity.

Mitigation: Limit history queries to authorized users and confirm the active identity before retrieving report lists.

Risk: The output provides health risk alerts that could be mistaken for veterinary diagnosis.

Mitigation: Present results as observations only and direct users to qualified veterinary care for diagnosis or treatment decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-litter-box-waste-analysis)
- [API Documentation](references/api_doc.md)
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [analysis, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown and JSON-formatted structured analysis text, with optional report links and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save analysis output to a file when an output path is provided.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
