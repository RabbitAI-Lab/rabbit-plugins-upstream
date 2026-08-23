## Description:

Detects possible employee phone use in workplace images or video, produces structured monitoring reports, and can list prior reports from the configured cloud service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Enterprise operators and workplace management teams use this skill to analyze authorized office monitoring media for possible phone-use behavior, summarize counts and duration, and review cloud-hosted report history. It is intended as an internal management aid and should not be used as the sole basis for employment decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Employee surveillance media or media URLs may be sent to the configured cloud service.

Mitigation: Use only with clear authorization to process workplace monitoring media, disclose monitoring scope and purpose, and avoid sending media that is outside the approved use case.

Risk: Cloud report history is queried by an internally resolved identity.

Mitigation: Limit report access to authorized operators and verify that identity-to-report association matches the intended organization or workspace.

Risk: The skill can silently provision identities and store authentication tokens in local workspace data.

Mitigation: Run in a controlled workspace, review local token storage practices before installation, and rotate or remove stored credentials when access is no longer needed.

Risk: Phone-use detection outputs may affect employee privacy and workplace decisions.

Mitigation: Treat reports as decision-support only, review results with human oversight, and follow applicable labor, privacy, and notice requirements.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-phone-usage-monitoring-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Workplace phone usage monitoring API documentation](artifact/references/api_doc.md)
- [Common analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON text, with optional local output files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return structured analysis, report links, warnings, suggestions, or a Markdown table of cloud report history.]

## Skill Version(s):

1.0.9 (source: ClawHub release metadata; artifact frontmatter says 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
