## Description:

MacCheck checks a Mac locally by collecting read-only system facts, opening a guided hardware-check page, and generating downloadable inspection reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iluoyao](https://clawhub.ai/user/iluoyao)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to perform local Mac health, acceptance, resale, post-repair, or troubleshooting checks. It is intended as an inspection aid and does not replace Apple official diagnostics or guarantees.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated output can include sensitive device details such as full serial number, OS/build, storage, MDM/ADE, FileVault, SIP, Activation Lock, network, and peripheral status.

Mitigation: Protect the output directory and downloaded reports, and review device identifiers before sharing reports publicly.

Risk: Camera, microphone, USB, and file-picker prompts expose local hardware capabilities while hardware tests are running.

Mitigation: Approve these prompts only when actively performing the corresponding test.

Risk: Local inspection cannot fully prove server-side Activation Lock, ADE, original configuration, repair history, or future ownership status.

Mitigation: Treat results as reference information and use Apple or other trusted checks before relying on the report for transactions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iluoyao/skills/mac-check-skill)
- [Server-resolved source repository](https://github.com/iluoyao/mac-check-skill)
- [Architecture](references/architecture.md)
- [Privacy and Security](references/privacy.md)
- [Detection Catalog](references/detection-catalog.md)
- [Report Specification](references/report-spec.md)
- [Rule Specification](references/rule-spec.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, files, guidance]

**Output Format:** [Plain-language agent messages, zsh command execution, a local HTML session, and downloadable Markdown/PDF/PNG reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally by default; generated reports may include device identifiers and security status.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter reports 2.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
