## Description:

Queries book details by ISBN or searches books by title keyword using the JisuAPI ISBN service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jisuapi](https://clawhub.ai/user/jisuapi)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to help users identify books from ISBN-10 or ISBN-13 values, search for books by title keywords, and summarize returned bibliographic details such as title, author, publisher, publication date, price, summary, cover, and ISBN.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends ISBNs or title keywords to JisuAPI and requires a JISU_API_KEY.

Mitigation: Treat the API key as a secret and avoid using the skill for confidential book lists or sensitive lookup terms.

Risk: Returned cover, seller, or product links may point to third-party sites.

Mitigation: Do not automatically fetch or open returned links; review them before use.

Risk: Book metadata is provided by a third-party API and may be incomplete or stale.

Mitigation: Verify important bibliographic details against an authoritative source before relying on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jisuapi/skills/isbn)
- [JisuAPI publisher profile](https://clawhub.ai/user/jisuapi)
- [JisuAPI ISBN documentation](https://www.jisuapi.com/api/isbn/)
- [JisuAPI website](https://www.jisuapi.com/)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with JSON command inputs and JSON tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and the JISU_API_KEY environment variable; returned API data may include book metadata, cover URLs, and seller links.]

## Skill Version(s):

1.0.6 (source: server release metadata, created 2026-09-10T09:38:31Z)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
