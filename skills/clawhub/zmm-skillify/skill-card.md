## Description:

Turns a completed, verified workflow from the current session into a reusable local skill with gates, observable criteria, self-checks, and evaluation guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill after a workflow has produced a verified result to extract the process into a reusable local skill. It helps define gates, success criteria, observable rules, self-checks, and evaluation samples before the skill is handed off.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Conversational trigger phrases can cause the agent to start skill creation before a workflow has actually been completed and verified.

Mitigation: Confirm there is a completed, verified workflow before allowing the agent to write files or memory.

Risk: The skill intentionally supports local skill and memory writes, which creates persistence risk if used on untrusted or unverified workflows.

Mitigation: Install and invoke it only when local reusable skill creation is desired, and review generated skill files before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-skillify)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with file plans, checklists, and code or shell command snippets when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local skill files, evaluation notes, and memory-note guidance when the required workflow validation gates pass.]

## Skill Version(s):

0.1.4 (source: server release metadata; artifact frontmatter says 0.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
