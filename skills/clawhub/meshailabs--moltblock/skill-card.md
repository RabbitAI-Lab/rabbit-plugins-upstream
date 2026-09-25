## Description:

Verification gating for AI-generated artifacts. Policy checks to catch dangerous patterns before execution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[meshailabs](https://clawhub.ai/user/meshailabs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to check higher-risk AI-generated tasks and artifacts before execution. It is intended for policy verification of operations involving destructive commands, privilege changes, credentials, filesystem writes, network calls, subprocesses, or dynamic code evaluation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the npm package may execute third-party package code on the user's machine.

Mitigation: Install only after reviewing and trusting the package; prefer npx over a global install.

Risk: Task descriptions may be sent to the selected LLM provider.

Mitigation: Use a dedicated limited-scope API key and avoid submitting secrets, confidential code, or sensitive operational details unless the package and provider path are trusted.

Risk: LLM-backed verification can miss dangerous patterns or produce incorrect pass/fail decisions.

Mitigation: Treat verification as an additional gate and continue reviewing generated artifacts before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/meshailabs/skills/moltblock)
- [Moltblock homepage](https://github.com/moltblock/moltblock)
- [Moltblock configuration documentation](https://github.com/moltblock/moltblock#configuration)
- [Moltblock npm package](https://www.npmjs.com/package/moltblock)
- [Release 0.11.9](https://github.com/moltblock/moltblock/releases/tag/v0.11.9)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [JSON verification result and concise text guidance, with markdown examples for shell commands and configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns pass/fail verification status with evidence; may use a configured LLM provider selected from environment variables.]

## Skill Version(s):

0.11.9 (source: server release metadata; artifact frontmatter and install examples mention 0.11.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
