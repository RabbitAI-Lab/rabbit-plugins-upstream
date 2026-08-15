## Description:

Generates a Chinese-language light due-diligence report for a company before cooperation, contracting, or credit decisions using bidding records and public risk checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

Business users and analysts use this skill to review a company before cooperation, contracting, supplier selection, or credit terms. It produces single-company due-diligence reports or two-company comparisons from Zhiliaobiaoxun bidding data plus cited public risk information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated reports and platform links may include signed login-bypass parameters.

Mitigation: Treat reports and links as sensitive; share them only with intended recipients and avoid reposting signed links in public channels.

Risk: The skill may create a trial vendor account after consent and send a hashed device identifier for trial deduplication.

Mitigation: Proceed with auto-registration only after explicit user consent, or configure ZLBX_API_KEY manually to skip registration.

Risk: The skill can persist an API key under ~/.zlbx/config.json.

Mitigation: Protect the local configuration file and rotate or revoke the key if the file or machine is exposed.

Risk: Due-diligence reports are saved under ~/zlbx-company-intel-files/ and may contain sensitive business analysis.

Mitigation: Store generated report files in an access-controlled location and delete them when they are no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dragonzu/skills/enterprise-due-diligence-shuidixinyong)
- [Publisher Profile](https://clawhub.ai/user/dragonzu)
- [API Quick Reference](artifact/references/api-quick.md)
- [Due-Diligence Workflow](artifact/references/workflow.md)
- [Report Template](artifact/references/report-template.md)
- [Auto-Registration Flow](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown report, optional self-contained HTML report, and user-facing guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or consent-gated trial registration; reports may include signed platform links.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
