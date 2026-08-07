## Description:

Add new language translations to customer service response templates and sync the update across Feishu Wiki, GitHub, and local files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Support operations teams, localization maintainers, and developers use this skill to add complete multilingual customer-service template blocks, then publish the update to Feishu Wiki, document it in GitHub, and commit the local file change.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local customer-service template content can be published to external Feishu Wiki and GitHub destinations.

Mitigation: Preview the template file and issue body before running sync or issue scripts, and confirm the target Feishu space, node, GitHub repository, and visibility.

Risk: A misconfigured Feishu API base URL could expose Feishu app credentials outside the intended service.

Mitigation: Keep FEISHU_BASE_URL unset or restricted to the official Feishu API host, and use least-privilege Feishu credentials.

Risk: Broad GitHub or Feishu credentials could permit unintended writes if the wrong target is supplied.

Mitigation: Use least-privilege credentials and verify target IDs before executing the workflow.

## Reference(s):

- [Language Style Guide](artifact/references/language-style-guide.md)
- [Feishu Open API](https://open.feishu.cn/open-apis)
- [ClawHub Skill Page](https://clawhub.ai/terrycarter1985/skills/multilingual-template-sync)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and generated issue or changelog text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local template files, Feishu Wiki documents, and GitHub issues when run with the required credentials and target IDs.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
