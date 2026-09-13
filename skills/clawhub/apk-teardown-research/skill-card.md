## Description:

Analyzes Android APKs through the Crawlora API by submitting an APK or public URL, inspecting static-analysis results, comparing versions, building timelines, and comparing ownership signals as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, mobile security researchers, and app provenance analysts use this skill to inspect Android package metadata, permissions, signing, SDK, library, technology-stack, timeline, diff, and ownership signals for apps they are authorized to analyze.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted APKs, public file URLs, job IDs, and the Crawlora API key are sent to a third-party service.

Mitigation: Use the skill only for apps you are authorized to analyze, avoid unreleased or secret-bearing APKs unless organizational policy permits Crawlora handling, and protect the API key as a credential.

Risk: Analysis of unauthorized packages can create legal or policy exposure.

Mitigation: Confirm authorization before submitting packages or URLs, and keep analysis within the documented APK teardown, diff, timeline, and ownership-comparison workflows.

## Reference(s):

- [apk-teardown-research endpoint reference](reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/apk-teardown-research)
- [Crawlora](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and authorized APKs or public HTTPS APK URLs.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
