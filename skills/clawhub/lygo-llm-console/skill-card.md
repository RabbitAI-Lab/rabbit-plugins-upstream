## Description:

LYGO LLM Console is a public ClawHub skill and kit for a local GGUF-based LLM console with a browser agent portal, Wikipedia and HTTPS fetch, workspace shell and Python limbs, and P0-gated generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[deepseekoracle](https://clawhub.ai/user/deepseekoracle)

### License/Terms of Use:

MIT No Attribution (MIT-0)

## Use Case:

Developers and local AI operators use this skill to install and inspect the LYGO LLM Console release, run map and self-check commands, and operate the bundled public kit for local GGUF model serving and agent-portal workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled runtime can run processes and expose shell or Python limbs while the public skill metadata declares no subprocess or shell access.

Mitigation: Run the kit as an unprivileged user, keep it in a dedicated non-sensitive workspace, and review proposed shell or Python actions before execution.

Risk: The runtime can fetch web content and download HTTPS resources.

Mitigation: Use trusted HTTPS targets, verify downloaded files and engine binaries against pinned checksums or trusted release sources, and treat fetched content as untrusted input.

Risk: The runtime can write files under kit-local workspace and save directories.

Mitigation: Use a dedicated workspace and inspect generated files before moving them into sensitive projects or repositories.

Risk: Enabling LAN binding can expose the local console beyond loopback.

Mitigation: Keep the default 127.0.0.1 binding unless remote access is required, and use token controls when LAN access is explicitly enabled.

## Reference(s):

- [LYGO LLM Console homepage](https://chatagent.ca/lygo-llm-console.html)
- [ClawHub skill page](https://clawhub.ai/deepseekoracle/skills/lygo-llm-console)
- [Public kit download](https://chatagent.ca/data/lygo-full-skills/dist/lygo-llm-console-public.zip)
- [Security notes](references/SECURITY.md)
- [Public kit vs admin console](references/PUBLIC_VS_ADMIN.md)
- [Credits](references/CREDITS.md)
- [Quickstart](examples/quickstart.md)
- [Public kit README](kit/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown documentation, JSON map output, plain text command output, and local runtime tool results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The public runtime can return fetched HTTPS text, captured shell or Python output, workspace file content, and generated files under kit-local workspace or save directories.]

## Skill Version(s):

1.1.0 (source: server release, SKILL.md frontmatter, claw.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
