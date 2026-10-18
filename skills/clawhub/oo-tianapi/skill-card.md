## Description:

Access TianAPI data and search results through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Users and developers with an OOMOL-connected TianAPI account can retrieve Chinese calendar information, trending topics, account usage, and entertainment-oriented interpretations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running an unverified CLI installer could execute untrusted code.

Mitigation: Use the official OOMOL installation guide and verify the installer source before running setup commands.

Risk: TianAPI requests can consume API quota or account credits.

Mitigation: Check available quota and expected call count before repeated or multi-request queries.

Risk: Horoscopes and compatibility interpretations may be mistaken for factual assessments.

Mitigation: Present these results as entertainment, not medical or other professional advice.

## Reference(s):

- [TianAPI skill on ClawHub](https://clawhub.ai/oomol/skills/oo-tianapi)
- [TianAPI homepage](https://www.tianapi.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI installation guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Plain text or Markdown summaries of TianAPI query results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the selected endpoint and enabled TianAPI access.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
