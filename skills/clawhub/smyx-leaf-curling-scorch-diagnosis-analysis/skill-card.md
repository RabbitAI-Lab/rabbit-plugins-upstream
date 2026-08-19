## Description:

Uses plant leaf images or video, with optional soil-moisture context, to identify curling direction and leaf-margin scorch patterns and return likely causes such as drought stress, disease, pesticide damage, or fertilizer burn.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External agricultural teams and developers use this skill to analyze crop, greenhouse, or orchard leaf imagery and generate structured diagnosis guidance for curling and scorch symptoms. It supports API-backed analysis, report export links, and cloud history lookup for prior diagnostic reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-supplied media or URL references may be uploaded to remote lifeemergence.com/open.lifeemergence.com services.

Mitigation: Use only with files and URLs that are approved for remote processing, and review network endpoints before installation.

Risk: The skill can create or reuse an internal cloud identity and store authentication tokens in local SQLite storage.

Mitigation: Run it in an environment with appropriate local storage controls, and clear stored tokens when access is no longer needed.

Risk: Cloud report history can be fetched automatically.

Mitigation: Use history lookup only where cloud report access is expected, and review returned reports before sharing them.

## Reference(s):

- [Leaf Curling and Margin Scorch API Documentation](references/api_doc.md)
- [SMYX Analysis API Error Codes](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown and structured JSON diagnostic reports, with optional saved text output and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload local media or URL references to remote analysis services and may query cloud report history.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
