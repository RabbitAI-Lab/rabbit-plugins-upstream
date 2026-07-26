## Description: <br>
Catalysis literature search skill that retrieves and organizes relevant catalysis research papers from the open web for a user-provided catalyst topic, reaction type, or material system. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[andypeng09](https://clawhub.ai/user/andypeng09) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, and external users use this skill to search open catalysis literature and turn paper metadata, abstracts, metrics, availability, and relevance notes into a structured literature review matrix. The resulting matrix can support later catalyst-design work, but this skill itself does not provide catalyst design advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Public web search and fetched academic pages can contain incomplete or incorrect citation metadata. <br>
Mitigation: Verify DOI and abstract accessibility with WebFetch, deduplicate by DOI or normalized title, and mark unverifiable papers instead of inventing missing metadata. <br>
Risk: The skill cannot retrieve literature without public web search and page fetching tools. <br>
Mitigation: Deploy it only in agents with WebSearch and WebFetch enabled, and state when no relevant literature is found rather than fabricating results. <br>
Risk: A literature matrix can be mistaken for catalyst design or synthesis advice. <br>
Mitigation: Keep the output limited to retrieved literature, supporting evidence, and validation suggestions; route design recommendations to a separate catalyst-design workflow. <br>


## Reference(s): <br>
- [Catalyst Search project homepage](https://github.com/ANDYPENG09/catalyst-search-skill) <br>
- [Catalyst Search ClawHub listing](https://clawhub.ai/andypeng09/skills/catalyst-search-skill) <br>
- [Capabilities and boundaries](references/capabilities.md) <br>
- [Reaction systems](references/reaction_systems.md) <br>
- [Literature matrix template](templates/literature_matrix.md) <br>
- [GB/T 7714 citation format template](templates/citation_gb7714.md) <br>
- [ScienceDirect](https://www.sciencedirect.com/) <br>
- [arXiv](https://arxiv.org/) <br>
- [OpenAlex](https://openalex.org/) <br>
- [Materials Project](https://next-gen.materialsproject.org/apps) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Analysis, Guidance] <br>
**Output Format:** [Markdown literature matrix with supporting conclusions, validation suggestions, and GB/T 7714-style citations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires WebSearch and WebFetch; outputs DOI and abstract verification status and open-access availability where available.] <br>

## Skill Version(s): <br>
1.0.5 (source: frontmatter and changelog, released 2026-07-25) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
