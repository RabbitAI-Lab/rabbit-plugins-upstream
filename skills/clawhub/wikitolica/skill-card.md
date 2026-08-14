## Description:

Searches and retrieves Spanish-language articles from Wikitólica, a Catholic encyclopedia with 4,400+ articles on doctrine, saints, popes, theology, church history, liturgy, sacraments, and biblical studies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cursocatolico](https://clawhub.ai/user/cursocatolico)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to answer Catholic-topic questions in Spanish using Wikitólica as a reference source. It is suited for finding article slugs, retrieving article text, and returning URLs with required attribution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate for broad Catholic-related topics and rely on Wikitólica as a single Spanish-language source.

Mitigation: Ask for additional sources or a broader research scope when the question requires comparison, non-Catholic perspectives, or independent verification.

Risk: Responses may default to Spanish because the source content and skill instructions are Spanish-language.

Mitigation: Ask explicitly for another output language when the user needs translation or localization.

Risk: Article URLs or slugs can be wrong if generated without checking Wikitólica.

Mitigation: Use MCP search or the sitemap to identify real slugs before returning article URLs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cursocatolico/skills/wikitolica)
- [Wikitólica](https://www.wikitolica.com)
- [Zenodo DOI](https://doi.org/10.5281/zenodo.19387074)
- [Publisher profile](https://clawhub.ai/user/cursocatolico)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown responses in Spanish with article URLs, excerpts or article text, and attribution when Wikitólica content is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses real Wikitólica slugs from MCP search or the sitemap and attributes content as Wikitólica (CC BY-SA 4.0).]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
