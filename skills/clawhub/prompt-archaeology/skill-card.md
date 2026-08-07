## Description:

Prompt Archaeology helps agents recover prior fixes, code snippets, decisions, commands, and rejected approaches from authorized past conversation sessions instead of re-solving known problems.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to search authorized session logs, notes, or exported conversation history for prior fixes, decisions, commands, and rejected approaches. It is intended for cases where a user suspects the answer was already worked out in an earlier session and wants a cited, minimal artifact.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Searching session logs or notes can expose private, credential-bearing, or otherwise sensitive content.

Mitigation: Search only directories you are authorized to process, avoid credential or personal-data locations, and review extracted snippets before sharing them.

Risk: Existing index files are loaded with Python pickle, which is unsafe for untrusted input.

Mitigation: Create indexes locally from trusted corpora and do not open index files from other people unless the index format is changed away from pickle or an explicit trusted-only warning and opt-in unsafe path are added.

Risk: Recovered historical fixes or decisions may be stale or incomplete.

Mitigation: Require source-session citation and validate any recovered command, code, or decision against the current repository, dependencies, and user requirements before applying it.

## Reference(s):

- [Source repository](https://github.com/voronindenis5/prompt-archaeology)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/prompt-archaeology)
- [Search strategies](references/search-strategies.md)
- [Relevance scoring](references/relevance-scoring.md)
- [Extraction patterns](references/extraction-patterns.md)
- [Deduplication](references/deduplication.md)
- [CLI reference](references/cli-reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown guidance with optional quoted excerpts, code blocks, and shell commands; the bundled CLI prints plain-text ranked search results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May cite source session paths, include score explanations, and deduplicate near-identical results when requested.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
