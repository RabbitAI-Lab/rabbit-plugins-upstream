## Description: <br>
Guides an agent through an interactive SWOT analysis by collecting user-provided strengths, weaknesses, opportunities, and threats, then generating SO/WO/ST/WT strategy recommendations and presentation-ready outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Business, product, project, supplier, and strategy teams use this skill to structure a SWOT interview, keep the analysis grounded in user-provided evidence, and turn the confirmed quadrants into strategy options for decision-making and presentation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Incomplete or low-quality user inputs can produce misleading SWOT conclusions. <br>
Mitigation: Collect each SWOT quadrant from the user, label missing quadrants as unconfirmed, and ask the user to confirm strategy recommendations before finalizing the report. <br>
Risk: Referenced helper files for templates and report generation are absent from the inspected artifact, so automated Markdown and HTML generation may not work as described. <br>
Mitigation: Verify the referenced assets and report builder are available before relying on automated file generation, or have the agent produce the Markdown and HTML directly from the confirmed structure. <br>


## Reference(s): <br>
- [Source repository](https://github.com/duding-engicool/skill-swot-analysis) <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-swot-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code] <br>
**Output Format:** [Interactive prompts, structured Markdown report, and HTML report] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user confirmation of the SWOT quadrants, derived strategies, and report outline before final output.] <br>

## Skill Version(s): <br>
0.1.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
