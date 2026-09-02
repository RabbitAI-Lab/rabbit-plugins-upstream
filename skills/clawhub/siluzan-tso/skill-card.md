## Description:

Siluzan TSO routes agents through advertising operations for Google, Bing, Yandex, TikTok, and Meta, including account management, campaign planning, keyword planning, market analysis, website diagnosis, and report generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sigedev01-bit](https://clawhub.ai/user/sigedev01-bit)

### License/Terms of Use:

MIT

## Use Case:

Advertising operators, analysts, and agents use this skill to select the correct Siluzan TSO workflow, run CLI-backed account and campaign tasks, and produce structured advertising reports. It is intended for external commercial workflows that require authenticated access to Siluzan TSO services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer and required CLI can make global system changes.

Mitigation: Install only when the Siluzan CLI is trusted, and prefer a manual or scoped installation when possible.

Risk: The skill supports high-impact account, permission, finance, and campaign write workflows.

Mitigation: Review each write action, require explicit user approval, and use the skill's documented confirmation and audit steps before committing changes.

Risk: Advertising workflows may involve credentials, personal data, lead data, and account identifiers.

Mitigation: Avoid pasting secrets or full personal and lead datasets into chat; use configured authentication mechanisms and share only the minimum data required for the task.

Risk: Generated HTML reports can load remote scripts.

Mitigation: Treat generated reports as network-enabled documents and open them only in contexts where remote script loading is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sigedev01-bit/skills/siluzan-tso)
- [Skill routing entrypoint](artifact/SKILL.md)
- [Documentation directory](artifact/AGENTS.md)
- [Setup and authentication](artifact/references/core/setup.md)
- [Analysis and reporting playbooks](artifact/references/core/playbooks.md)
- [Operations and management workflows](artifact/references/core/workflows.md)
- [Intent routing rules](artifact/references/core/intent-routing.md)
- [Report templates index](artifact/report-templates/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, shell commands, JSON configuration, and generated HTML or XLSX report files depending on the selected workflow.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18+ and siluzan-tso-cli authentication before workflows can access account data or perform write actions.]

## Skill Version(s):

1.1.49 (source: ClawHub release evidence and artifact/_meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
