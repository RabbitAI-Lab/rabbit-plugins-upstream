## Description: <br>
Poyo Gpt 4o Image helps an agent prepare, submit, and track PoYo GPT-4o Image generation or image-editing jobs through PoYo's external API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Use this skill when an agent needs to choose a PoYo GPT-4o Image model, assemble a compatible payload, submit a request with a PoYo API key, and report the returned task identifier for later polling or webhook follow-up. <br>

### Deployment Geography for Use: <br>
No geography restrictions are stated in the release evidence. Use where PoYo's service, the publisher's terms, and local policy permit sending prompts, image URLs, callback URLs, and generated-image requests to PoYo. <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, image URLs, and callback URLs are sent to PoYo's external service. <br>
Mitigation: Do not include secrets or private content unless the user is comfortable sending that data to PoYo. <br>
Risk: The skill requires a PoYo API key for authenticated requests. <br>
Mitigation: Set POYO_API_KEY as an environment variable and avoid passing the key directly on the command line. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-gpt-4o-image) <br>
- [PoYo model page](https://poyo.ai/models/gpt-4o-image-api) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text] <br>
**Output Format:** [Concise model-selection guidance, JSON payload details or summaries, curl or shell command usage, and task tracking notes.] <br>
**Output Parameters:** [PoYo model id, prompt, optional reference image URLs, optional size, optional image count, optional mask URL, optional callback URL, and POYO_API_KEY environment configuration.] <br>
**Other Properties Related to Output:** [If a request is submitted, the agent should report the returned task_id and the next step for status polling or webhook handling.] <br>

## Skill Version(s): <br>
1.0.1 <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
