## Description:

Analyzes aquarium video to estimate fish gill opening and closing respiratory rate, flag abnormal breathing patterns such as possible hypoxia, and return structured monitoring guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium owners, public aquarium staff, ornamental fish farm operators, laboratory staff, and agent users use this skill to analyze close-up fish tank videos or URLs, estimate respiratory rate, review abnormal breathing alerts, and query prior cloud reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends fish videos or video URLs to the publisher's cloud service for analysis.

Mitigation: Install and use only when users are comfortable with cloud processing of submitted aquarium media.

Risk: The skill can query cloud history by account identity and persists local user records and service tokens.

Mitigation: Review identity, token storage, and retention behavior before deployment, and prefer a release that documents these behaviors clearly.

Risk: The security verdict is suspicious because cloud services, account identity, history lookup, and local token persistence are used silently.

Mitigation: Review and scan the skill before deployment; require user-visible consent for uploads and history lookup in managed environments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-respiratory-rate-monitor-analysis)
- [API Documentation](references/api_doc.md)
- [smyx_analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files, guidance]

**Output Format:** [Structured analysis report or history list, usually as Markdown text with embedded JSON and report links; optional saved output file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include respiratory-rate estimates, alert levels, suggested non-medication actions, disclaimers, and exported report links.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter says 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
