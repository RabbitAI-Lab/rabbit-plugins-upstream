## Description:

Look up French Horn F/Bb double horn valve fingerings, trigger combinations, concert pitch transposition, and alternate harmonic partials via the HornLib MCP server at https://hornlib.com/api/mcp.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hornlib](https://clawhub.ai/user/hornlib)

### License/Terms of Use:

MIT

## Use Case:

External users, including French horn players and learners, use the skill to look up F/Bb double horn fingerings, trigger combinations, concert pitch transposition, and harmonic tendencies for a written note.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contacts HornLib when looking up a fingering, so the service receives the lookup request.

Mitigation: Review the HornLib endpoint and use the lookup only when you are comfortable contacting that service; avoid including sensitive information in note queries.

## Reference(s):

- [Interactive French Horn Fingering Chart](https://hornlib.com/fingerings)
- [HornLib MCP endpoint](https://hornlib.com/api/mcp)
- [All French Horn Notes & Valve Combinations](https://hornlib.com/all-notes)
- [French Horn Beginner Pedagogy & Embouchure Guide](https://hornlib.com/beginners)
- [French Horn Practice & Transposition Tools](https://hornlib.com/7-in-1-tools)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text containing fingering, trigger, transposition, and harmonic lookup results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Lookup for a written note; documented range C1 to F6.]

## Skill Version(s):

1.0.3 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
