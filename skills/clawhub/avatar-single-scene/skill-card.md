## Description: <br>
Use when someone wants one polished host-on-camera beat: a speaking person with intake and approval gates before generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to plan and generate a single host-on-camera avatar clip from an approved portrait, script, voice, and motion plan. It guides intake, explicit approval gates, Pruna generation calls, polling, download, and manifest capture. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Portraits, scripts, optional audio, and prompt details may be sent to Pruna-related generation services. <br>
Mitigation: Use the skill only when the user is comfortable with those uploads, rely on approved media, and record intake answers before generation. <br>
Risk: Paid API credits may be consumed during avatar generation. <br>
Mitigation: Require explicit plan and still approvals before calling generation APIs, and do not combine planning with paid video generation in the same turn. <br>
Risk: A generated avatar can drift from the intended identity, voice, or scene plan. <br>
Mitigation: Reuse the approved portrait URL and voice settings, show the script and motion plan before generation, and keep the required review gates before final acceptance. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/avatar-single-scene) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Text] <br>
**Output Format:** [Markdown guidance with command examples and structured manifest notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes approval gates before paid generation and manifest capture of intake answers, prompts, URLs, retries, and prediction IDs.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
