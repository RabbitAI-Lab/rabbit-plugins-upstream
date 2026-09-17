## Description:

Automates Juejin article publishing and provides semi-automated Zhihu publishing, including login, draft creation, metadata validation, cover generation, column attachment, publishing, and status checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thneoly](https://clawhub.ai/user/thneoly)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and content creators use this skill to configure and run command-line publishing workflows for Markdown articles on Juejin and Zhihu.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing-session cookies are stored locally and should be treated as account credentials.

Mitigation: Use a dedicated writing directory, do not commit .juejin.env or .cdp-profile, and restrict access to saved credential files.

Risk: A Zhihu clipboard fallback path has a command-injection risk when handling untrusted or unusual filenames.

Mitigation: Avoid running that fallback on untrusted files and prefer a patched version that avoids PowerShell command interpolation.

Risk: The skill relies on reverse-engineered platform behavior that may change.

Mitigation: Run preview and status checks before publication and review platform responses when publishing fails.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/thneoly/skills/juejin-publisher-pro)
- [Juejin category IDs](references/category_ids.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with command invocations and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local credential/profile files and generated cover or preview artifacts during publishing workflows.]

## Skill Version(s):

1.0.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
