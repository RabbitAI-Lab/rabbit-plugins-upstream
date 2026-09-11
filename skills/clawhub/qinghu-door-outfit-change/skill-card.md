## Description:

This skill helps agents generate Qinghu/LinkPix door-outfit-change videos from one model image, up to four clothing images, and optional audio for womenswear styling and commerce content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, commerce teams, and agents supporting them use this skill to prepare and submit Qinghu/LinkPix door-outfit-change video jobs, check pricing, poll completion, and return generated media links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the agent to install and run the third-party qhkit npm CLI.

Mitigation: Use a pinned or local CLI install where possible and review the package before allowing execution.

Risk: The workflow requires a Qinghu API token.

Mitigation: Use a narrowly scoped token, keep it out of source files and logs, and revoke it when no longer needed.

Risk: The workflow uploads model, clothing, and optional audio files to Qinghu/LinkPix.

Mitigation: Use only owned or authorized media and confirm upload consent before generation.

Risk: Video generation can consume paid Qinghu credits.

Mitigation: Run the estimate command first and wait for user confirmation before submitting generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-door-outfit-change)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON parameters and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated media URLs and a final Qinghu credit consumption line after workflow completion.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
