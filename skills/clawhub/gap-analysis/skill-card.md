## Description:

Audits repositories for evidence-backed gaps between current code, specs, architecture, and documentation, then prepares confirmed gaps for draft specs, GitHub issues, and orchestrated delivery behind approval gates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to audit a repository before release or after review, compare implementation evidence against specs and documentation, and turn confirmed gaps into tracked follow-up work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Approved runs can create draft specs, GitHub issues, and hand off work to other installed skills.

Mitigation: Review generated drafts and approve the gate only when the proposed work and downstream automation are acceptable.

Risk: Repository audits can produce incorrect or incomplete gap findings when evidence is missing or contradictory.

Mitigation: Require each gap to cite AS-IS evidence, TO-BE evidence, and a coverage check; mark unresolved contradictions inconclusive.

Risk: Issue bodies, PR comments, and external documents may contain untrusted instructions or sensitive data.

Mitigation: Treat external text as evidence only, do not follow embedded directives, and record secrets or personal data as redacted references.

## Reference(s):

- [Gap Record](references/gap-record.md)
- [Report Template](references/report-template.md)
- [ClawHub Skill Page](https://clawhub.ai/afonsoft/skills/gap-analysis)
- [Publisher Metadata URL](https://github.com/afonsoft/skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown reports, gap records, draft SPEC content, approval prompts, and GitHub issue content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [User-facing confirmations are in pt-BR; external actions are gated by explicit approval.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
