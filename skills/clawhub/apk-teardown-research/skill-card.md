## Description:

Analyzes Android APKs through the Crawlora API -- submit an APK or public URL, inspect static-analysis results, compare versions, build timelines, and compare ownership signals -- returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, mobile security researchers, and provenance analysts use this skill to submit authorized Android packages for static teardown, inspect permissions, signing, SDK, library, and tech-stack signals, and compare completed jobs across versions or apps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can send the Crawlora API key to an unexpected host if CRAWLORA_API_BASE is set unexpectedly.

Mitigation: Use the skill only in trusted shells or CI jobs, keep Crawlora credentials scoped and rotatable, and unset or pin CRAWLORA_API_BASE before use.

Risk: The helper accepts arbitrary Crawlora paths, which can expand behavior beyond the documented APK teardown endpoints.

Mitigation: Restrict use to the documented /apk-teardown endpoints and review proposed commands before execution.

Risk: Unauthorized APK submission could violate policy, law, or service terms.

Mitigation: Submit only packages or public HTTPS URLs that the user is authorized to inspect.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora API key setup](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [JSON results with concise Markdown guidance and inline shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and authorized APKs or HTTPS package URLs.]

## Skill Version(s):

1.0.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
