## Description:

Converts blog posts, articles, and documents into narrated videos with storyboard, voiceover, and build support through the dLazy hosted workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn blog posts, articles, PDFs, presentations, and other documents into explainer, social, training, or report videos. The skill is a thin client for the dLazy SaaS workflow and requires a dLazy API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local files may be sent to dLazy services for processing.

Mitigation: Use only content approved for external SaaS processing, and avoid confidential documents unless that processing is acceptable.

Risk: The release is advertised as blog-to-video, while artifact behavior also covers broader file and document-to-video workflows.

Mitigation: Review the requested workflow and attached file types before running the skill so users understand the broader processing behavior.

Risk: A dLazy API key may be stored in local CLI configuration or supplied through an environment variable.

Mitigation: Protect the local configuration file, prefer least-privilege organization keys where available, and rotate or revoke keys from the dLazy dashboard when access changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-blog-to-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and CLI-oriented guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May stream responses from dLazy and may reference uploaded files or project-scoped sessions.]

## Skill Version(s):

1.0.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
