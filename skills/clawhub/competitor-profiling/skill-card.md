## Description: <br>
Competitor Profiling helps agents research competitor URLs and produce structured, source-traceable competitor profile Markdown files using site scraping, SEO and market data, and standardized comparison templates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coreyhaines31](https://clawhub.ai/user/coreyhaines31) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing, product, and sales teams use this skill to turn competitor URLs into comparable competitor dossiers covering positioning, pricing, product signals, SEO strength, customer proof, and strategic implications. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Raw competitor research files may contain confidential product context, personal information from review pages, or licensed third-party page content. <br>
Mitigation: Review access controls and retention for competitor-profiles/raw/ and delete or restrict files that are not needed after synthesis. <br>
Risk: Competitor profiles can become stale as pricing pages, SEO rankings, and product positioning change. <br>
Mitigation: Use the generated date, save each run in a dated folder, and re-pull pricing, SEO metrics, and changelog data before relying on older profiles. <br>
Risk: Homepage claims, logo walls, and inferred weaknesses may be incomplete or misleading if used without corroboration. <br>
Mitigation: Cross-check claims against scraped pages, review sources, SEO data, and raw evidence folders, and clearly label inferences in the final profile. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/coreyhaines31/skills/competitor-profiling) <br>
- [Tool reference](artifact/references/tool-reference.md) <br>
- [Profile templates](artifact/references/templates.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, files, guidance] <br>
**Output Format:** [Markdown competitor profiles and summaries, plus raw Markdown and JSON evidence files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes dated raw scrape, SEO, and review data under competitor-profiles/raw/ and synthesized profiles under competitor-profiles/.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata; artifact metadata lists 2.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
