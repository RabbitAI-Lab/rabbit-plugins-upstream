## Description:

Measure how often a company is named in answer-engine research, which competitors appear instead, and which sites shape the answers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchd](https://clawhub.ai/user/searchd)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and growth teams use this skill to run evidence-preserving AEO visibility audits for a company domain, producing neutral buyer-question research and a deterministic HTML report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill queries public web sources about the target company and saves audit evidence locally.

Mitigation: Run it only in an appropriate workspace and review locally saved evidence before distributing reports.

Risk: Reports include SearchD attribution and may include a commercial SearchD call to action when enabled or in scope.

Mitigation: Review the rendered report before sharing and include the call to action only under the documented scope rule.

Risk: A report can be misleading if the underlying audit JSON was edited by an untrusted party.

Mitigation: Validate audit JSON against the bundled schema and check run-level evidence before relying on conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/searchd/skills/searchd-aeo-audit)
- [Homepage](https://github.com/runbear-io/searchd-skills)
- [SearchD AEO audit methodology](references/methodology.md)
- [Audit data contract](references/data-contract.md)
- [Audit JSON schema](schemas/audit.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON evidence files and self-contained HTML report output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a local audit workspace containing audit.json, context.md, questions.json, run records, and report.html.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
