## Description:

LYGO LLM Console provides map scripts that print URLs and verify the kit SHA-256, plus an operator-run local GGUF portal with loopback HTTP, HTTPS search/fetch, workspace files, and optional workspace shell.

This skill is ready for commercial/non-commercial use.

## Publisher:

[deepseekoracle](https://clawhub.ai/user/deepseekoracle)

### License/Terms of Use:

MIT No Attribution (MIT-0)

## Use Case:

External users, developers, and operators use this skill to install and verify the LYGO LLM Console map layer, then run a local GGUF web console with the supplied kit after integrity checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The operator-run kit can execute local commands and Python as the current user.

Mitigation: Run it only as an unprivileged user, keep the working directory constrained to the verified extracted kit, and review command execution before use.

Risk: The bundled launcher and external engine supply chain require review before execution.

Mitigation: Verify the kit SHA-256 first, inspect or fix the BAT launcher path behavior, and obtain llama-server.exe only from the official source with separate integrity checks.

Risk: LAN exposure can increase token and command-execution risk.

Mitigation: Keep the console on loopback by default and enable LAN binding only with explicit consent and a clear understanding of the exposure.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/deepseekoracle/skills/lygo-llm-console)
- [Project Homepage](https://chatagent.ca/lygo-llm-console.html)
- [Security Reference](references/SECURITY.md)
- [Public Kit vs Admin](references/PUBLIC_VS_ADMIN.md)
- [Quickstart](examples/quickstart.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, plus JSON or plain-text map output from helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes pinned install guidance, kit SHA-256 verification, runtime setup notes, and loopback-first operating constraints.]

## Skill Version(s):

1.2.0 (source: SKILL.md frontmatter, claw.json, and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
