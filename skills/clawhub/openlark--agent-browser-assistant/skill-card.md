## Description:

For browser automation tasks, web data scraping, form filling, page screenshots, UI testing, and more.

This skill is ready for commercial/non-commercial use.

## Publisher:

[openlark](https://clawhub.ai/user/openlark)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate a browser for page navigation, element interaction, form filling, data extraction, screenshots, PDF export, and UI testing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser automation may operate on logged-in sites or reuse a user browser profile.

Mitigation: Review the skill before installation and permit profile, credential, or authenticated browsing only when explicitly requested and the destination site is trusted.

Risk: Form filling, file upload, scraping, screenshots, PDFs, and exports can expose account, local file, or page data if used without clear scope.

Mitigation: Limit actions to the requested workflow, confirm sensitive uploads or exports before execution, and avoid authenticated scraping unless the user has approved it.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/openlark/skills/agent-browser-assistant)

## Skill Output:

**Output Type(s):** [API Calls, Files, Text, Guidance]

**Output Format:** [Markdown guidance with browser tool-call examples and browser-generated artifacts such as screenshots, PDFs, and extracted text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce browser actions that interact with authenticated sessions, local uploads, screenshots, PDFs, and scraped page content.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
