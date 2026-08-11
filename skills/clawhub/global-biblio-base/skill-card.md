## Description:

This skill lets an agent search SmartLib academic literature records, retrieve article details, and provide PDF download links for authorized Chinese journals and open-access foreign literature.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j-levee](https://clawhub.ai/user/j-levee)

### License/Terms of Use:

MIT-0

## Use Case:

External users and researchers use this skill to find academic papers, patents, standards, theses, and supporting citations through natural-language requests. Agents can return search results, article details, source links, and available PDF download links while tracking SmartLib quota and download limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can register a SmartLib account and tie usage to a user email.

Mitigation: Ask for explicit user consent before account registration and explain that the email is used for quota and service access.

Risk: The skill can spend quota and present payment flows during a conversation.

Mitigation: Confirm with the user before any paid action and show quota or download impact before executing chargeable operations.

Risk: The skill can fetch PDF files from SmartLib and external open-access channels.

Mitigation: Review download destinations, avoid untrusted notification links, and use this only in environments where file download behavior is acceptable.

Risk: The security evidence recommends review before installation.

Mitigation: Run installation review and security scanning before deployment, and check that stored configuration does not expose secrets to users.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/j-levee/skills/global-biblio-base)
- [SmartLib Account and Billing Reference](artifact/references/account.md)
- [SmartLib Pipeline Optimization Guide](artifact/PIPELINE.md)
- [SmartLib Website](https://www.vipslib.com/)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with search-result lists, article metadata, links, quota notices, and occasional shell-command guidance for downloads.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include PDF download links, source URLs, payment or quota status prompts, and user-facing notices returned by the SmartLib gateway.]

## Skill Version(s):

3.9.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
