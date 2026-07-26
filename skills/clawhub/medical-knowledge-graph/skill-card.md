## Description: <br>
围绕疾病，药品，症状，诊断，并发症，饮食及其关系的知识图谱。仅限初步研究，具体应用需根据实际情况调整。 <br>

This skill is for research and development only. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Medical-domain researchers and developers can inspect a medical knowledge graph about diseases, medicines, symptoms, diagnoses, complications, diets, and relationships. The skill supports schema lookup and read-only Cypher queries for preliminary research, with practical use requiring review and adaptation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores a XiaoBenYang API key in a local .env file. <br>
Mitigation: Use a scoped or disposable key when possible, avoid sensitive workspaces, and remove XBY_APIKEY from .env when the skill is no longer needed. <br>
Risk: The skill depends on an external XiaoBenYang service and has unclear runtime disclosure. <br>
Mitigation: Install and run it only if the user trusts the service and is comfortable sending queries and credentials to that service. <br>
Risk: The medical knowledge graph is described as suitable only for preliminary research. <br>
Mitigation: Validate outputs with appropriate domain review before any practical or clinical use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/medical-knowledge-graph) <br>
- [ALinkLab publisher profile](https://clawhub.ai/user/alinklab) <br>
- [XiaoBenYang service](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Guidance] <br>
**Output Format:** [JSON results summarized as text or Markdown] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns raw API data with success and message fields; requires a XiaoBenYang API key.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter: 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
