## Description:

AI-powered pet sleep quality analysis for fixed bed or rest-area camera videos that estimates sleep and wake states, total sleep duration, roll-overs, startle awakenings, and a 0-100 sleep-quality score.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External pet owners, animal hospitals, and pet boarding centers use this skill to analyze pet rest-area video files or URLs for sleep-quality indicators and report links. Results are wellness references and do not provide medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send pet monitoring videos or supplied URLs to a configured cloud service.

Mitigation: Use only trusted publisher releases, check endpoint configuration before use, and avoid sensitive household or clinical footage unless appropriate consent and handling are in place.

Risk: The skill can silently create or reuse an account identity and store service tokens in the workspace database.

Mitigation: Review workspace identity and token handling before deployment, restrict workspace access, and rotate or remove stored tokens when no longer needed.

Risk: The skill can query account-linked history reports.

Mitigation: Run it only in workspaces where account-linked history access is expected and verify that returned report history belongs to the intended user or tenant.

## Reference(s):

- [Pet sleep quality API documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-sleep-quality-analysis-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON text with optional report links and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write analysis output to a user-specified file when invoked with an output path.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
