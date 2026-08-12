## Description:

Analyzes publicly accessible Douyin creator profiles to summarize video themes, engagement structure, representative content, and report outputs in HTML, Markdown, and JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tars1230](https://clawhub.ai/user/tars1230)

### License/Terms of Use:

MIT

## Use Case:

External users, researchers, and content analysts use this skill to inspect public Douyin creators, resolve stable creator identifiers, collect public video metadata, choose transcription samples, and generate auditable creator insight reports. It is not intended for private accounts, favorites synchronization, bypassing access controls, or treating partial collections as complete.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use a logged-in Douyin browser profile while collecting public creator and video metadata.

Mitigation: Use a dedicated browser profile when possible, and share an existing favorites profile only when that is intentional.

Risk: Cloud transcription can send media and API credentials to configurable external ASR services.

Mitigation: Keep API keys in a trusted secret store, avoid untrusted custom ASR endpoints, and use index mode when media should not be downloaded or sent to ASR providers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tars1230/skills/douyin-creator-insight)
- [README](README.md)
- [Apify Douyin Actors reference](references/apify-douyin-actors.md)
- [Creator Resolution Playbook](references/creator-resolution-playbook.md)
- [Data Schema](references/data-schema.md)
- [Categorization Taxonomy](references/categorization-taxonomy.md)
- [Failure Playbook](references/failure-playbook.md)
- [Report Rubric](references/report-rubric.md)
- [Sample report](docs/sample-report.md)
- [Security policy](SECURITY.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [HTML, Markdown, and JSON reports with concise command and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports should distinguish full, partial, degraded, and unavailable collection or transcription states.]

## Skill Version(s):

1.3.6 (source: SKILL.md frontmatter, CHANGELOG, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
