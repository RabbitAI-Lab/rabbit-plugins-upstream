## Description:

Drive Chromium from standard Playwright APIs with a real-device fingerprint applied inside the browser kernel, one persistent isolated profile per identity, and a per-profile proxy whose exit IP sets timezone and WebRTC - JavaScript/TypeScript (npm 'anti-detect-browser') or Python (PyPI 'antibrow').

This skill is ready for commercial/non-commercial use.

## Publisher:

[antibrow](https://clawhub.ai/user/antibrow)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and automation teams use this skill to integrate antibrow's Playwright-compatible browser into authorized QA, ad verification, public-data scraping, regional testing, and account-management workflows that need persistent isolated profiles and coherent browser fingerprints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dual-use browser automation could be misapplied to unauthorized access, account abuse, fake engagement, or platform enforcement evasion.

Mitigation: Use only for authorized browser automation, QA, ad verification, public-data collection, or accounts the operator owns or administers; follow site terms, robots.txt, rate limits, and applicable law.

Risk: API keys and proxy URLs are sensitive operational secrets.

Mitigation: Keep API keys and proxy URLs in environment-managed secrets, never commit them to source or configuration, and rotate scoped keys if exposure is suspected.

Risk: Persistent browser profile directories can contain live sessions, cookies, and account state.

Mitigation: Treat profile storage as credential material, restrict access to it, and exclude it from shared backups, container images, logs, and support archives.

Risk: The browser kernel is a closed-source binary downloaded and cached by the SDK.

Mitigation: Pin SDK package versions, warm and verify the browser cache during image builds where possible, and review the closed-source kernel requirement before deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/antibrow/skills/anti-detect-browser)
- [AntiBrow Documentation](https://antibrow.com/docs)
- [AntiBrow REST API](https://antibrow.com/api/v1/)
- [REST API and Docker deployment](references/rest-api-and-docker.md)
- [CreepJS Browser Fingerprint Test](https://abrahamjuliot.github.io/creepjs/)
- [LiarJS Consistency Tests](https://liarjs.dev)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JavaScript, TypeScript, Python, Dockerfile, JSON, YAML, and shell snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include environment-variable names, package/version pins, and authorized-use constraints; does not include secrets.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
