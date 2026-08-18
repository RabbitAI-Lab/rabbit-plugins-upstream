## Description:

Analyzes automotive lamp designs or parts lists for supply-chain make-or-buy decisions and preliminary patent infringement risk, then produces a tabbed HTML report packaged as a zip file.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Automotive lighting, procurement, engineering, and IP teams use this skill to break down lamp parts, compare buy-versus-build options, and prepare preliminary patent risk analysis across invention, utility model, and design patents. It is intended to support early design and sourcing decisions before professional FTO review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates local HTML and zip report files.

Mitigation: Run it in an environment where local report file creation is expected and review generated files before sharing them.

Risk: Patent conclusions are preliminary and depend on configured PatSnap MCP access for patent searches and image retrieval.

Mitigation: Confirm PatSnap account configuration before relying on database-backed results, and treat missing MCP access as limiting the output to an analysis framework.

Risk: IP risk analysis may be incomplete or legally insufficient for production decisions.

Mitigation: Use the output as an early screening aid and obtain formal FTO review from a qualified patent professional before production or commercialization.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/auto-lamp-ip-advisor)
- [PatSnap Open Platform](https://open.zhihuiya.com/)

## Skill Output:

**Output Type(s):** [Text, Code, Shell commands, Files, Guidance]

**Output Format:** [Interactive HTML report packaged as a zip file, with concise supporting guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local report file creation and configured PatSnap MCP access for patent search and patent image retrieval when available.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
