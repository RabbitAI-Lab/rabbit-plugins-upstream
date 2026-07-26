## Description: <br>
Make a site citable by AI engines through crawler allowlists, stable Schema.org @graph IDs, IndexNow sitemap submission, and answer-first page structure. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alexbloch-ia](https://clawhub.ai/user/alexbloch-ia) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, SEO/GEO practitioners, and site owners use this skill to audit public site visibility in AI answer engines and prepare reviewable robots.txt, llms.txt, Schema.org, sitemap, IndexNow, and answer-first content changes for sites they control. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated SEO/GEO changes may introduce inaccurate or unsupported public claims. <br>
Mitigation: Review drafted copy, facts, dates, sources, and author attribution before publishing. <br>
Risk: IndexNow key material can become persistent if committed to source control. <br>
Mitigation: Keep INDEXNOW_KEY in the environment, generate the required key file outside versioned source, and ignore the key file path in git. <br>
Risk: Public robots.txt, llms.txt, or schema files can disclose sensitive paths or non-public business details. <br>
Mitigation: Publish only information already safe for the public web and protect sensitive resources with authentication or noindex controls rather than robots.txt alone. <br>
Risk: Benchmarking and demand-signal workflows can expose competitor names or customer data in shareable outputs. <br>
Mitigation: Use public pages, anonymize competitors as A/B/C in shareable materials, and use only aggregated human-provided demand themes. <br>
Risk: Optional IndexNow submission can fail or target URLs outside the verified domain if environment settings are wrong. <br>
Mitigation: Set INDEXNOW_HOST deliberately, verify the domain in the search console, and submit only public sitemap URLs for a site the user controls. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alexbloch-ia/skills/ai-search-visibility) <br>
- [Playbooks](artifact/references/playbooks.md) <br>
- [robots.txt template](artifact/templates/robots.txt) <br>
- [llms.txt template](artifact/templates/llms.txt) <br>
- [Schema.org @graph template](artifact/templates/graph.json) <br>
- [IndexNow ping script](artifact/scripts/indexnow-ping.js) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with tables, code blocks, JSON, robots.txt, and llms.txt templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces reviewable audit tables, rewrite plans, configuration templates, and optional IndexNow sitemap submission commands for public URLs owned by the user.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
