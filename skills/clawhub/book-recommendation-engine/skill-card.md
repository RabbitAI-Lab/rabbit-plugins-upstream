## Description:

Book Recommendation Engine supports collaborative filtering, content similarity, trending-book, and tag-expansion recommendations, plus themed booklists, Open Library search, and wishlist tracking with price checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xuan905](https://clawhub.ai/user/xuan905)

### License/Terms of Use:

MIT

## Use Case:

Readers, researchers, and agents can use this skill to recommend books from a local library, search Open Library by title, author, or ISBN, generate themed reading lists, and maintain a wishlist with priorities and price history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores library, rating, wishlist, and price-history data locally under the user's home directory.

Mitigation: Use it only on machines where local storage of reading preferences is acceptable, and review exported wishlist or library files before sharing them.

Risk: Live lookup, web-summary, and price-check features send book queries or ISBNs to external book and search sites.

Mitigation: Avoid live lookup, web-summary, and price-check commands for sensitive reading interests or ISBNs; use local recommendation and list features instead.

## Reference(s):

- [Server-resolved GitHub source](https://github.com/xuan905/book-recommendation-engine)
- [ClawHub skill page](https://clawhub.ai/xuan905/skills/book-recommendation-engine)
- [Open Library](https://openlibrary.org)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands]

**Output Format:** [Terminal text, Markdown reading lists, JSON exports, and local data files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May cache lookup results and store library, rating, wishlist, and price-history data under the user's home directory.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
