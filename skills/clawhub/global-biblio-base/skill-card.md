## Description:

Searches Chinese and global academic literature, retrieves article details, and helps obtain licensed Chinese journal PDFs and open-access papers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j-levee](https://clawhub.ai/user/j-levee)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and other users can search for academic papers, patents, and standards, inspect citations and article details, and obtain available Chinese journal or open-access full texts. Registration requires an email address, and some usage consumes quotas or offers paid plans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release bundles a populated gateway bearer secret.

Mitigation: Rotate or remove the bundled secret before distribution and review the skill before installation.

Risk: Registration and literature retrieval share an email address and search or download requests with SmartLib and related open-access services.

Mitigation: Disclose the destinations and obtain the user's consent before registration or sending requests.

Risk: Search and download calls consume quotas, and the skill can present paid Alipay options.

Mitigation: Confirm downloads and payment actions with the user, and show quota use and pricing before proceeding.

Risk: Broad triggers and subprocess or browser fallbacks may perform actions beyond a simple literature lookup.

Mitigation: Narrow triggers and require confirmation before using subprocess or browser fallbacks.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/j-levee/skills/global-biblio-base)
- [Search and download pipeline](PIPELINE.md)
- [Account and quota guidance](references/account.md)
- [SmartLib website](https://www.vipslib.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, PDF download links]

**Output Format:** [Markdown search results and literature details with links to available full texts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May download available PDFs; retrieval is subject to access rights and usage quotas.]

## Skill Version(s):

3.10.3 (source: release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
