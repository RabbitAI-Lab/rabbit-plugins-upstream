## Description: <br>
ct-advisor helps agents answer clinical-trial methodology, design, regulatory, quality-control, safety, and writing questions from a local knowledge pack, route data or sample-size needs to sibling ct-series skills, and assemble competitive-intelligence briefs from those outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[medstatstar](https://clawhub.ai/user/medstatstar) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External clinical-trial practitioners, clinicians, nurses, and medical students use ct-advisor to scope clinical-development questions, get methodology and regulatory guidance, prepare sample-size handoffs, and coordinate public-data retrieval through related ct-series skills. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Clinical and regulatory guidance may be outdated or insufficient for submission decisions. <br>
Mitigation: Verify clinical, statistical, and regulatory conclusions against official sources before using them for deadlines, version-sensitive requirements, or submissions. <br>
Risk: The server security summary reports that the shipped config can enable unencrypted local Q&A logging despite documentation saying logging is off by default. <br>
Mitigation: Review config.json before installing; remove or disable qa_store.mode: local unless unencrypted records in data/qa_log.jsonl are intentionally desired. <br>
Risk: Real-data and sample-size tasks depend on sibling ct-series skills and can be incomplete if those skills are missing or their outputs are stale. <br>
Mitigation: Confirm required sibling skills are installed, label unavailable retrieval as data not retrieved, and attach source/date labels to data-grounded claims. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/medstatstar/skills/ct-advisor) <br>
- [Publisher profile](https://clawhub.ai/user/medstatstar) <br>
- [Project homepage](https://github.com/medstatstar/ct-advisor) <br>
- [English README](README.md) <br>
- [Chinese README](README_zh-CN.md) <br>
- [ICH official guidance](https://www.ich.org) <br>
- [NMPA](https://www.nmpa.gov.cn) <br>
- [CDE](https://www.cde.org.cn) <br>
- [FDA](https://www.fda.gov) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with structured sections, citations, handoff payloads, and occasional shell commands or configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Bilingual response behavior; public-data claims should be labeled with source and date when sibling skills are used.] <br>

## Skill Version(s): <br>
0.8.2 (source: evidence.release.version and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
