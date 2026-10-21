## Description:

Counts livestock or poultry in barn and passage images or videos and presents inventory estimates and historical reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Farm operators and their agents use camera footage to estimate livestock counts and review past inventory reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Camera footage and media URLs may be sensitive and are sent to configured lifeemergence.com services.

Mitigation: Obtain permission to share footage and URLs with the service; avoid uploading sensitive material until its handling is approved.

Risk: The skill silently creates or reuses a local cloud identity and stores service tokens locally.

Mitigation: Review identity and token storage before installation, and restrict access to stored credentials, especially on shared systems.

Risk: Hidden identity selection may affect which historical reports are accessible.

Mitigation: Fix or tightly control identity selection and verify report access boundaries in shared or multi-user environments.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-livestock-counting-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Text]

**Output Format:** [Text or Markdown report with estimated counts, confidence, and report links; historical reports as a Markdown table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may be saved to a local file.]

## Skill Version(s):

1.0.12 (source: server-resolved release; artifact frontmatter lists 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
