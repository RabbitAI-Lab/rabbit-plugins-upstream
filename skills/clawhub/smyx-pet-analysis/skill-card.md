## Description:

Analyzes cat, dog, bird, or other pet videos and media URLs through remote health-analysis APIs to produce a structured Pet Safety Guardian health report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to submit pet media for remote health analysis, receive structured findings, recommendations, and report links, or retrieve prior report lists associated with the current identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet media and identity-linked data are sent to remote services for analysis.

Mitigation: Install only when the publisher and configured API environment are trusted, and confirm users are comfortable with remote media processing.

Risk: The skill can silently create or reuse a default identity and store authentication tokens in a local workspace database.

Mitigation: Run it in an isolated workspace with restricted local data access, and clear stored identity or token records when access is no longer needed.

Risk: History-related phrases may trigger cloud report lookups tied to the current identity.

Mitigation: Confirm user intent before history queries and avoid using the skill from shared accounts or shared workspaces.

Risk: The health report is informational and may be incomplete or incorrect.

Mitigation: Treat results as health references only and consult a qualified veterinarian for diagnosis or treatment decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)
- [SMYX Analysis API Error Codes](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with structured JSON text and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save the result to a user-specified output file.]

## Skill Version(s):

999.999.1006 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
