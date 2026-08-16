## Description:

Turns a fact-checked and compliance-approved final Markdown draft into local multi-channel publishing assets for WeChat, LinkedIn, standalone HTML, and archive records without auto-publishing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Content, communications, and publishing teams use this skill to package an already reviewed Markdown draft into platform-ready publishing files and a local archive ledger. It is intended for generation and validation of publishing assets, not fact-checking, rewriting, or automatic external publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or overwrite publishing-package files in a selected output directory.

Mitigation: Review the target output directory before execution and keep generated assets isolated from source drafts or unrelated working files.

Risk: Publishing assets could be generated from a draft that has not passed the required review gate.

Mitigation: Require an approved final-check file or an explicit reviewed marker before packaging, and stop when the gate is missing or fails.

Risk: A user-confirmed external write to Notion or a publishing platform could publish or record unintended content.

Mitigation: Use dry-run generation by default, list targets before any external action, require user confirmation, and verify writes after completion.

## Reference(s):

- [Content Publishing Suite on ClawHub](https://clawhub.ai/haiyangchenbj/skills/content-publishing-suite-skill)
- [Channel Output Contracts](references/channel-contracts.md)
- [WeChat 135 Inline Style Guide](references/wechat-style.md)
- [WeChat Snippet Template](templates/wechat-snippet.html)
- [LinkedIn Post Template](templates/linkedin-post.md)
- [Standalone HTML Template](templates/standalone.html)
- [Archive Record Template](templates/archive-record.json)
- [Publishing Package Builder](scripts/build_publish_package.py)
- [Publishing Output Validator](scripts/validate_publish_output.py)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with generated HTML, Markdown, JSON, and shell command artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local publishing-package files and validation reports; default posture is dry-run with confirmation required before any external write.]

## Skill Version(s):

1.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
