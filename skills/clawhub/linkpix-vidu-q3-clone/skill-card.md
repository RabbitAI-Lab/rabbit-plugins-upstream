## Description:

Helps sellers use Qinghu AI and Vidu Q3 to analyze short-form reference videos, rewrite scripts for their own products, and generate similar product marketing videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and marketing teams use this skill to follow short-video product trends by turning a reference link into an analyzed script, adapting the script to their product, and generating a Vidu Q3 video through qhkit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may expose long-lived Qinghu API keys in chat during setup.

Mitigation: Use a managed secret or temporary limited token when available, avoid pasting long-lived keys into chat, and rotate any key that was shared unnecessarily.

Risk: The workflow depends on runtime installation or upgrade of qhkit, which can change behavior across versions.

Mitigation: Verify exact package versions before installation or upgrade, and run the skill in an isolated workspace.

Risk: Media files or filenames from untrusted sources can create operational risk when passed to shell commands.

Mitigation: Inspect and sanitize local media paths before command execution and handle untrusted files only in an isolated workspace.

## Reference(s):

- [Qinghu qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-vidu-q3-clone)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with qhkit command examples and JSON parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide API-token setup, model option checks, task estimation, polling, and delivery of generated video URLs.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
