## Description: <br>
Transforms long-form source content into platform-specific social and newsletter drafts for Twitter/X, LinkedIn, email, Instagram, and Threads. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[audsmith28](https://clawhub.ai/user/audsmith28) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Creators, marketers, agencies, and content teams use this skill to adapt one source article, transcript, or notes file into drafts for multiple publishing channels. It is intended to help prepare channel-specific text while preserving a configured voice and style. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security summary says the current implementation appears to output canned demo posts rather than true adaptations of the user's source content. <br>
Mitigation: Review generated drafts against the original source before publishing, and avoid relying on the outputs for production campaigns until the generation path is confirmed. <br>
Risk: The main script can fetch user-supplied URLs and falls back to curl plus html2text. <br>
Mitigation: Use trusted URLs only, confirm required dependencies are installed, and avoid fetching private or access-controlled content unless the data flow has been reviewed. <br>
Risk: Setup and execution create local configuration, examples, logs, and per-platform output files under user-configurable directories. <br>
Mitigation: Run setup in a controlled workspace, inspect configured output paths, and avoid storing sensitive brand details in configuration until retention expectations are clear. <br>
Risk: The skill may copy the highest-priority generated draft to the clipboard when clipboard copying is enabled. <br>
Mitigation: Set copy_to_clipboard to none for sensitive workflows or verify clipboard contents before switching contexts. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/audsmith28/content-repurposer) <br>
- [Publisher Profile](https://clawhub.ai/user/audsmith28) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Text and Markdown files written to a local output directory, with shell command guidance for setup and execution.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses configurable platform settings, can fetch URL input, writes per-platform draft files, and may copy the highest-priority output to the clipboard when configured.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
