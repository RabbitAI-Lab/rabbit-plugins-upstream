## Description:

Documents how agents can store, run, and seal MGC Blackbox scripts through MCP, REST API, and WebUI while requiring explicit user authorization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zkeviny](https://clawhub.ai/user/zkeviny)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this documentation skill to guide agents through local MGC Blackbox script management, including encrypted storage, approved execution, runtime parameters, internal credential access, and script sealing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local script execution and credential access can affect the user's environment.

Mitigation: Require explicit approval before every save, run, seal, or credential-related action, and execute only scripts from trusted sources.

Risk: The zero-exposure claim is not universal because scripts passed through agent tool calls may be visible to the agent before encrypted storage.

Mitigation: Avoid sending sensitive script plaintext through agent-visible channels and verify the intended MGC data flow before storing or running scripts.

Risk: The agent cannot audit script content during blackbox execution.

Mitigation: Have a human verify the script source, purpose, and expected access to sensitive data before execution.

Risk: MGC 1.4.9 script execution issues may cause parameter parsing failures or missing output.

Mitigation: Use parse_known_args, strip quotes from runtime values, write substantial results to files, and review output files after execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zkeviny/skills/secure-script-runner)
- [MGC Blackbox repository](https://github.com/zkeviny/MGC-Blackbox)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline code blocks, shell commands, JSON snippets, and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit user authorization before save, run, seal, or credential-related actions.]

## Skill Version(s):

1.1.1 (source: release evidence, frontmatter, and manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
