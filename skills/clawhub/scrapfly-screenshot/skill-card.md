## Description: <br>
Capture web page screenshots using the Scrapfly Screenshot API with the Python SDK. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scrapfly](https://clawhub.ai/user/scrapfly) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to add Scrapfly-powered website screenshot capture to agent workflows, including full-page, viewport, element-specific, geo-targeted, and JavaScript-rendered screenshots. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Target URLs, rendered page contents, and screenshots are sent to Scrapfly. <br>
Mitigation: Use the skill only for pages approved for third-party processing, and avoid private dashboards, authenticated sessions, regulated data, or visible secrets unless authorization is documented. <br>
Risk: Custom JavaScript can alter the page before capture. <br>
Mitigation: Keep custom JavaScript narrow, reviewable, and limited to the intended visual changes before execution. <br>


## Reference(s): <br>
- [Scrapfly Screenshot API endpoint](https://api.scrapfly.io/screenshot) <br>
- [Scrapfly Python SDK ScreenshotConfig reference](https://raw.githubusercontent.com/scrapfly/python-scrapfly/master/scrapfly/screenshot_config.py) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with Python and shell code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces agent guidance for calling a third-party screenshot API and handling binary screenshot files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
