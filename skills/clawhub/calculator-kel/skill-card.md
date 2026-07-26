## Description: <br>
A Model Context Protocol (MCP) numeric calculator skill for addition, subtraction, multiplication, division, powers, square roots, and integer factorials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers can use this skill to route basic arithmetic requests through MCP-backed tools and return the calculated result. The skill requires a xiaobenyang.com API key and sends calculation inputs to an external service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill presents calculator functions but sends inputs to a remote service and requires an external API key. <br>
Mitigation: Use only when the publisher and xiaobenyang.com endpoint are trusted, and avoid sending sensitive or confidential calculation inputs. <br>
Risk: The required API key may be stored in a local .env file. <br>
Mitigation: Protect the local .env file, rotate the API key if exposed, and remove the key when the skill is no longer needed. <br>


## Reference(s): <br>
- [XiaoBenYang API key site](https://xiaobenyang.com) <br>
- [ClawHub skill listing](https://clawhub.ai/cainingnk/skills/calculator-kel) <br>


## Skill Output: <br>
**Output Type(s):** [Text, API Calls, Configuration] <br>
**Output Format:** [Structured JSON tool responses summarized as text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires XBY_APIKEY; arithmetic inputs are sent to an external service.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
