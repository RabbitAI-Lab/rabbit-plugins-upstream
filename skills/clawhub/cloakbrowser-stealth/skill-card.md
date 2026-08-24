## Description:

Provides stealth browser automation with CloakBrowser for fetching public protected pages that block standard automation, excluding login-required pages and interactive CAPTCHA solving.

This skill is ready for commercial/non-commercial use.

## Publisher:

[space-cadet](https://clawhub.ai/user/space-cadet)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to fetch public, non-login web pages when standard fetch tools are blocked by anti-bot defenses, optionally extracting selectors, saving screenshots, or returning text, HTML, or JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stealth and proxy-based scraping can violate site rules or create legal and operational risk when used without authorization.

Mitigation: Use only on sites you are authorized to automate, avoid logged-in or personal pages, and stop when a site presents interactive CAPTCHA, rate limiting, or access restrictions.

Risk: Screenshots and persistent browser profiles may store sensitive local data.

Mitigation: Choose explicit temporary output paths, treat captures and profiles as sensitive files, and delete them after use.

Risk: The skill depends on the external CloakBrowser package for stealth browser behavior.

Mitigation: Review the CloakBrowser package before relying on it and install it only in controlled environments.

## Reference(s):

- [CloakBrowser Configuration Reference](references/config.md)

## Skill Output:

**Output Type(s):** [text, html, json, screenshots, shell commands, configuration, guidance]

**Output Format:** [Plain text, HTML, or JSON from fetch.py; optional PNG screenshot file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Output may be truncated by --max-chars; JSON includes URL, page title, blocked status, extracted text, optional HTML, and optional screenshot path.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
