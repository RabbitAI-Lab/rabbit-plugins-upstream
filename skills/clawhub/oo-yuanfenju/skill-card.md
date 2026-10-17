## Description:

Connects agents to Yuanfenju for calendar and almanac lookups, astrology charts, and cultural interpretations through OOMOL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents serving Yuanfenju users can retrieve Chinese calendar and almanac information, generate astrology charts, and provide cultural or entertainment interpretations through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup suggests running an unverified remote installation script.

Mitigation: Install the OOMOL CLI through a trusted, verifiable method rather than letting an agent execute the remote script.

Risk: Yuanfenju inputs pass through OOMOL, and some actions can consume paid credits or change data.

Mitigation: Share only inputs you are comfortable sending through OOMOL and confirm paid, quota-consuming, write, or destructive actions before execution.

## Reference(s):

- [Yuanfenju homepage](https://yuanfenju.com/)
- [OOMOL CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI installation guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text or Markdown summaries of Yuanfenju results, including calendar dates, charts, and interpretations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Natal chart SVG may be included when provided by Yuanfenju.]

## Skill Version(s):

1.0.0 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
