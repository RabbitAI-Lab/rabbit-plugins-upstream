## Description: <br>
Generate AI-powered presentations, documents, and social posts through the Gamma.app API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lucassynnott](https://clawhub.ai/user/lucassynnott) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to ask an agent to create Gamma presentations, pitch decks, documents, reports, or social carousels from prompts or user-provided content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, documents, and file contents provided to the skill are sent to Gamma.app using the user's Gamma API key. <br>
Mitigation: Avoid submitting secrets, private keys, regulated data, or confidential business material unless Gamma use is approved. <br>
Risk: An autonomous agent could choose local files for upload without sufficient user review. <br>
Mitigation: Require users to explicitly select or provide content before generation, and review inputs before running the script. <br>


## Reference(s): <br>
- [ClawHub Gamma skill page](https://clawhub.ai/lucassynnott/skills/gamma) <br>
- [Gamma generation API endpoint](https://public-api.gamma.app/v1.0/generations) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API calls, Text, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and text status output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires GAMMA_API_KEY. Generation may return a Gamma URL, generation status, and credit usage.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
