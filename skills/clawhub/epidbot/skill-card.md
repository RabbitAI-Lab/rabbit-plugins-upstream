## Description:

Interact with EpidBot - AI-powered assistant for Brazilian public health data (DATASUS/SINAN)

This skill is ready for commercial/non-commercial use.

## Publisher:

[fccoelho](https://clawhub.ai/user/fccoelho)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and public health teams use EpidBot to query, download, analyze, and visualize public health data and related international, environmental, genomic, and literature sources through the EpidBot API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, uploaded files, query results, and request bodies are transmitted to the third-party EpidBot service.

Mitigation: Confirm the user is comfortable sending the relevant content to EpidBot before invoking endpoints.

Risk: Uploaded files or queries may contain personally identifiable or regulated health information.

Mitigation: Use data minimization, prefer de-identified or aggregated data, and confirm consent, legal basis, or a data-sharing agreement before upload.

Risk: Publishing a dataset can make private data visible to all EpidBot users.

Mitigation: Require explicit confirmation that the dataset contains no sensitive, identifiable, or regulated data before using the publish endpoint.

## Reference(s):

- [EpidBot homepage](https://kwar-ai.com.br/epidbot)
- [ClawHub EpidBot skill page](https://clawhub.ai/fccoelho/skills/epidbot)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires EPIDBOT_API_KEY and EPIDBOT_BASE_URL; API responses may include job status, text, images, reports, datasets, and errors.]

## Skill Version(s):

2.4.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
