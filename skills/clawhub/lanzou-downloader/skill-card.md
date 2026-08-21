## Description:

Downloads Lanzou Cloud single-file and folder shares locally, including password handling, anti-crawling retry logic, pagination, selective downloads, and interrupted-download retries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwqww1](https://clawhub.ai/user/wwqww1)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and end users use this skill when they need an agent to download supported Lanzou Cloud links or password-protected folder shares to a chosen local output path.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HTTPS certificate validation is disabled, which can expose downloads or submitted passwords to network interception.

Mitigation: Use a version that keeps normal HTTPS certificate validation enabled before sending passwords or downloading files.

Risk: The implementation does not enforce the stated Lanzou/CDN domain limits.

Mitigation: Require a strict allowlist for Lanzou and approved CDN domains before making requests, following redirects, sending passwords, or writing downloaded files.

Risk: Untrusted Lanzou links may cause the agent to fetch unexpected content and write files to the selected output path.

Mitigation: Install only after review, use trusted Lanzou links, and confirm the intended output path before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wwqww1/skills/lanzou-downloader)

## Skill Output:

**Output Type(s):** [Shell commands, Files, Guidance]

**Output Format:** [Markdown with inline bash commands and downloaded files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes downloaded content to the requested output path and supports optional password and --select filters.]

## Skill Version(s):

0.0.5 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
