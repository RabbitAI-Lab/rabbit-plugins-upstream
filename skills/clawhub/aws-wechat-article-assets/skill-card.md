## Description:

Helps agents manage a local WeChat article business asset library, ingest product images, and import trusted .aws preset bundles into .aws-article resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aiworkskills](https://clawhub.ai/user/aiworkskills)

### License/Terms of Use:

MIT-0

## Use Case:

Content operators, brand teams, and design support users use this skill to keep reusable product copy, product images, and article preset packages organized for WeChat article workflows. Agents can save business descriptions, copy uploaded product images with matching Markdown descriptions, and run shell commands to import .aws ZIP presets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The preset importer can automatically change repository credentials and can print secret values in configuration diffs.

Mitigation: Review the skill before installing, run imports with --dry-run first, check aws.env and .aws-article/config.yaml for real secrets before importing, and rotate any credentials that may have been printed or copied into backups.

Risk: Importing untrusted .aws bundles can modify local article assets, preset files, and configuration in the repository.

Mitigation: Import only trusted .aws bundles, keep the default aiworkskills.cn HTTPS host restriction, avoid --allow-any-host in normal use, and review resulting file changes before reuse.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aiworkskills/skills/aws-wechat-article-assets)
- [Publisher profile](https://clawhub.ai/user/aiworkskills)
- [aiworkskills.cn preset source domain](https://aiworkskills.cn)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated local files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update .aws-article product assets, image description Markdown files, preset directories, config.yaml, downloads, temporary extraction files, and aws.env entries when the user runs the provided commands.]

## Skill Version(s):

1.0.25 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
