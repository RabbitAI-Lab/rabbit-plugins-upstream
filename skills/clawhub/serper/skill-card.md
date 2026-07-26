## Description: <br>
Google search via Serper API with full page content extraction, combining fast API lookup with concurrent page scraping and explicit locale controls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nesdeq](https://clawhub.ai/user/nesdeq) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to answer current or research-oriented questions by running a focused Google search through Serper and returning enriched page content in one streamed result set. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries are sent to Serper and result pages are fetched from third-party sites. <br>
Mitigation: Do not use the skill for secrets, private project names, regulated data, or confidential investigations unless that external disclosure is acceptable. <br>


## Reference(s): <br>
- [Serper API](https://serper.dev) <br>
- [ClawHub Skill Page](https://clawhub.ai/nesdeq/skills/serper) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Streamed JSON search metadata and enriched result objects, with Markdown and shell-command guidance in the skill documentation.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Serper API key and may send search queries to Serper while fetching third-party result pages for extraction.] <br>

## Skill Version(s): <br>
3.0.2 (source: server release metadata; artifact metadata lists 3.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
