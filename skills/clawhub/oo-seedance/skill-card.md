## Description:

Seedance helps agents manage Seedance video generation through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit Seedance video generation jobs, inspect task status and results, list visible generations, and cancel or delete tasks through their OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submit and delete actions can change Seedance state or remove tasks.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running write or destructive connector commands.

Risk: The first-time setup fallback includes pipe-to-shell installer commands.

Mitigation: Use a verified or version-pinned install method when available, and run installer commands only after the user trusts OOMOL's distribution channel.

## Reference(s):

- [ClawHub Seedance Skill](https://clawhub.ai/oomol/skills/oo-seedance)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Seedance homepage](https://www.volcengine.com/product/ark)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to inspect live connector schemas before running oo connector commands; connector responses may include JSON data and meta.executionId.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
