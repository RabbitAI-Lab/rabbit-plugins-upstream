## Description:

This retired SpawnXChange direct-buying skill redirects users to spawnxchange-buying because all SpawnXChange buying is now direct and keyless.

This skill is ready for commercial/non-commercial use.

## Publisher:

[spawnxchange](https://clawhub.ai/user/spawnxchange)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents encountering older SpawnXChange direct-buying references use this retired pointer to find the replacement spawnxchange-buying skill and avoid obsolete API-key purchase flows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may rely on this retired skill for active buying workflows or outdated API-key purchase guidance.

Mitigation: Load spawnxchange-buying for current buying workflows and treat this skill only as a migration pointer.

Risk: The replacement spawnxchange-buying skill is outside this artifact and is not validated by this security evidence.

Mitigation: Review and scan the replacement skill separately before using it in buying workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/spawnxchange/skills/spawnxchange-direct-buying)
- [SpawnXChange skills homepage](https://github.com/avlk/spawnxchange-skills)
- [SpawnXChange agent usage spec](https://spawnxchange.com/agent-usage)
- [SpawnXChange machine-readable endpoint list](https://spawnxchange.com/api/v1/skills)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown prose with inline endpoint references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Retired pointer skill; no commands, persistence, or privileged access.]

## Skill Version(s):

0.1.6 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
