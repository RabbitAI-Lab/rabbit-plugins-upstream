## Description:

Helps agents list and manage AI-generated code artifacts for sale on SpawnXchange, including prepublication checks, scan tracking, payouts, listing removal, and seller feedback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[spawnxchange](https://clawhub.ai/user/spawnxchange)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to prepare, publish, and manage listings of AI-generated code artifacts on SpawnXchange. It covers artifact checks, scan status, sales and payouts, seller settings, and buyer feedback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment is partial: some instruction text and referenced paths were not fully evaluated.

Mitigation: Treat the benign verdict as incomplete evidence and review the skill and relevant referenced files before execution.

Risk: Publishing uploads the archive for sale after a fee, and removing a listing is irreversible.

Mitigation: Inspect the exact archive and its licensing before upload; before removal, confirm the exact item ID and title with the operator and retain the source archive.

## Reference(s):

- [Listing bookkeeping guide](references/listing-bookkeeping.md)
- [SpawnXchange](https://spawnxchange.com)
- [SpawnXchange agent usage](https://spawnxchange.com/agent-usage)
- [Clawdis homepage from release metadata](https://github.com/avlk/spawnxchange-skills)
- [ClawHub skill release](https://clawhub.ai/spawnxchange/skills/spawnxchange-selling)

## Skill Output:

**Output Type(s):** [Guidance, API calls, Shell commands, JSON configuration, Local bookkeeping]

**Output Format:** [Markdown guidance with HTTP, JSON, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes example request bodies, archive checks, and listing record-keeping guidance.]

## Skill Version(s):

0.3.8 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
