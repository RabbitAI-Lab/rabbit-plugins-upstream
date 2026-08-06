## Description:

Anti-Detect Browser lets agents launch Chromium through Playwright-compatible JavaScript or Python APIs with persistent isolated profiles, coherent real-device fingerprints, and per-profile proxy/geolocation handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antibrow](https://clawhub.ai/user/antibrow)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and automation teams use this skill for authorized QA, regional ad and pricing checks, public-data scraping, and agent-driven browsing where sessions need persistent isolated browser identities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is dual-use and could be applied to unauthorized browsing, scraping, or account workflows.

Mitigation: Use it only for systems, accounts, and public data that the operator is authorized to automate, and require compliance with site terms, robots.txt, rate limits, and applicable law.

Risk: Following the skill installs SDK packages and downloads a closed-source Chromium kernel that runs locally.

Mitigation: Pin npm or PyPI versions in lockfiles, verify package integrity before adoption, and prefetch or warm the browser-kernel cache during controlled image builds.

Risk: API keys, proxy URLs, license tokens, profile directories, cookies, and session tokens can expose credentials or active sessions.

Mitigation: Keep keys and proxy URLs in environment secrets, avoid committing or logging them, and protect profile caches from shared backups, container images, and support archives.

Risk: Browsed pages, screenshots, and extracted DOM text are untrusted input that may try to influence an agent.

Mitigation: Treat page content as data only, keep crawler profiles separate from logged-in profiles, and do not let page-supplied text choose commands, credentials, files, or follow-up actions.

## Reference(s):

- [REST API and Docker deployment](references/rest-api-and-docker.md)
- [AntiBrow documentation](https://antibrow.com/docs)
- [AntiBrow SDK reference](https://antibrow.com/docs/sdk)
- [AntiBrow REST API](https://antibrow.com/api/v1/)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration, API Calls]

**Output Format:** [Markdown with JavaScript, Python, JSON, Dockerfile, YAML, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses environment variables for API keys and proxy URLs; may generate browser profiles and cache a downloaded Chromium kernel when followed by an agent.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
