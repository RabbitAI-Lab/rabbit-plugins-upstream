## Description:

Evaluates AI scan results against security and compliance frameworks, checks policies, and helps generate compliance reports and SBOMs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams use this skill to assess AI scan results against compliance frameworks, enforce policies, and produce SBOMs. Optional cloud benchmark checks require explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an external package from an untrusted source could expose the user's environment.

Mitigation: Verify that you trust the agent-bom package and source before installation.

Risk: Optional cloud benchmark checks contact provider APIs using configured credentials.

Mitigation: Run these checks only when needed, with explicitly approved least-privilege read-only credentials.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/msaad00/skills/agent-bom-compliance)
- [Project homepage (skill metadata; not verified import provenance)](https://github.com/msaad00/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)
- [Project OpenSSF Scorecard (skill metadata)](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Compliance reports and guidance in text or Markdown; CycloneDX or SPDX SBOMs in JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.108.1 (source: SKILL.md frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
