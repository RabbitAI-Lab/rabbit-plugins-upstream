## Description: <br>
Adds new language translations to customer service response templates and syncs the updated content across local files, Feishu Wiki, and GitHub. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[terrycarter1985](https://clawhub.ai/user/terrycarter1985) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and support operations teams use this skill to maintain complete multilingual customer-service template coverage, then publish or track those updates in Feishu Wiki and GitHub. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: External sync steps can publish template changes to Feishu Wiki, GitHub, or git targets. <br>
Mitigation: Review the markdown and changelog content, confirm the Feishu space or document and GitHub repository, and skip external sync for local-only translation work. <br>
Risk: Feishu and GitHub credentials grant write access to external systems. <br>
Mitigation: Use least-privilege tokens scoped to the intended space or repository and avoid sharing credentials in prompts, logs, or committed files. <br>
Risk: Translation updates can create inconsistent or incomplete customer-service responses. <br>
Mitigation: Verify every template has each required language subsection, preserve placeholders exactly, and use native-speaker review for production content. <br>


## Reference(s): <br>
- [Feishu Wiki API Notes](references/feishu-api.md) <br>
- [Translation Quality Guide](references/translation-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with bash command blocks and generated synchronization or issue content] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May update local markdown, create or update Feishu Wiki documents, create GitHub issues, and optionally prepare git commits when the agent runs the bundled commands.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
