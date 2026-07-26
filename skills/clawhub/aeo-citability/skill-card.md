## Description: <br>
Make a static site answer-engine-citable by adding JSON-LD, clean Markdown siblings, llms.txt, and a sitemap so answer engines can parse and cite it. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[workloftai](https://clawhub.ai/user/workloftai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, site owners, and content teams use this skill to audit static HTML pages and add machine-readable citation surfaces for answer engines. It supports in-place JSON-LD updates plus generated Markdown, llms.txt, and sitemap.xml files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can edit selected static-site HTML files and create Markdown, llms.txt, and sitemap.xml files. <br>
Mitigation: Run audit and dry-run previews first, review the planned changes, and apply writes only on a version-controlled site. <br>
Risk: Generated citation metadata may reflect incomplete or inaccurate source page titles, descriptions, dates, images, or FAQ answers. <br>
Mitigation: Review generated JSON-LD, Markdown siblings, llms.txt, and sitemap.xml before publishing or requesting a recrawl. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/workloftai/skills/aeo-citability) <br>
- [Workloft Ships](https://workloft.ai/ships) <br>
- [Workloft support](https://workloft.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and generated site files including JSON-LD, Markdown, llms.txt, and sitemap.xml] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs locally with Python 3 standard library and no network calls; write operations support dry-run previews and are designed to be idempotent.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
