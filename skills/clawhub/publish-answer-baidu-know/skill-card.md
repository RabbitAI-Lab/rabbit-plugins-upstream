## Description: <br>
Publishes a locally prepared answer draft to a specified Baidu Zhidao question page. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[masterdxd](https://clawhub.ai/user/masterdxd) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content operations and brand teams use this skill to publish prepared FAQ, product, or support answers to individual Baidu Zhidao questions while preserving local execution records. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can post publicly to Baidu Zhidao using a saved browser and account session. <br>
Mitigation: Review the target question URL, selected account, and answer file before each run, and use idempotency keys to reduce accidental duplicate posting. <br>
Risk: The server scanner reports under-disclosed browser evasion and local profile fallback behavior. <br>
Mitigation: Install only when this browser behavior is acceptable for the environment, and monitor local browser-profile use and task records. <br>
Risk: Optional AI-generated answer optimization can change content before posting. <br>
Mitigation: Avoid the direct_rpa_run.py --optimize/--auto-approve path unless external AI generation and automatic approval are intentional. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/masterdxd/skills/publish-answer-baidu-know) <br>
- [Publisher profile](https://clawhub.ai/user/masterdxd) <br>
- [CLI contract](references/CLI.md) <br>
- [Data schema](references/SCHEMA.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON status records] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local task logs and answer publish records containing account IDs, question URLs, answer file paths, status, and platform messages.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
