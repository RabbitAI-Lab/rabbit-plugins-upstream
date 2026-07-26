## Description: <br>
Helps users choose launch timing by comparing candidate windows, industry events, competitor activity, review-buffer needs, and embargo lift details. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing, launch, and product teams use this skill to compare launch windows, account for event and competitor timing, select a launch-week or rolling-release format, and define an embargo lift moment before handing the proposal to a launch registry. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Launch dates, review buffers, or embargo lift details could be saved before the team confirms they are correct. <br>
Mitigation: Review proposed dates, buffers, and embargo details before allowing them to be saved or promoted. <br>
Risk: Connector results, calendar exports, and pasted launch data may contain unreliable or adversarial content. <br>
Mitigation: Treat fetched and pasted data as untrusted input and keep source labels such as Measured, User-provided, or Estimated in the recommendation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/launch-window-planner) <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown with candidate-window tables, rationale, embargo details, and handoff summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Labels launch timing inputs as Measured, User-provided, or Estimated; proposed dates and embargo facts are candidates until reviewed and saved by the registry workflow.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
