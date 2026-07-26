## Description: <br>
This skill analyzes hydroponic root and leaf images or videos to qualitatively assess nutrient concentration status and provide adjustment guidance without producing EC or ppm values. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Hydroponic growers, plant-factory operators, and developers integrating plant monitoring workflows use this skill to analyze root and leaf media, identify visual stress indicators, and receive qualitative nutrient adjustment advice. It can also query cloud-hosted historical assessment records associated with the local user identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cloud analysis sends selected plant media and account-linked metadata to lifeemergence.com services. <br>
Mitigation: Use only intended hydroponic media, avoid unrelated private files, and confirm that sharing the media with the external service is acceptable before running analysis. <br>
Risk: The skill can create or reuse a local identity and store service tokens in the workspace data directory. <br>
Mitigation: Review or clear data/smyx-api-key.txt and smyx-common-claw.db before use, and restrict access to workspaces where those files may be created. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-hydroponic-nutrient-assessment-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Interface Documentation](artifact/references/api_doc.md) <br>
- [SMYX Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-like structured analysis text with optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include qualitative nutrient status, root and leaf observations, adjustment advice, historical report records, and report links when returned by the service.] <br>

## Skill Version(s): <br>
1.0.3 (source: server-resolved release metadata; artifact frontmatter reports 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
