## Description:

Helps agents recommend Volcengine Config compliance baselines, summarize current compliance findings across built-in and custom rules, and draft custom Rego audit rules when built-in coverage is insufficient.

This skill is ready for commercial/non-commercial use.

## Publisher:

[volc-sdk-team](https://clawhub.ai/user/volc-sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud engineers, and compliance operators use this skill to inspect Volcengine accounts for compliance posture, choose relevant built-in conformance-pack templates, and prepare custom audit rules for gaps. It separates reporting from remediation and requires confirmation before cloud-side writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use a Volcengine CLI session or VOLCENGINE_* credentials to inspect account compliance data.

Mitigation: Use least-privilege Config permissions, run it only in trusted environments, and avoid exposing generated reports.

Risk: Confirmed write operations can create conformance packs, enable the recorder, or register custom audit rules.

Mitigation: Start with recommend or overview, review dry-run output, and allow --confirm only when the intended account change is clear.

Risk: Compliance outputs may include account IDs, resource IDs, regions, and annotations.

Mitigation: Store reports in controlled locations and redact identifiers before sharing outside the intended audience.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/volc-sdk-team/skills/volcengine-compliance)
- [Compliance recommendation guide](references/recommend.md)
- [Compliance overview guide](references/overview.md)
- [Conformance pack deployment guide](references/apply.md)
- [Authentication and prerequisites](references/auth.md)
- [Custom rule authoring guide](references/writing-config-rules.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, plus generated Markdown, CSV, and JSON compliance report files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only recommendation and overview commands are available; conformance-pack deployment, recorder enablement, and custom rule registration require explicit confirmation.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
