## Description: <br>
Higgsfield AI connects an agent to Higgsfield AI through OOMOL's oo CLI for request status checks, text-to-image generation, image-to-video generation, and queued request cancellation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to operate a connected Higgsfield AI account through OOMOL for generation workflows, progress checks, output retrieval, and queued job cancellation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can submit Higgsfield AI generation requests through the user's connected OOMOL account. <br>
Mitigation: Confirm generation prompts and payloads with the user before running write actions. <br>
Risk: The skill can cancel queued Higgsfield AI generation requests. <br>
Mitigation: Confirm the exact request ID and cancellation target before running the cancellation action. <br>
Risk: First-time setup commands can install the oo CLI or initiate account connection steps. <br>
Mitigation: Run installer, login, or connection commands only when an action fails because setup is missing or expired. <br>


## Reference(s): <br>
- [Higgsfield AI homepage](https://higgsfield.ai/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-higgsfield-ai) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, JSON, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the live connector schema before submitting action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
