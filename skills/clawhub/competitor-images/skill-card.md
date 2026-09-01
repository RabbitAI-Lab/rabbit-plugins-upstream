## Description:

Compares product-page image fields, visible product information, and review feedback for a primary Amazon ASIN and authorized competitor pages to identify image-expression gaps and shooting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and ecommerce operators use this skill to compare their product-page imagery against authorized competitor pages and convert review and listing signals into image-content improvement guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is presented as a narrow competitor image-gap reviewer, but the bundled CLI and instructions expose broader ARI review analysis, monitoring, export, and account-state workflows.

Mitigation: Install only when broad ARI Amazon review and operations-client behavior is intended, and review schedule, watch, competitor, workbench, export, and monitoring actions before allowing them.

Risk: Paid analysis or collection commands can consume ARI credits, and interrupted runs may already have charged or archived a report.

Mitigation: Require the quote step and explicit user confirmation before paid commands, reuse the quoted requestId for operations runs, and check report or run status before retrying after interruption.

Risk: The ARI API key can authorize account actions beyond image comparison.

Mitigation: Use an API key with no more account authority than needed, keep it in the supported local configuration or environment variable, and never include the key in reports or command examples.

Risk: A custom API base URL could redirect authenticated requests away from the official ARI service.

Mitigation: Use the default ARI service URL unless a user intentionally configures a custom environment and also sets the required custom-base confirmation flag.

## Reference(s):

- [Amazon 竞品图片差距 Skill Listing](https://clawhub.ai/funewa/skills/competitor-images)
- [Amazon 竞品图片差距 专属运营工作流](references/operation-workflow.md)
- [ARI CLI 与 API 参考](references/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI command snippets and links to generated ARI reports when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid operations require explicit user confirmation before execution.]

## Skill Version(s):

1.4.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
