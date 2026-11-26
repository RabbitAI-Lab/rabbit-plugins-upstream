## Description:

Use when the user asks to automate browser tasks, scrape websites, fill forms, capture screenshots, extract structured data from web pages, or build web automation workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[eohmig](https://clawhub.ai/user/eohmig)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to build Playwright-based browser automation for web scraping, structured data extraction, form filling, screenshots, PDF capture, and authenticated browser workflows. It is intended for automation and data workflows, not browser test suites.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes stealth and anti-detection guidance that can help bypass website bot controls.

Mitigation: Use it only for authorized automation, respect site policies and anti-bot controls, and review generated scripts before running them.

Risk: Saved Playwright storage state files may contain active login sessions.

Mitigation: Treat storage state files as secrets, restrict access, avoid committing them, and rotate sessions when exposure is suspected.

Risk: Generated scraping or form automation can unintentionally violate rate limits or collect unintended data.

Mitigation: Set explicit scope, add rate limits and retries, validate selectors and extracted fields, and review outputs before using them downstream.

## Reference(s):

- [Browser Automation Skill](https://clawhub.ai/eohmig/skills/browser-automation)
- [Anti-Detection Patterns](references/anti_detection_patterns.md)
- [Data Extraction Recipes](references/data_extraction_recipes.md)
- [Playwright Browser API Reference](references/playwright_browser_api.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline Python, JSON configuration, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce Playwright scraping and form-automation script skeletons, JSON scraping configuration, and anti-detection risk reports.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
