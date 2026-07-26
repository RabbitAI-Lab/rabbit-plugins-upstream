## Description: <br>
Route model requests based on configured models, costs, and task complexity. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mrjootta](https://clawhub.ai/user/mrjootta) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to select an appropriate LLM for a request from a configured model list, balancing task complexity, capability needs, and cost. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The router may select any provider or model listed in the supplied configuration, which can affect cost or where prompts are sent by the surrounding application. <br>
Mitigation: Review and control the models JSON before use, and include only providers and models approved for the deployment environment. <br>
Risk: The documented --mode auto example appears unsupported by the included script. <br>
Mitigation: Use the supported CLI options shown by the script, such as --models, --task, --min-capability, --prefer, and --dry. <br>


## Reference(s): <br>
- [Model Router on ClawHub](https://clawhub.ai/mrjootta/skills/model-router-premium) <br>
- [Example model configuration](examples/models.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [JSON model selection with short text reasoning, plus CLI usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Selection depends on the supplied models JSON, task text, optional minimum capability, and optional provider or model preference.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
