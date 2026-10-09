## Description:

根据视频号作品的 object_id 生成可分享的作品短链。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

视频号创作者和运营人员可提供作品 object_id，获取便于分享的视频号作品短链。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions may install or update local Node.js and qhkit, or change the user's PATH.

Mitigation: Review and explicitly approve setup changes; prefer a trusted, preinstalled qhkit.

Risk: Configuring qhkit can persist a Qinghu API token locally.

Mitigation: Prefer short-lived or environment-injected credentials where possible, and avoid sharing the token in responses.

Risk: Generating links uses a paid Qinghu tool with an unspecified base price.

Mitigation: Check the current estimate and obtain user approval before paid calls; report actual credits charged.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-shipinhao-share-link)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Share URL in a concise response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports credits charged for paid calls; failures are reported instead of a link.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
