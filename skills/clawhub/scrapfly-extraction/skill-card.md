## Description: <br>
Extract structured data from web content using the Scrapfly Extraction API with the Python SDK. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scrapfly](https://clawhub.ai/user/scrapfly) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to extract structured data from HTML, markdown, text, or scraped web pages with Scrapfly prompts, pre-trained extraction models, or templates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: HTML, markdown, text, or scraped page content processed with this skill is sent to Scrapfly for extraction. <br>
Mitigation: Use only with data approved for Scrapfly processing; avoid secrets, regulated data, customer data, and private internal pages unless Scrapfly is approved for that data. <br>
Risk: The Scrapfly API key could be exposed if embedded in source code, prompts, or logs. <br>
Mitigation: Store SCRAPFLY_API_KEY in an environment variable or secrets manager and avoid logging it. <br>


## Reference(s): <br>
- [Scrapfly Extraction API endpoint](https://api.scrapfly.io/extraction) <br>
- [Saved Extraction Templates](https://scrapfly.io/docs/extraction-api/templates) <br>
- [Extraction Rules and Templates](https://scrapfly.io/docs/extraction-api/rules-and-template#rules) <br>
- [ClawHub skill page](https://clawhub.ai/scrapfly/skills/scrapfly-extraction) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown guidance with Python and shell code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Describes Scrapfly extraction calls that return structured data, typically JSON-compatible.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
