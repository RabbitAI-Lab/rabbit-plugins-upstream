## Description:

Talaria is an opt-in Playwright stealth wrapper for authorized browser automation on websites the user owns or is explicitly permitted to test.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gadielkalleb](https://clawhub.ai/user/gadielkalleb)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation engineers use Talaria when an authorized Playwright workflow needs a stealth browser wrapper because a documented basic bot-detection signal blocks ordinary automation. It should not be used for generic browsing, broad scraping, CAPTCHA solving, or bypassing access controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stealth browser automation can be misused against sites where the user lacks authorization.

Mitigation: Use only for websites the user owns or is explicitly authorized to test, and confirm authorization when the target or permission is unclear.

Risk: Proxy credentials and target data can leak through logs, URLs, screenshots, HTML captures, or generated files.

Mitigation: Do not enumerate environment variables or print proxy credentials, and write screenshots or HTML only to explicit user-provided paths.

Risk: The wrapper may still encounter CAPTCHAs, paywalls, login walls, or advanced bot-detection challenges.

Mitigation: Do not add solvers or claim success when a challenge remains; report the challenge and stop or request an authorized alternative.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gadielkalleb/skills/talaria)
- [Publisher profile](https://clawhub.ai/user/gadielkalleb)
- [Talaria homepage](https://github.com/gadielkalleb/talaria)
- [Bright Data Playwright CAPTCHA article credited by the skill](https://brightdata.com.br/blog/dados-do-site/bypass-captchas-with-playwright)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration, JSON, files]

**Output Format:** [Markdown guidance with JavaScript examples, shell commands, and optional CLI JSON, screenshot, and HTML outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The wrapper can emit page metadata as JSON and write screenshots or HTML only to user-specified output paths.]

## Skill Version(s):

0.1.3 (source: server release metadata; artifact frontmatter and package.json list 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
