## Description: <br>
Grades tomato and strawberry ripeness from images or videos by analyzing visual cues such as color, colored-area ratio, gloss, and relative size, then produces a structured maturity report and harvest guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Growers, greenhouse operators, home gardeners, fruit and vegetable cooperatives, and agents assisting them use this skill to evaluate tomato or strawberry images and videos, classify maturity stages, and retrieve prior grading reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Submitted fruit images, videos, or URLs are processed by the Life Emergence cloud service. <br>
Mitigation: Install only when this cloud processing is acceptable for the data being analyzed. <br>
Risk: The skill silently creates or reuses a local/default identity and can store authentication tokens locally. <br>
Mitigation: Review workspace data files before and after use, especially data/smyx-api-key.txt and the local SQLite database, and prefer releases with explicit account, retention, and deletion controls. <br>
Risk: Fruit maturity output is decision support and may be unsuitable as the sole basis for commercial grading. <br>
Mitigation: Use the result as harvest guidance and pair commercial grading decisions with human or enterprise-standard review. <br>


## Reference(s): <br>
- [API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fruit-ripeness-grading-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, guidance] <br>
**Output Format:** [Structured text or Markdown, with JSON available through the detailed output mode and optional file output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can include maturity classifications, visual observations, harvest guidance, history tables, and report links.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact frontmatter reports 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
