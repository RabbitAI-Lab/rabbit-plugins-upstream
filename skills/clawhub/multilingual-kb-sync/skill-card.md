## Description:

Add new language translations to customer service response templates and sync them across Feishu Wiki, GitHub, and local files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Support operations teams and developers use this skill to add reviewed translations to customer-service knowledge-base templates, sync the updated content to Feishu Wiki, and document the change with a GitHub issue.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload the selected markdown file to Feishu Wiki.

Mitigation: Confirm the exact input file, wiki space ID, and parent node before running the sync script; avoid using files that contain secrets or private drafts.

Risk: The skill can create GitHub issues in the target repository.

Mitigation: Review the repository, issue title, labels, and generated body before submitting the issue.

Risk: The workflow may commit and push repository changes.

Mitigation: Inspect the diff and verify the git remote before committing or pushing generated template updates.

## Reference(s):

- [Feishu Wiki API Reference](references/feishu-wiki-api.md)
- [GitHub Issue Template for KB Template Updates](references/github-issue-template.md)
- [Feishu Wiki create node API](https://open.feishu.cn/document/server-docs/docs/wiki-v2/space-node/create)
- [Feishu Docx block create API](https://open.feishu.cn/document/server-docs/docs/docs/docx-v1/document-block/create)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and generated issue body text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call Feishu and GitHub APIs through provided shell scripts when the required credentials and destinations are supplied.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
