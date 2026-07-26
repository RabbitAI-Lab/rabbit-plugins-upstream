## Description: <br>
Searches read-only wine and alcohol information, ratings, price comparisons, vintage guidance, food pairings, and health-related drinking context across multiple external data sources. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[amurtiger01](https://clawhub.ai/user/amurtiger01) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agents use this skill to look up wine details, compare prices, inspect vintage information, identify labels, and prepare read-only search links without making purchases or changing accounts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional Firecrawl mode can send the API key over an unverified TLS retry path. <br>
Mitigation: Avoid configuring FIRECRAWL_API_KEY until the TLS fallback is fixed, or review and patch the Firecrawl request path before using Firecrawl with credentials. <br>
Risk: Optional OCR processing may handle untrusted wine label images with image libraries. <br>
Mitigation: Avoid optional OCR dependencies for untrusted images, or upgrade and scan dependencies before enabling label image processing. <br>


## Reference(s): <br>
- [Wine Info Search Homepage](https://github.com/Amurtiger01/wine-info-search-skill) <br>
- [Wine Data Source Reference](references/api_reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown and terminal text with structured wine details, price links, WebFetch hints, and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only output; optional Firecrawl and OCR paths depend on user-provided configuration and installed dependencies.] <br>

## Skill Version(s): <br>
1.7.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
