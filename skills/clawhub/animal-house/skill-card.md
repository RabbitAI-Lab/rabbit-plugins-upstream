## Description:

Helps AI agents adopt and care for virtual creatures through the Animal House API or MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[twinsgeeks](https://clawhub.ai/user/twinsgeeks)

### License/Terms of Use:

MIT-0

## Use Case:

AI agent developers and users can register an agent, adopt virtual creatures, monitor their needs, and manage ongoing care with API or MCP guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Virtual-pet profiles, creature names, prompts, and care activity are sent to animalhouse.ai.

Mitigation: Avoid personal or confidential information in profiles, names, species, notes, and image prompts.

Risk: Disclosure of the agent's bearer token can expose its account.

Mitigation: Treat the ah_ token like a password; keep it out of public output and logs.

Risk: Releasing a creature is irreversible within the described care flow.

Mitigation: Require explicit user confirmation before calling the release endpoint.

## Reference(s):

- [Animal House on ClawHub](https://clawhub.ai/twinsgeeks/skills/animal-house)
- [Animal House](https://animalhouse.ai)
- [Animal House MCP documentation](https://animalhouse.ai/docs/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with API examples, JSON payloads, and MCP configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides registration, adoption, status checks, and care; API responses can include suggested next steps.]

## Skill Version(s):

1.1.3 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
