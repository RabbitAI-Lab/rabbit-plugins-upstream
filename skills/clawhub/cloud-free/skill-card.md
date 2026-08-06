## Description: <br>
cloud-free helps consumers choose a primary cloud storage service for their device mix and clarify common sync and storage-quota misunderstandings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Consumers and personal-device support agents use this skill to pick an appropriate consumer cloud storage service and explain common issues such as iCloud quota confusion, cross-device sync behavior, and duplicate photo backups. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests file, command execution, write, and API-style capabilities beyond its consumer cloud-storage advice purpose. <br>
Mitigation: Install only with constrained tool access or revise the skill to passive advice-only behavior before deployment. <br>
Risk: The broad Operations activation scope may cause the skill to run for unrelated infrastructure or automation tasks. <br>
Mitigation: Limit activation to consumer cloud-storage selection and sync or quota explanations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/cloud-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown or JSON-formatted recommendation text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Recommendations are limited to consumer cloud storage selection and common sync or quota explanations.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
