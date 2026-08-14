## Description:

Prompt Optimizer turns rough prompts into structured, constrained, versioned prompts with output-format guidance, self-check steps, and A/B benchmarking support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, prompt engineers, and teams use this skill to improve weak prompts into reusable structured prompts, compare prompt variants, and keep lightweight optimization history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent learning records may store user preferences, notes, and usage history.

Mitigation: Review learned preference/history files before sharing the skill directory and disable or avoid the learner script when persistent notes are not desired.

Risk: Local helper scripts can write optimized prompts, benchmark reports, logs, and learned history files.

Mitigation: Run the scripts in a controlled working directory and review generated files before using them as team templates or production prompt assets.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with local shell command examples and optional JSON benchmark or learning reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write optimized prompt files, benchmark reports, optimization logs, and learned preference/history JSON files when its scripts are run.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
