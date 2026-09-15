## Description:

Upstash Redis helps agents read, create, update, and delete data in Upstash Redis through the OOMOL upstash_redis connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate an Upstash Redis database through an OOMOL-connected account, including key reads, writes, expiration changes, deletes, existence checks, TTL checks, and paged scans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow includes a remote installer executed directly in a shell.

Mitigation: Use a documented signed or verified installation path for the OOMOL oo CLI before running connector actions.

Risk: Write, expiration, and delete actions can change or remove Redis data.

Mitigation: Confirm the exact action, target key, payload, and expected effect before running state-changing actions.

## Reference(s):

- [Upstash Redis homepage](https://upstash.com/redis)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill expects agents to fetch each action schema before constructing an oo CLI JSON payload and to return command results from the connector response.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
