## Description:

Measure and safely reduce always-loaded agent instruction context in characters and tokens.

This skill is ready for commercial/non-commercial use.

## Publisher:

[posthuman](https://clawhub.ai/user/posthuman)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to audit always-loaded agent instruction files, identify context-budget pressure, and safely reduce duplicated or task-specific material without weakening authority, safety, or meaning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running reports on repositories you do not fully control may expose raw headings in terminal output.

Mitigation: Prefer JSON output or trusted files, keep report output local, and review headings before sharing results.

Risk: Editing always-loaded instruction files can weaken policy, authority, or availability even when token counts improve.

Mitigation: Use explicit edit scopes, review diffs carefully, preserve higher-precedence rules, and avoid token-only compression of security policy.

## Reference(s):

- [Method and measurements](artifact/references/method.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples; the helper script emits plain text or JSON reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Token counts are exact only when an explicit trusted loopback tokenizer is selected; otherwise reports label token counts as estimates.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
