## Description: <br>
Audits and scores Amazon listings across CDQ content quality, A9 indexability, COSMO intent coverage, Alexa discoverability, and compliance, producing a diagnostic health report with issues and prioritized fix guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[buluslan](https://clawhub.ai/user/buluslan) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External sellers, ecommerce operators, and developers use this skill to diagnose Amazon listing quality, compliance, indexability, intent coverage, and AI-shopping discoverability from pasted listing data, URLs, or ASIN-normalized JSON. It identifies issues and prioritized fixes without rewriting listing copy. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can shape user-facing responses with mandatory promotional attribution. <br>
Mitigation: Review generated reports before sharing and remove or adapt promotional attribution when it conflicts with publication, marketplace, or organizational policy. <br>
Risk: The skill requests command and file access for local diagnostics. <br>
Mitigation: Run it in a scoped workspace with only the listing data needed for the audit, and review proposed file or command actions before execution. <br>
Risk: The optional SellerSprite fetch path may send ASIN requests to a third-party service using the user's API secret. <br>
Mitigation: Prefer pasted or exported listing data for local-only analysis; use SellerSprite only when third-party API use and secret handling are intentional. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/buluslan/skills/listing-doctor) <br>
- [README_EN.md](artifact/README_EN.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [report-template.md](artifact/assets/report-template.md) <br>
- [output-template.json](artifact/assets/output-template.json) <br>
- [cosmo_ontology.json](artifact/references/cosmo_ontology.json) <br>
- [new-rules-2026.md](artifact/references/new-rules-2026.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Structured JSON and Markdown diagnostic report] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces scores, critical issues, data-coverage notes, and prioritized fix guidance; it does not rewrite listing copy.] <br>

## Skill Version(s): <br>
0.3.0 (source: ClawHub release, target metadata, and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
