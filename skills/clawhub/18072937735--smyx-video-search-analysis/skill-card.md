## Description:

Conducts intelligent video search based on target and semantic descriptions, including conventional target retrieval, natural language description retrieval, and vectorized model matching.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to search video inputs or URLs for described targets, retrieve matching segments, and query prior video-search reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Videos, URLs, and historical report queries are sent to a vendor cloud service and may be associated with an internal identity.

Mitigation: Review data sensitivity and vendor trust before installing; use only approved videos, URLs, and accounts.

Risk: The skill may silently register or reuse an account and store reusable service tokens in a local workspace database.

Mitigation: Install only in workspaces where local token storage is acceptable, and review or rotate stored credentials according to local policy.

Risk: The security guidance warns that returned instructions may steer agents toward payment-skill installation or recharge flows.

Mitigation: Require separate human confirmation before following any payment, recharge, or payment-skill installation instruction returned by the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-video-search-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Video search API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON analysis reports, with optional report links and history tables.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save report output to a file when an output path is supplied.]

## Skill Version(s):

999.999.999 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
