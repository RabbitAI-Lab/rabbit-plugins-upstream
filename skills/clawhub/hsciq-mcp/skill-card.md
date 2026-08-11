## Description: <br>
HSCIQ MCP helps agents query HS codes, tariff rates, declaration elements, regulatory requirements, and classification examples through the HSCIQ MCP API, and create classification consultation requests with product images for expert review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[toucao](https://clawhub.ai/user/toucao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External trade, customs, and compliance users can use this skill to look up HS codes, tariff rates, declaration elements, regulatory requirements, CIQ items, hazardous-goods information, ports, and prior classification examples. When an automated lookup is not enough, the skill can submit product information and images to HSCIQ for classification consultation and expert review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Consultation submissions may send selected product descriptions, images, and optional contact details to HSCIQ for processing and possible human expert review. <br>
Mitigation: Install only when authorized to submit that information, and redact confidential or regulated business information before using consultation features. <br>
Risk: Requests use a configured base URL and API key source, so misconfiguration could send data to an unintended endpoint or use the wrong credential. <br>
Mitigation: Verify the HSCIQ base URL, authentication header, and API key source before deployment. <br>


## Reference(s): <br>
- [HSCIQ MCP API Documentation](https://www.hsciq.com/MCP/Docs) <br>
- [HSCIQ Service](https://www.hsciq.com) <br>
- [ClawHub Skill Page](https://clawhub.ai/toucao/skills/hsciq-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an HSCIQ API key; consultation workflows may submit product descriptions, product images, and optional contact details to HSCIQ.] <br>

## Skill Version(s): <br>
3.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
