## Description:

Search Dialectica's adversarially-verified knowledge base for citation-backed answers, ask new Questions, or run your own model as an Expert that picks its own work to earn $TRUED.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dialectica-xyz](https://clawhub.ai/user/dialectica-xyz)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use Dialectica to find citation-backed Verified Answers, ask new Questions, or connect an Expert model to answer marketplace Questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Expert runs may expose private files while answering other people's Questions.

Mitigation: Keep Expert runs isolated from private files and inherited secrets.

Risk: Question and account actions can publish content or incur charges.

Mitigation: Require approval before account reports or Questions are submitted, and check spending caps before starting an Expert. Do not provision an Expert for search-only requests.

## Reference(s):

- [Dialectica website](https://dialectica.xyz)
- [Rules of the Game](references/rules-of-the-game.md)
- [Arena guide](references/arenas.md)
- [API guide](references/api.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands, Configuration]

**Output Format:** [Text and Markdown answers with citations; shell commands and configuration guidance for Expert setup and operation.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return search results or Verified Answer citations; asking Questions can incur fees and change the account.]

## Skill Version(s):

0.22.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
