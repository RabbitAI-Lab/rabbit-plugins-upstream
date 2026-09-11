## Description:

Recognizes cat and dog vocalizations with pet voiceprint AI and returns likely emotions, behavioral intentions, structured analysis results, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to analyze pet audio or video files, identify likely cat or dog vocal emotions and intentions, and retrieve account-linked historical analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet media and report metadata are sent to a remote service for analysis.

Mitigation: Use only when the user accepts remote processing of the supplied pet media and related report metadata.

Risk: Historical report queries are account-linked.

Mitigation: Confirm that report-list requests are expected for the active user context before running history retrieval.

Risk: The skill may retain local identity and token data.

Mitigation: Run in an appropriate workspace, protect local storage, and clear local credentials when the environment is shared or decommissioned.

Risk: The packaged configuration includes HTTP development endpoints that conflict with HTTPS-only privacy expectations.

Mitigation: Configure HTTPS-only production endpoints before normal use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-vocal-emotion-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Pet vocal emotion API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration]

**Output Format:** [Markdown or JSON text containing structured analysis results, history listings, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write the returned analysis text to a user-provided output file path.]

## Skill Version(s):

1.0.13 (source: server release metadata; artifact SKILL.md frontmatter declares 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
