## Description:

Run an adaptive, bounded, evidence-backed work loop when the user explicitly invokes it, asks it to remain active for the current task or thread, or when active personal, workspace, or project instructions declare it the default.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ojusave](https://clawhub.ai/user/ojusave)

### License/Terms of Use:

MIT

## Use Case:

Developers, writers, researchers, and product teams use this skill to run bounded feedback loops for coding, product and UI work, accessibility, research, strategy, public writing, and reusable prompts. It helps an agent define success, choose an appropriately small loop, collect evidence, and stop with an explicit status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can stay active across substantive follow-ups in the same task, which may be broader than a user expects if enabled as a default workflow.

Mitigation: Use explicit invocation for narrow adoption and avoid default activation when the skill should run only on direct command.

Risk: Deep workflows can create local .loop task notes and handoff files.

Mitigation: Review generated local state in sensitive environments and avoid storing secrets, credentials, personal data, copied production data, or hidden reasoning in loop state.

Risk: Bundled helper scripts may be run by the agent during verification, handoff, prompt, claim, or editorial checks.

Mitigation: Review bundled scripts before deployment and prefer pinned or manually reviewed install and update methods in sensitive environments.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/ojusave/loop-engineering)
- [ClawHub skill page](https://clawhub.ai/ojusave/skills/loop-engineering)
- [Engineering Loop](references/engineering-loop.md)
- [Product UX Loop](references/product-ux-loop.md)
- [Prompt Generation](references/prompt-generation.md)
- [Verification](references/verification.md)
- [Orchestration](references/orchestration.md)
- [Source Integrity](references/source-integrity.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, plain text, code snippets, shell commands, and local workflow artifacts when task scope requires them]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local .loop task state or handoff files during deeper multi-cycle work; otherwise output is kept in the active agent response.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
