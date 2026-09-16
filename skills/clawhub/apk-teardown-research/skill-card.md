## Description:

Analyzes Android APKs through the Crawlora API - submit an APK or public URL, inspect static-analysis results, compare versions, build timelines, and compare ownership signals - returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security researchers, and mobile-app analysts use this skill to submit authorized Android packages to Crawlora for static analysis, then inspect permissions, signing, SDK, library, release-history, and ownership signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: APK files, APK URLs, job identifiers, and the Crawlora API key are sent to a third-party API.

Mitigation: Use the skill only when Crawlora processing is acceptable, protect CRAWLORA_API_KEY, and avoid submitting proprietary or sensitive packages unless that handling has been approved.

Risk: The skill can be misused to analyze packages without permission.

Mitigation: Submit only apps and URLs that the user is authorized to inspect, matching the artifact's authorization guidance.

Risk: Results come from static teardown analysis and may not capture runtime behavior.

Mitigation: Treat returned permissions, signing, SDK, library, and ownership signals as static-analysis evidence and corroborate high-impact conclusions before acting on them.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/apk-teardown-research)
- [Crawlora](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [JSON results with concise Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and authorized APK files or public HTTPS APK URLs.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
