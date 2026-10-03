## Description:

Turns topics and source material into researched WeChat articles with evidence notes, formatted content, visuals, draft assets, and optional cross-platform distribution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[clarezoe](https://clawhub.ai/user/clarezoe)

### License/Terms of Use:

MIT

## Use Case:

Writers and content teams use this skill to research a topic or adapt source material into a sourced WeChat article, prepare publication-ready files, and optionally save a WeChat draft or distribute to other platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Draft delivery can upload, update, replace, or delete content in a WeChat account.

Mitigation: Review the skill before installing on an account with important drafts, start with local rendering, and require explicit confirmation before draft changes or deletion.

Risk: The manual curl-to-bash installer runs downloaded code; account credentials may be exposed if handled carelessly.

Mitigation: Prefer ClawHub installation and keep WeChat credentials in environment configuration.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/clarezoe/skills/research-to-wechat)
- [Project homepage listed in release metadata](https://github.com/Fei2-Labs/skill-genie)
- [Execution contract](artifact/references/execution-contract.md)
- [WeChat compatibility guide](artifact/references/wechat-compat.md)

## Skill Output:

**Output Type(s):** [Markdown, HTML, JSON, Images, Guidance]

**Output Format:** [Article workspace with research notes, formatted Markdown, WeChat-ready HTML, a JSON manifest, cover and inline images, and optional draft delivery]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Draft delivery and cross-platform distribution are optional.]

## Skill Version(s):

0.7.0 (source: server release, skill metadata, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
