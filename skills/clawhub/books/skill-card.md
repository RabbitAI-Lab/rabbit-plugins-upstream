## Description: <br>
CLI for AI agents to search and lookup books for their humans. Uses Open Library API. No auth required. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jeffaf](https://clawhub.ai/user/jeffaf) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and AI agents use this skill to search Open Library for books, retrieve work details by Open Library work ID, and look up author information and bibliographies. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The reviewed ClawHub artifact does not include the executable `books` scripts described by the documentation. <br>
Mitigation: Review the fetched script source before use and pin the external repository or commit when installing from the README's clone instructions. <br>
Risk: The skill is intended for explicit public book, work ID, or author lookup requests and may be over-applied to unrelated book conversations. <br>
Mitigation: Invoke it only when the user asks for book search, Open Library work details, or author metadata. <br>


## Reference(s): <br>
- [ClawHub Books skill page](https://clawhub.ai/jeffaf/skills/books) <br>
- [Open Library](https://openlibrary.org) <br>
- [Open Library API](https://openlibrary.org/developers/api) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Plain text and Markdown with inline shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs can include book titles, Open Library work IDs, authors, publication years, ratings, subjects, descriptions, author biographies, bibliography entries, and cover image links.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
