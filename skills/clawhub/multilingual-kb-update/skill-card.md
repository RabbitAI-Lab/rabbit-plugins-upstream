## Description:

Adds new language translations to customer service knowledge base templates, syncs updates to Feishu Wiki, and creates a GitHub issue to document the change.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and support-operations teams use this skill to add multilingual customer-service response templates, keep local documentation current, and coordinate the update through Feishu Wiki and GitHub.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can update the wrong Feishu Wiki document or GitHub repository if destination variables are misconfigured.

Mitigation: Confirm FEISHU_WIKI_SPACE_ID, FEISHU_WIKI_NODE_TOKEN, and GITHUB_REPO before running Feishu sync or GitHub issue creation.

Risk: The workflow uses Feishu and GitHub credentials to modify external services.

Mitigation: Use appropriately scoped credentials and skip external sync or issue creation when the required credentials are not configured.

Risk: The workflow can create a local commit containing unintended template changes.

Mitigation: Review the changed KB template and changelog before running the local git commit step.

## Reference(s):

- [Feishu Wiki API Reference](references/feishu-api.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell command and API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include translated template content, Feishu sync steps, GitHub issue text, and local git commit commands; pushing is excluded unless explicitly requested.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
