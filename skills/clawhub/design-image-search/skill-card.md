## Description:

根据产品照片识别产品并检索视觉相近的外观设计专利。

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

External users can identify a product from a photo and find visually similar design patents for preliminary product research; the results are not legal conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated downloads may expose the API key if sent to an untrusted service.

Mitigation: Use only the trusted HTTPS PatentMax service and a corrected release that restricts authenticated downloads to it.

Risk: Downloaded images may be saved outside the intended output folder.

Mitigation: Prefer a corrected release that confines filenames to the output folder, and verify download paths.

Risk: Product photos are sent to PatentMax; API keys and task records persist locally, and searches may continue after the command exits.

Mitigation: Avoid sending confidential photos, protect local credentials and task records, and check or cancel active searches when appropriate.

## Reference(s):

- [FAQ](references/faq.md)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)

## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [Brief text summary, JSON search results, Word report, and patent-figure image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are ranked by visual similarity; they do not constitute a legal infringement assessment.]

## Skill Version(s):

1.0.2 (source: SKILL.md frontmatter, server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
