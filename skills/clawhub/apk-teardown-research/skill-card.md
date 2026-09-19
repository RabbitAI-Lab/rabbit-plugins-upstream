## Description:

Analyzes Android APKs through the Crawlora API - submit an APK or public URL, inspect static-analysis results, compare versions, build timelines, and compare ownership signals - returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security researchers, and mobile-app analysts use this skill to submit authorized Android APK teardown jobs, inspect manifest and signing signals, compare versions, build timelines, and compare possible ownership indicators.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: APK files, APK URLs, job IDs, and related analysis requests are sent to Crawlora under the user's API key.

Mitigation: Use the skill only when Crawlora's terms and organizational policy allow the package data to be submitted to Crawlora.

Risk: The skill can be misused to inspect packages the user is not authorized to analyze.

Mitigation: Submit only apps, APKs, URLs, and teardown job IDs that the user is authorized to inspect.

Risk: Private or proprietary app packages may contain sensitive implementation details.

Mitigation: Avoid submitting private or proprietary apps unless sharing them with Crawlora is approved.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/apk-teardown-research)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands; Crawlora API responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and authorized APKs, APK URLs, or completed teardown job IDs.]

## Skill Version(s):

1.0.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
