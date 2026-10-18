## Description:

Helps operators inspect and launch a local GGUF-based LLM console with an agent portal and optional workspace tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[deepseekoracle](https://clawhub.ai/user/deepseekoracle)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect a bundled local console, verify its files, and run GGUF-based inference and agent tools on their own machine; it is not a hosted or multi-user service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local startup endpoint exposes a process-control token without authentication.

Mitigation: Keep the console bound to loopback, avoid LAN exposure, and fix or disable the doorbell startup endpoint before relying on its token boundary.

Risk: Optional workspace shell and Python tools execute as the current user; the console is not a sandbox.

Mitigation: Review the kit before running it, use an unprivileged user, and do not serve untrusted users.

Risk: Local chat history and state remain on disk.

Mitigation: Use the console only if local retention is acceptable, and remove its stored data when no longer needed.

## Reference(s):

- [ClawHub release](https://clawhub.ai/deepseekoracle/skills/lygo-llm-console)
- [LYGO LLM Console overview](https://chatagent.ca/lygo-llm-console.html)
- [Security notes](references/SECURITY.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Plain text and Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can report local kit file hashes and verification results.]

## Skill Version(s):

1.6.3 (source: ClawHub release and claw.json; SKILL.md frontmatter says 1.6.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
