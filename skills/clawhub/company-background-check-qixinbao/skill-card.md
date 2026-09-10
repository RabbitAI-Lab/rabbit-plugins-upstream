## Description:

Generates company background-check reports from a bidding and procurement perspective, covering business profile, customer and supplier relationships, award history, competitors, public-risk checks, and optional contact lookup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

Business users and analysts use this skill to investigate a company from public procurement and bidding data, either as a single-company report or a two-company comparison. It helps summarize business activity, procurement relationships, award strength, competitive overlap, public-risk signals, and data gaps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use an optional automatic registration flow involving a hardware-derived hash and provider account creation.

Mitigation: Review the account flow before consenting, or preconfigure ZLBX_API_KEY to avoid automatic registration.

Risk: The skill stores an API key locally and writes company reports to local files.

Mitigation: Protect the local configuration and report directory, and avoid sharing generated reports unless their contents are intended for recipients.

Risk: Contact lookup and generated HTML reports may contain sensitive business or contact information.

Mitigation: Treat contact results and generated reports as sensitive, and be cautious opening or sharing reports until link escaping and URL validation are fixed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dragonzu/skills/company-background-check-qixinbao)
- [Workflow Guide](artifact/references/workflow.md)
- [API Quick Reference](artifact/references/api-quick.md)
- [Report Template](artifact/references/report-template.md)
- [Auto-Registration Flow](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown report text and optional self-contained HTML report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local report files and requires a ZLBX_API_KEY for data access.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
