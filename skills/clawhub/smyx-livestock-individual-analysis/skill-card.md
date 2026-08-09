## Description:

Identifies individual livestock (pigs, cattle, sheep) by facial or body-pattern features and outputs a stable individual ID with confidence for precision farm management and tracking. | 通过面部/体纹识别畜禽个体，实现精准管理追踪。

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Farm operators, livestock technology teams, and agents use this skill to identify pigs, cattle, and sheep from face or body-pattern images or videos, then return identity IDs, confidence, matched feature areas, report links, or history tables for tracking workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Livestock media, media URLs, identity tokens, and identifiers are processed by lifeemergence.com services and may be linked to locally stored workspace data.

Mitigation: Use a dedicated workspace, begin with non-sensitive test media, and install only when this cloud processing and local token storage are acceptable.

Risk: The skill silently creates or reuses an account identity and retrieves identity-linked history.

Mitigation: Review account and history behavior before deployment, avoid shared workspaces for sensitive use, and clear workspace data files during uninstall or rotation.

Risk: Identification results are reference outputs for livestock identity association and may be wrong or incomplete under poor capture conditions.

Mitigation: Use clear face or body-pattern media that meets the documented capture requirements and verify important records against farm systems or human review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-livestock-individual-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Livestock individual analysis API documentation](references/api_doc.md)
- [Common analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON text returned by Python command-line scripts, with optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Analysis output may include individual IDs, confidence, matched feature regions, report links, and Markdown tables for historical reports.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter lists 1.0.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
