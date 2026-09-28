## Description:

快速生成电影级商品广告视频：基于物理渲染的光影场景、细腻画面质感，适合品牌宣传与高端商品展示。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to prepare and run Qinghu/QHKIT commands for cinematic product advertising videos, TVC-style brand promos, estimates, task polling, and delivery of generated video URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade Node/npm tooling, qhkit, registry settings, or PATH entries while preparing the environment.

Mitigation: Preinstall qhkit where possible and require user confirmation before install, upgrade, PATH, or registry mirror changes.

Risk: The skill can upload referenced product images or media and requires a QHKIT API token.

Mitigation: Confirm the user is comfortable sharing the selected media with Qinghu/QHKIT and use token handling that avoids exposing secrets in conversation or logs.

Risk: Video generation may consume account credits and submitted tasks may run for an extended time.

Mitigation: Run estimates when supported, confirm credit-sensitive actions before generation, preserve task IDs, and poll status at reasonable intervals.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-ad-film)
- [QHKIT npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include QHKIT task IDs, status summaries, credit estimates or charges, and generated video URLs returned by the CLI.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
