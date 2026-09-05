## Description:

Audit public webpages and websites for crawlability, indexing signals, metadata, canonical URLs, headings, structured data, and evidence-backed SEO fixes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

SEO practitioners, developers, and site owners use this skill to run bounded technical and on-page SEO audits of public HTTP(S) sites and produce prioritized, evidence-backed reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Target URLs and optional keywords are sent to Dataify services during audits.

Mitigation: Use the skill for public SEO audits only and avoid confidential/internal targets or sensitive keyword lists.

Risk: Raw fetched HTML is saved in the output directory.

Mitigation: Remove the evidence/output folder when no longer needed and avoid auditing pages that may contain sensitive content.

Risk: The skill uses a Dataify API token.

Mitigation: Configure the token through the environment and do not paste, print, or include it in reports.

## Reference(s):

- [Audit Framework](references/audit-framework.md)
- [SEO Checks](references/checks.md)
- [Output Contract](references/output-contract.md)
- [Site-Type Playbooks](references/site-type-playbooks.md)
- [Dataify Documentation](https://doc.dataify.com)
- [Dataify Support](https://www.dataify.com/)
- [ClawHub Skill Page](https://clawhub.ai/dataify-server/skills/dataify-seo-audit)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with JSON reports and local evidence files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces report.json, raw evidence, and Markdown findings with code, layer, priority, impact, evidence, and fix fields.]

## Skill Version(s):

1.1.0 (source: frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
