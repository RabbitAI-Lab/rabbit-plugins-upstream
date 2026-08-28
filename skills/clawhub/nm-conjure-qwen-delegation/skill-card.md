## Description:

Delegates tasks to Qwen CLI via delegation-core for Alibaba's models.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to delegate batch processing, summarization, and multi-file analysis to the Qwen CLI through delegation-core when Qwen is installed and configured.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected files may be sent to the configured Qwen provider when users run the suggested commands.

Mitigation: Review file globs before delegation and avoid including secrets or sensitive files.

Risk: Qwen credentials can be exposed if API keys are hard-coded or committed.

Mitigation: Keep API keys in normal secret-management flows and do not hard-code them in skill files or examples.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-conjure-qwen-delegation)
- [Conjure plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/conjure)
- [Qwen-specific configuration](modules/qwen-specifics.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference selected file globs that the user passes to Qwen CLI.]

## Skill Version(s):

1.9.19 (source: release evidence; artifact frontmatter reports 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
