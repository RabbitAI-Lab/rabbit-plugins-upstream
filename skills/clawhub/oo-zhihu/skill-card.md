## Description:

Zhihu lets an agent read, search, create, and update Zhihu data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent search and read Zhihu content, list account-backed public resources, and run write-capable Zhihu or Zhida workflows through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write-capable actions can change Zhihu or Zhida resources.

Mitigation: Confirm the exact payload and expected effect with the user before running actions marked `[write]`, and inspect the live connector schema before constructing payloads.

Risk: The skill operates through the user's OOMOL-connected Zhihu account.

Mitigation: Use the skill only when the user intends account-backed Zhihu operation, and avoid handling raw credentials directly.

Risk: Setup commands can install the oo CLI or initiate account login.

Mitigation: Run one-time install, login, or connection steps only after a command fails because the CLI or account connection is missing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-zhihu)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Zhihu Homepage](https://www.zhihu.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The oo CLI returns JSON data with execution metadata for connector runs.]

## Skill Version(s):

1.0.1 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
