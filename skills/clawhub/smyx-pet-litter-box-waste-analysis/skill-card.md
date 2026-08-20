## Description:

Analyzes cat litter box images or videos by calling remote APIs to identify feces morphology and urine clump characteristics, returning structured observation reports and health risk alerts without disease diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze cat litter box media for waste characteristics, urine clump size, and trend-oriented health observations. The output is intended for monitoring and risk awareness, not veterinary diagnosis or treatment guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded household pet media or supplied media URLs may be sent to remote services.

Mitigation: Confirm the intended backend, consent model, and data-retention policy before use.

Risk: The skill can automatically create or reuse an identity and store authentication tokens in a local workspace database.

Mitigation: Run in a controlled workspace, restrict local database access, and clear stored credentials when no longer needed.

Risk: Default development configuration references private HTTP 192.168.1.234 endpoints.

Mitigation: Review configuration before installation and set trusted production endpoints before processing media.

Risk: History queries retrieve prior analysis reports from cloud APIs.

Mitigation: Verify the user or account scope before listing reports and avoid exposing internal identity values.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-litter-box-waste-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, guidance]

**Output Format:** [Markdown report or JSON-formatted structured analysis and history list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include remote report links; does not diagnose disease.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter says 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
