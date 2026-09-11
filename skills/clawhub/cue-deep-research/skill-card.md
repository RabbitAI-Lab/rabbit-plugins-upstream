## Description:

Cue 深度研究（通用版） helps agents run public-source financial, business, and industry research through Cue, with cross-validated findings and source links in the resulting report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agent users use this skill to submit open-information research questions about companies, industries, competitors, markets, and compliance risks, then receive a sourced Markdown research report. The skill is intended for public information retrieval and does not claim support for personal data or non-public information handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release instructs users to execute an unpinned external runner, which can change behavior after the skill is published.

Mitigation: Inspect or pin the sensedeal/cue-skills repository to a trusted commit before installing or running it.

Risk: The mimic-file option uploads a local document to the Cue service for style analysis.

Mitigation: Do not use mimic-file with confidential, personal, regulated, or proprietary documents; use public reference links or non-sensitive samples instead.

Risk: The runner depends on a Cue API key for authentication.

Mitigation: Use a revocable Cue API key, keep it out of shared logs and prompts, and rotate it if exposure is suspected.

Risk: The security verdict is suspicious because external runner execution requires review before installation.

Mitigation: Run the skill in a dedicated environment and review the runner before connecting it to sensitive workspaces.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-deep-research)
- [Cue runner repository](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)
- [Cue API key setup](https://cuecue.cn/hub/api-key)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown research report written to a local file, with inline source links and optional conversion guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Research jobs are documented as taking about 3-15 minutes and may use optional mimic-url or mimic-file inputs for style matching.]

## Skill Version(s):

1.0.8 (source: ClawHub release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
