## Description:

Analyzes videos of fish and other aquatic pets for visible health concerns and returns a structured health report with care guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium keepers use this skill to review fish and other aquatic pets for visible health concerns and get a structured report with care suggestions. Results are for reference and do not replace advice from a qualified aquatic veterinarian.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Videos are uploaded to LifeEmergence for analysis, and server retention and account isolation are unverified.

Mitigation: Use non-sensitive footage and a separate workspace; verify retention and account isolation before sending sensitive material.

Risk: Remote account creation and credential storage are not clearly explained.

Mitigation: Use a separate workspace and verify how accounts and credentials are handled before use.

Risk: The security review reports that export-only mode may not be honored.

Mitigation: Use a corrected release that honors export-only mode.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-aquarium-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API interface notes](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis report, JSON, Markdown, Care guidance]

**Output Format:** [Structured health report with observations, risk indicators, care suggestions, and report links; JSON or Markdown text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Informational health assessment; does not replace professional veterinary diagnosis.]

## Skill Version(s):

1.0.18 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
