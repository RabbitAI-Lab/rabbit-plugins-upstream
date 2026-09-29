## Description:

Guides open-source security reviewers through private vulnerability reporting, layered code and dependency review, and repository-specific security practices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qikairo7](https://clawhub.ai/user/qikairo7)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and open-source maintainers use this skill to route vulnerability reports to private channels, plan security checks, and respond to dependency alerts. It does not provide penetration testing or legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive vulnerability details could be exposed in public issues, pull requests, commits, or test names.

Mitigation: Use the repository's security policy or private vulnerability reporting; keep payloads and reproduction details out of public channels.

Risk: The review workflow may be incomplete if companion tools or private reporting channels are unavailable.

Mitigation: Confirm the referenced review tool, routing workflow, and private reporting process exist before relying on the guidance for live vulnerabilities.

## Reference(s):

- [oss-security on ClawHub](https://clawhub.ai/qikairo7/skills/oss-security)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown guidance with optional commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-language instructions; security report details should stay out of public posts and commit messages.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
