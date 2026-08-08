## Description:

Analyzes multi-pet images or videos to identify social interactions such as sniffing, chasing, biting, fleeing, hiding, and playing, then returns a structured social-behavior report with durations, frequency, roles, observations, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, pet-care operators, and developers use this skill to analyze multi-pet interaction media and produce behavior observations for homes, boarding centers, daycare, and animal behavior clinics. The results are for visual behavior observation and should not be treated as medical or training advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may upload pet videos or media URLs to a remote service for cloud processing.

Mitigation: Run it only with footage and URLs approved for cloud processing, and confirm user consent before submitting sensitive media.

Risk: The skill may query cloud report history tied to a resolved user identity.

Mitigation: Use approved accounts and review returned history before sharing it outside the intended user context.

Risk: The skill may create or reuse an internal user identity and persist service tokens in the workspace data directory.

Mitigation: Install and run it only in trusted workspaces, review local credential storage, and rotate or remove stored tokens when access is no longer needed.

## Reference(s):

- [Skill API Interface Documentation](references/api_doc.md)
- [Shared Analysis API Interface Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON]

**Output Format:** [Markdown report with structured JSON-style analysis results and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write the returned report to a user-specified output file and may return cloud report history for the resolved user identity.]

## Skill Version(s):

1.0.5 (source: server release metadata; artifact frontmatter says 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
