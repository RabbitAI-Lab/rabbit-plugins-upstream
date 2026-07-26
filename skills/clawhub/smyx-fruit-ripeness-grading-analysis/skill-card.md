## Description: <br>
Grades tomato and strawberry ripeness from fruit images or videos by detecting color, colored-area ratio, gloss, and relative size, then returns maturity grades and harvest-window guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Growers, greenhouse operators, home gardeners, and produce cooperatives use this skill to assess tomato or strawberry ripeness from submitted media and receive structured grading plus harvest-timing guidance. Agents can invoke it for image or video analysis, report generation, and cloud report-history lookup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Submitted fruit images, videos, or URLs may be processed by configured LifeEmergence cloud services. <br>
Mitigation: Use only media appropriate for external processing, and avoid sensitive content until the publisher documents retention, deletion, and account controls. <br>
Risk: The skill can silently create or reuse a local workspace identity and link cloud report history to that identity. <br>
Mitigation: Review identity and report-state behavior before installation, and run in a dedicated workspace when separation from other activity matters. <br>
Risk: Evidence.security marks this release as suspicious because account creation, token storage, report retention, and leftover pet/video-analysis references need review. <br>
Mitigation: Install only after reviewing the publisher documentation and configured service endpoints, and reassess after those behaviors are clarified or cleaned up. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fruit-ripeness-grading-analysis) <br>
- [Skill usage demo](https://lifeemergence.com/sample.html) <br>
- [API interface documentation](artifact/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown and JSON-oriented structured analysis reports, with optional Markdown tables for report history] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can return ripeness grades, harvest recommendations, report links, and saved report output when an output path is supplied.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata and target metadata; artifact frontmatter states 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
