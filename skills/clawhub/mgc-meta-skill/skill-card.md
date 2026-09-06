## Description:

Local encrypted credential and script management for AI agents, with guidance for storing tokens, passwords, configs, and scripts and running them through MGC tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zkeviny](https://clawhub.ai/user/zkeviny)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to configure MGC Blackbox workflows for local secret storage, script execution, sealed script distribution, and MCP or REST integration. It is intended for trusted local environments where agents need structured access to stored credentials or scripts without embedding those values directly in skill source.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents or local callers can use `mgc_get` and the REST API as plaintext secret access paths.

Mitigation: Use the skill only in trusted local environments, restrict access to the MGC token, and treat retrieval operations as direct access to sensitive values.

Risk: Stored scripts can be executed through MGC tool paths.

Mitigation: Install and run only scripts that have been explicitly reviewed and trusted for the local environment.

Risk: The `~/.mgc` token file controls access to local MGC operations.

Mitigation: Protect and permission the token file so only intended users and agent processes can read it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zkeviny/skills/mgc-meta-skill)
- [Artifact README](artifact/README.md)
- [Artifact skill definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code examples, shell commands, and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces operational guidance for MGC Blackbox tools; it does not itself return stored secrets or script output.]

## Skill Version(s):

1.4.10 (source: server release evidence, artifact frontmatter, artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
