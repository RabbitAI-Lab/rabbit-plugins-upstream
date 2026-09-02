## Description:

詹明明·哪里会被划走 helps an agent review talking-head scripts for viewer drop-off risk by scanning paragraph transitions, information-density dips, and hard-to-say sentences.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and writing assistants use this skill to review Chinese talking-head scripts for flow and retention risk, then decide whether to request a marked-up rewrite that preserves the creator's voice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read existing zmm reference and memory files and save narrow memory notes about corrections or retention results after use.

Mitigation: Review the memory behavior before installation, use explicit slash commands to reduce accidental activation, and avoid sensitive drafts unless scoped retention is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-flow)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance, Text]

**Output Format:** [Markdown report with optional marked-up rewrite guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include paragraph structure, issue list, overall assessment, and a prompt asking whether to proceed with marked-up edits.]

## Skill Version(s):

0.2.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
