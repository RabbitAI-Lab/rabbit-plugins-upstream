## Description:

Compare Chrome extensions using Crawlora's live store listings and stored adoption, publisher, permission, and privacy history for shortlists, market comparisons, or investigating observed changes, while treating store disclosures as insufficient to establish runtime safety.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and security reviewers use this skill to compare Chrome Web Store extensions against feature requirements, adoption and maintenance evidence, permission and privacy disclosures, and observed change history. It supports shortlists, market comparisons, and investigation triage without treating store metadata as proof of runtime behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled API helper can send the Crawlora API key to a configurable API base.

Mitigation: Use the skill only where CRAWLORA_API_BASE is controlled, avoid overriding it unless necessary, and review the helper before installation.

Risk: Chrome Web Store permissions, privacy statements, ratings, and user counts can be misleading if treated as proof of runtime safety or usage.

Mitigation: Label these values as store observations or developer disclosures, compare dated evidence windows, and avoid concluding runtime safety without independent review.

## Reference(s):

- [chrome-extension-research endpoint reference](reference/endpoints.md)
- [Chrome extension permission definitions](https://developer.chrome.com/docs/extensions/develop/concepts/declare-permissions)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/chrome-extension-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured comparison guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dated store observations, current listing fields, permissions, privacy disclosures, review themes, and missing evidence.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
