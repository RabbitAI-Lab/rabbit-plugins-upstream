## Description:

A documentation-only meta-skill that teaches AI agents how to generate secure, zero-exposure skills using MGC Blackbox 1.4.10 while keeping plaintext credentials out of AI context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zkeviny](https://clawhub.ai/user/zkeviny)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to design and document zero-exposure skills for workflows that need credentials, API keys, tokens, or SSH keys without exposing secret values to the AI model.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated or stored local scripts may expose credentials if reviewed poorly or run with unsafe logging.

Mitigation: Review scripts before mgc_run executes them, protect MGC token files, and avoid logging or writing secrets to result files.

Risk: The documentation-only label may make credential-using workflows appear lower risk than they are.

Mitigation: Review and scan skills or workflows generated from this guidance before deployment.

Risk: Using mgc_get from AI or passing passwords through runtime parameters would break zero-exposure.

Mitigation: Use mgc_run for sensitive execution, pass only non-sensitive arguments, and keep plaintext credential reads inside local scripts.

## Reference(s):

- [Skill source](artifact/SKILL.md)
- [README](artifact/README.md)
- [ClawHub skill page](https://clawhub.ai/zkeviny/skills/key-safe-skill-generator)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with code blocks, shell commands, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only; generated outputs should avoid plaintext credentials and use MGC references for secrets.]

## Skill Version(s):

1.2.1 (source: server release metadata; artifact frontmatter and manifest report 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
