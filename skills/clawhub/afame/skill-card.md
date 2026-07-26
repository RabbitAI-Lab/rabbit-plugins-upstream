## Description: <br>
Generate diverse creative illustrations via the OpenAI Images API for book illustrations, editorial art, children's book art, concept illustrations, and artistic scenes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[adebayoabdushaheed-a11y](https://clawhub.ai/user/adebayoabdushaheed-a11y) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, developers, and content creators use this skill to generate illustration prompts and image assets for stories, editorials, presentations, children's books, and concept art. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Illustration prompts and related parameters are sent to OpenAI or a configured OpenAI-compatible endpoint. <br>
Mitigation: Avoid confidential prompt content and verify OPENAI_BASE_URL or OPENAI_API_BASE before running. <br>
Risk: The skill requires an OpenAI API key for image generation. <br>
Mitigation: Use a scoped API key and provide it through OPENAI_API_KEY or the command-line option only in trusted environments. <br>
Risk: Generated index.html galleries may include prompt content supplied by the user. <br>
Mitigation: Be cautious when opening generated galleries from untrusted prompt content. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/adebayoabdushaheed-a11y/skills/afame) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Images, JSON, HTML] <br>
**Output Format:** [Command-line output plus PNG image files, prompts.json metadata, and an index.html gallery] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses an OpenAI or OpenAI-compatible Images API endpoint and writes generated assets to a local output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
