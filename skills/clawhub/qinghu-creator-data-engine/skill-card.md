## Description:

This skill helps agents submit Douyin, Xiaohongshu, or Bilibili creator homepage links to Qinghu's qhkit workflow and retrieve standardized Excel exports with creator account and playback metrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to monitor competitor or partner creator accounts by submitting supported platform profile URLs, estimating paid workflow cost, and retrieving generated XLSX data tables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Creator homepage links are sent to Qinghu for paid or subscription-gated processing.

Mitigation: Install and use only when the user intends to use Qinghu's qhkit service, has a Qinghu API key, and understands what data will be submitted.

Risk: The generate action creates a paid task and may consume Qinghu credits.

Mitigation: Run an estimate with the exact parameters, disclose the estimated credits or credits notice, and wait for explicit user approval before generation.

Risk: Unsupported or incorrect URLs can produce unusable results.

Mitigation: Use only Douyin, Xiaohongshu, or Bilibili creator homepage links, verify online field labels with options when uncertain, and split batches larger than five accounts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-creator-data-engine)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON parameters; completed workflow status returns XLSX file links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires qhkit authentication, estimates paid workflow credits before generation, and supports up to five creator homepage links per run.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
