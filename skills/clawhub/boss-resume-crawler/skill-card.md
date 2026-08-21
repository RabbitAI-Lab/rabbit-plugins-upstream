## Description:

从 Boss 直聘批量爬取职位详情（含 security_id、职位描述），支持 PUA 薪资解码和增量去重。

This skill is ready for commercial/non-commercial use.

## Publisher:

[iichaner](https://clawhub.ai/user/iichaner)

### License/Terms of Use:

MIT

## Use Case:

Developers and recruiting-data operators use this skill to guide an agent through collecting Boss直聘 job-listing details from an authenticated browser session, decoding salary obfuscation, deduplicating records, and exporting crawl results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automates logged-in scraping with anti-detection browser control, which may create terms-of-service, account, legal, and privacy risk.

Mitigation: Use the skill only when authorized to collect the target Boss直聘 data and after accepting the applicable platform and legal risks.

Risk: Uses a debugging browser session that may expose unrelated browsing context if reused.

Mitigation: Use a dedicated temporary browser profile, keep unrelated tabs closed, and shut down the debugging browser after use.

Risk: Writes durable CSV and error-log files that may contain scraped job details and security identifiers.

Mitigation: Choose a controlled output directory and delete CSV and error-log files when they are no longer needed.

## Reference(s):

- [Server-resolved source repository](https://github.com/iichaner/boss-resume-crawler)
- [ClawHub skill page](https://clawhub.ai/iichaner/skills/boss-resume-crawler)
- [Data field specification](references/data-spec.md)
- [Standard operating procedure](references/sop.md)
- [Error handling](references/error-handling.md)
- [CloakBrowser project](https://github.com/nickspaargaren/cloakbrowser)
- [OpenClaw project](https://github.com/openclaw/openclaw)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration, files]

**Output Format:** [Markdown instructions with inline shell and Python snippets; the bundled scripts produce CSV result files and error logs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python 3, curl, websocket-client, and a user-controlled headed CloakBrowser/CDP session.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
