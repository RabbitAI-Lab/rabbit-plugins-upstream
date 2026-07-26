## Description: <br>
Generates AI videos and images through the AI Director service, and helps query credits, task status, and generated works. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chenzhigao61](https://clawhub.ai/user/chenzhigao61) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users can use this skill to submit text-to-video, image-to-video, and text-to-image generation jobs, then check balances, task status, and generated works. It is best suited for users who have an AI Director API key and are comfortable using paid credits with the external service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends prompts, public image URLs, and account queries to the external AI Director service, and generated jobs may consume paid credits. <br>
Mitigation: Avoid submitting private images or sensitive prompts unless third-party processing is acceptable, and check credit balance before running generation jobs. <br>


## Reference(s): <br>
- [Seedance2.5 Skill on ClawHub](https://clawhub.ai/chenzhigao61/skills/seedance2-5skill) <br>
- [AI Director service](https://seedance25movie.coze.site) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Guidance] <br>
**Output Format:** [JSON responses and Markdown guidance with shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and AI_DIRECTOR_API_KEY; video tasks are asynchronous and should be polled for completion.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
