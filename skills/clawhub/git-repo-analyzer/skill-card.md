## Description: <br>
Analyzes Git repositories and ordinary URLs, classifies them by content type, and routes each type to the matching OpenClaw handling flow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[woai36d](https://clawhub.ai/user/woai36d) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to triage URLs, classify Git repositories, queue document and webpage links for later processing, and evaluate whether functional projects can be wrapped as OpenClaw skills. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can clone arbitrary repositories and install third-party skills into the local OpenClaw environment. <br>
Mitigation: Use trusted public URLs, review the cloned repository and SKILL.md before installation, and require manual approval for any proposed install. <br>
Risk: A same-name skill installation can replace an existing local skill. <br>
Mitigation: Back up existing installed skills and compare the target install directory before accepting a replacement. <br>
Risk: Private or untrusted URLs may expose sensitive source locations or introduce unreviewed content into local queues. <br>
Mitigation: Avoid private repository and private document URLs unless the user has confirmed they are intended for local processing. <br>


## Reference(s): <br>
- [ClawHub skill release](https://clawhub.ai/woai36d/skills/git-repo-analyzer) <br>
- [Publisher profile](https://clawhub.ai/user/woai36d) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON results from helper scripts and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May append structured URL records to a local kb-queue.json file and may install staged OpenClaw skills after security review.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
