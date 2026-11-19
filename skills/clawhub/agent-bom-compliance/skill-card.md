## Description:

Evaluates AI infrastructure scan results against security and regulatory frameworks, checks policy rules, and generates SBOMs and compliance reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security or compliance teams use the skill to assess AI infrastructure against supported frameworks, apply policy-as-code checks, run selected CIS benchmarks, and generate SBOMs and compliance reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SBOM generation writes sbom.json in the documented command and may replace an existing report at the chosen path.

Mitigation: Choose the output location carefully and check whether a report already exists before generating it.

Risk: Optional CIS benchmark checks make authenticated, read-only calls to selected cloud or Snowflake APIs using locally configured credentials.

Mitigation: Run these checks only when explicitly requested, use operator-configured credentials with appropriate read-only access, and do not paste or print secrets.

## Reference(s):

- [Project repository linked in skill metadata](https://github.com/koda-ai-studio/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/koda-ai-studio/agent-bom)

## Skill Output:

**Output Type(s):** [Analysis, Reports, JSON, Files]

**Output Format:** [Compliance and policy findings as text or Markdown; SBOM files in CycloneDX or SPDX JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [SBOM generation writes to a user-selected path; the documented example uses sbom.json.]

## Skill Version(s):

0.115.4 (source: SKILL.md frontmatter; matches server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
