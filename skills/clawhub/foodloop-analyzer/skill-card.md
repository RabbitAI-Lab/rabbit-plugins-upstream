## Description: <br>
Reverse-engineer and analyze a FoodLoop AI deployment when given a FoodLoop AI URL, including its workflow, API, and architecture. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[justhackr](https://clawhub.ai/user/justhackr) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and auditors use this skill to inspect FoodLoop AI deployments they own or are authorized to test, map frontend and FastAPI backend behavior, trace user workflows, and document endpoint and schema findings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Live API probes can trigger state-changing requests against a FoodLoop deployment. <br>
Mitigation: Run only against deployments you own or are explicitly authorized to test, and prefer test environments for POST requests. <br>
Risk: Photo analysis can involve personal or sensitive images. <br>
Mitigation: Upload images only with consent, avoid sensitive photos, and delete temporary image files and saved reports after use. <br>


## Reference(s): <br>
- [FoodLoop Analyzer ClawHub page](https://clawhub.ai/justhackr/skills/foodloop-analyzer) <br>
- [FoodLoop API Workflow Reference](references/api_workflow.md) <br>
- [FoodLoop live backend reference](https://foodrecycler.onrender.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown analysis notes with inline bash commands and API request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce local Markdown reports and temporary image upload files during authorized analysis.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
