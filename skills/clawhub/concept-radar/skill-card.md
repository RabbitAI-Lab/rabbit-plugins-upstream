## Description:

Discovers, deduplicates, and evaluates evidence-backed concepts when explicitly invoked for specified URLs or an author pool.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and analysts use this skill to discover concepts from public URLs or an author pool, consolidate overlaps, and evaluate each retained concept against public evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can search and fetch public web pages when explicitly invoked, which may expose private or access-controlled source details if a user supplies them.

Mitigation: Use only public, intended research sources unless the user is comfortable with the agent inspecting the supplied pages through web tools.

Risk: Concept maturity, confidence, and deduplication decisions may be uncertain when public evidence is sparse or inaccessible.

Mitigation: Label unsupported dimensions as Unknown, record access gaps, retain supporting URLs, and evaluate conservatively.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/concept-radar)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown with evidence links, rubric ratings, and concise rationales]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a scope note, deduplication notes, maturity and confidence ratings, applicable scenarios, boundaries, and evidence gaps.]

## Skill Version(s):

0.1.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
