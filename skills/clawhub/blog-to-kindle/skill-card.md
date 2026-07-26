## Description: <br>
Scrape blogs/essay sites and compile into Kindle-friendly EPUB with AI-generated cover. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ainekomacx](https://clawhub.ai/user/ainekomacx) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users can use this skill to fetch supported blog or essay archives, compile the content into Kindle-friendly EPUB files, and optionally send the result to a Kindle address. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send generated files through Mail.app to a built-in personal Kindle address. <br>
Mitigation: Remove the built-in address, require an explicit recipient for each send, and confirm the file and destination before allowing Mail.app or osascript to send. <br>
Risk: Fetched blog content and generated EPUB files may be incorrect, incomplete, or larger than expected. <br>
Mitigation: Run fetching and EPUB generation locally first, inspect the output, and check file size before delivery. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ainekomacx/skills/blog-to-kindle) <br>
- [Manual Blog-to-Kindle Workflow](references/manual-workflow.md) <br>
- [Paul Graham essays archive](https://paulgraham.com/articles.html) <br>
- [Kevin Kelly The Technium](https://kk.org/thetechnium/) <br>
- [Derek Sivers blog](https://sive.rs/blog) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, markdown, code, configuration] <br>
**Output Format:** [Markdown with inline shell commands, file paths, and workflow guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide generation of local markdown, EPUB, cover image, and email-delivery artifacts.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
