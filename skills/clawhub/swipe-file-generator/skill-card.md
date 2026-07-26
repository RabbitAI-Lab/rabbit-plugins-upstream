## Description: <br>
Analyzes high-performing content from URLs and builds a local swipe file with reusable content patterns, psychological techniques, and frameworks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vincentchan](https://clawhub.ai/user/vincentchan) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Creators, marketers, and content strategists use this skill to analyze supplied URLs for why content works and to maintain a reusable swipe file of structures, hooks, psychological patterns, and recreatable templates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill fetches content from user-provided URLs, including Twitter/X URLs through FxTwitter. <br>
Mitigation: Only provide URLs you are comfortable having fetched by the agent and, for Twitter/X links, sent through FxTwitter. <br>
Risk: The skill creates or updates local files under swipe-file/, including the master swipe file and digested URL registry. <br>
Mitigation: Review existing swipe-file/ content before running the skill when manual edits need to be preserved. <br>
Risk: Failed URL fetches may leave some requested content unanalyzed. <br>
Mitigation: Check the skill's summary for failed URLs and retry or replace those sources before relying on the swipe file as complete. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/vincentchan/skills/swipe-file-generator) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Configuration] <br>
**Output Format:** [Markdown analysis blocks, JSON registry entries, and local file updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes and updates files under swipe-file/ and reports processed and failed URLs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
