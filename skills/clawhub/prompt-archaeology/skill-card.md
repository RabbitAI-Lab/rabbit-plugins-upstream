## Description:

Excavate forgotten solutions, code snippets, and decisions from past conversation sessions. Use when the user is re-solving a problem you've likely solved before, hunting for a lost snippet, or wants to mine session history for buried knowledge instead of starting from scratch.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill to search authorized conversation logs, recover prior fixes or decisions, rank likely matches, extract concise evidence, and deduplicate repeated findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can search sensitive session archives when an agent is pointed at directories containing private or shared conversation history.

Mitigation: Limit searches to authorized local history and avoid using it across other users' private profiles unless explicitly authorized.

Risk: The reusable index feature loads pickle files unsafely according to the security summary.

Mitigation: Avoid loading shared, downloaded, or old index files unless their origin is fully trusted; prefer direct directory searches or replace pickle persistence before broad use.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/voronindenis5/prompt-archaeology)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/prompt-archaeology)
- [Search strategies](references/search-strategies.md)
- [Relevance scoring](references/relevance-scoring.md)
- [Extraction patterns](references/extraction-patterns.md)
- [Deduplication](references/deduplication.md)
- [CLI reference](references/cli-reference.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands]

**Output Format:** [Markdown guidance with inline code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May cite recovered session paths or identifiers when reporting extracted artifacts.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
