## Description:

global-biblio-base helps an agent search academic literature through the SmartLib Open Platform API, retrieve article details, and provide full-text PDF links for authorized Chinese journals and open-access foreign literature when available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j-levee](https://clawhub.ai/user/j-levee)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent for literature searches, article details, citation-support discovery, and PDF download links where the configured SmartLib service can lawfully provide them. It is intended for academic discovery workflows covering journals, patents, conference papers, theses, and standards metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for a user email, creates or uses a SmartLib account, and stores that email in local configuration.

Mitigation: Use a purpose-appropriate email address, review local configuration handling, and avoid installing in shared environments unless account ownership and data retention expectations are acceptable.

Risk: Search, detail, and download actions consume monthly quota through the SmartLib gateway and may trigger paid recharge prompts.

Mitigation: Confirm the expected number of API calls before large searches or downloads, monitor quota notices, and require user confirmation before any paid plan or download purchase.

Risk: The artifact includes a gateway credential used to call the SmartLib gateway.

Mitigation: Review credential exposure and rotation practices before deployment, and do not echo secrets in chat, logs, generated pages, or shared configuration.

Risk: Foreign paywalled literature cannot be downloaded through the skill and open-access retrieval may vary by publisher or route.

Mitigation: Treat PDF availability as best-effort, preserve source links and metadata, and use institutional or publisher-approved access paths for closed-access articles.

Risk: The release evidence security verdict is suspicious despite no specific riskFindings entries.

Mitigation: Perform human review of the account registration, quota, payment, and gateway behavior before approving installation in managed or production contexts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/j-levee/skills/global-biblio-base)
- [SmartLib account and billing reference](references/account.md)
- [SmartLib pipeline guide](PIPELINE.md)
- [SmartLib website](https://www.vipslib.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with literature result lists, article details, quota notices, payment guidance, and download commands or links when available.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include quota status, SmartLib account prompts, source links, and PDF retrieval guidance; closed-access foreign literature is limited to metadata or lawful open-access routes.]

## Skill Version(s):

3.9.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
